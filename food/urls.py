from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/new/', views.create_category, name='create_category'),
    path('category/<int:pk>/edit/', views.update_category, name='update_category'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('food/new/', views.create_food, name='create_food'),
    path('food/<int:pk>/edit/', views.update_food, name='update_food'),
    path('food/<int:pk>/delete/', views.delete_food, name='delete_food'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('all-food/', views.all_food, name='all_food'),
    path('all-categories/', views.all_categories, name='all_categories'),
]