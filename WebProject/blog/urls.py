from django.urls import path
from . import views 

# Create your views here.

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categories/<int:categories_id>/', views.category, name="Category"),
]