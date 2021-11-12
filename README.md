# Dispo Backend Take Home

Create an API that allows users to create and like posts, and follow other users. 
For this assessment you should not need additional dependencies to complete the below.

And while not required, feel free to add additional flourishes or features!

## Complete the following:
1. Create endpoints `POST /users/create` and `POST /posts/create` to create a user  
   and a post. See `posts/models.py` for reference on what to supply in the request body  
   for posts. User endpoint should accept a `username` and `password`. A 201 HTTP status  
   code is the expected response.
   - sample create user request: `curl -X POST http://127.0.0.1:8000/users/create/ -H 'Content-Type: application/json' -d '{"username":"test2","password":"test2"}'`
   - sample create post request: `curl -X POST http://127.0.0.1:8000/posts/create/ -H "Content-Type: application/json" -d '{"body":"test1 first post!"}' --user "test1:test1"`
   - sample like post request: `curl -X POST http://127.0.0.1:8000/posts/like/ -H "Content-Type: application/json" -d '{"post":3}' --user "test1:test1"`
   
2. Create an endpoint `GET /users/top` that returns a list of users with one or more posts  
   sorted by number of posts authored descending.  The expected response is a list of:
   ```
   {
     "username": "<username>",
     "posts": <number of posts>
   }
   ```
   - sample request: `curl -X GET http://127.0.0.1:8000/users/top/`
    
3. Add (unidirectional) follow relationships to `User` and an endpoint `POST /users/follow`  
   that accepts a user id and a following user id from the request body 
   - sample request: `curl -X POST http://127.0.0.1:8000/users/follow/ -H "Content-Type: application/json" -d '{"follow":3}' --user "test1:test1"`

4. Create an endpoint `GET /users/feed/<user_id>` that returns a list of posts created  
   by the user or anyone they follow with number of likes received in reverse   
   chronological order. List items should have the following structure:
   ```
   {
     "id": "<post id>",
     "body": "<post body>",
     "author": "<post author's username>",
     "likes": <post like count>
   }
   ```
   - sample request: `curl -X GET http://127.0.0.1:8000/users/feed/2/`
   
## Setup
* If you have [Poetry](https://python-poetry.org) installed simply `poetry install` to  
  set  up you environment.  
    * If you don't want to use Poetry, create a virtual environment with `django` and   
      `djangorestframework` installed.
* Set up the SQLite database
    * Poetry: `poetry run python manage.py migrate`
    * Non-Poetry: `python manage.py migrate`
* Run the server (on port 8000)
    * Poetry: `poetry run python manage.py runserver`
    * Non-Poetry: `python manage.py migrate`

## Evaluation:

### What you will be evaluated on
* Functionality - can you translate the requirements into working code?
* Following modern best practices

### What you will not be evaluated on
* Testing

## Submission Instructions
Create a public GitHub repository. Share this GitHub URL with your point of contact.
