from django.contrib import admin
from .models import Comment,Post,Category,Profile
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)
# Register your models here.
