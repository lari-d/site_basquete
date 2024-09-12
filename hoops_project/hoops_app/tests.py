from django.test import TestCase
from django.contrib.auth.models import User

User.objects.create_user(username='user002', password='password')

user = User.objects.get(username='user002')
print(user)