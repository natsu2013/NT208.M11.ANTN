from django.urls import path
from polls import views

urlpatterns = [
    #path('blog', views.blog, name='blog'),
    # path('feedback', views.feedback, name='feedback'),
    path('contact', views.handleFeedback, name='contact'),
    path('menu/<int:_id>', views.BlogDetailView, name='menu'),
]