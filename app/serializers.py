from rest_framework import serializers

from .models import Post, PostLike, User, UserFollow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = User(id=validated_data['user'])
        post = Post(**validated_data)
        post.save()
        return post


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = User(id=validated_data['user'])
        validated_data['post'] = Post(id=validated_data['post'])
        post = PostLike(**validated_data)
        post.save()
        return post


class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = User(id=validated_data['user'])
        validated_data['follow'] = User(id=validated_data['follow'])
        post = UserFollow(**validated_data)
        post.save()
        return post
