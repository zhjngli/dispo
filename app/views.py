from django.db.models import Count, Q
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer, PostLikeSerializer, UserSerializer, UserFollowSerializer
from .models import Post, User


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request):
    request.data['user'] = request.user.id
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def like_post(request):
    request.data['user'] = request.user.id
    serializer = PostLikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_top_users(request):
    # 'num_posts' can't be named 'posts' as it clashes with an existing field on the model
    users = User.objects.annotate(num_posts=Count('posts')).filter(num_posts__gt=0).order_by('-num_posts')
    # convert 'num_posts' field to 'posts' per requirement
    response_data = map(lambda v: {'username': v['username'], 'posts': v['num_posts']},
                        users.values('username', 'num_posts'))
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def follow(request):
    request.data['user'] = request.user.id
    serializer = UserFollowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_user_feed(request, user_id=None):
    if not user_id:
        return Response('Specify a user.', status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.get(id=user_id)
    following = map(lambda u: u.follow, user.following.all())
    all_posts = Post.objects \
        .filter(Q(user=user) | Q(user__in=following)) \
        .select_related('user') \
        .annotate(likes=Count('liked_by')) \
        .order_by('-timestamp')
    response_data = map(lambda p: {'id': p.id, 'body': p.body, 'author': p.user.username, 'likes': p.likes}, all_posts)
    return Response(response_data, status=status.HTTP_200_OK)
