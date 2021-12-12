from django.contrib import admin
from polls.models import Blog, Comment, Diet, Feedback

@admin.register(Feedback)
class feedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message')
    list_filter = ('name', 'email',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'title', 'description','images', 'link')
    list_filter = ('topic',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'commentText', 'blog', 'time')
    list_filter = ('name', 'blog', 'time')

@admin.register(Diet)
class personInfo(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'data')
    list_filter = ('type',)