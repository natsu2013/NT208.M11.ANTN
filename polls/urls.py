from django.urls import path
from polls import views

urlpatterns = [
    path('contact', views.handleFeedback, name='contact'),
    path('menu/<int:_id>', views.BlogDetailView, name='menu'),
]
