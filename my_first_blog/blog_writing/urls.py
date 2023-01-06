from django.urls import path
from . import views

urlpatterns = [path('', views.PostView.as_view(), name='home'),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('about_us', views.about_us, name='about'),
               path('create', views.create, name='create'),
               path('review/<int:pk>/', views.AddComments.as_view(), name='comments'),

               ]