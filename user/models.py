from django.db import models
from django.contrib.auth.models import AbstractUser


"""
Model representing a user.
Fields:
- username: The user's username (primary key).
- password: The user's password.
- introduction: A brief introduction about the user.
- weight: The user's weight with a maximum of 3 digits and 2 decimal places.
- height: The user's height with a maximum of 3 digits and 2 decimal places.
- target: The user's target weight with a maximum of 3 digits and 2 decimal places.
- age: The user's age.
- gender: The user's gender (True for male, False for female).
- email: The user's email address.
- loseOradd: The user's plan is whether lose or add weight (True for lose, False for add).
"""
class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    introduction = models.TextField(max_length=100, null=True)
    email = models.EmailField()

class Administrator(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()

"""
Model representing a post.

Fields:
- title: The title of the post, with a maximum length of 50 characters.
- user: The user who created the post.
- created_at: The date and time the post was created.
- content: The content of the post, with a maximum length of 1000 characters.
"""
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    content = models.TextField(max_length=1000)


"""
Model representing a comment on a post.

Fields:
- user: The user who wrote the comment.
- post: The post to which the comment is associated.
- created_at: The date and time the comment was created.
- content: The content of the comment, with a maximum length of 100 characters.
"""
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    content = models.CharField(max_length=100)


"""
Model representing a reply to a comment.

Fields:
- comment: The comment to which the reply is associated.
- author: The user who wrote the reply.
- content: The content of the reply, with a maximum length of 100 characters.
- created_at: The date and time the reply was created.
"""
class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)