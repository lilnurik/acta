from django.contrib import admin
from .models import Article, User

admin.site.register(User)
admin.site.register(Article)