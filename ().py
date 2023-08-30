# coding: utf-8
from blog.models import Post
from django.contrib.auth.models import User
Post.objects.all()
post_2 = Post(title = 'Blog 2', content = 'Second Blog content', author = user)
user = User.objects.first()
post_2 = Post(title = 'Blog 2', content = 'Second Blog content', author = user)
