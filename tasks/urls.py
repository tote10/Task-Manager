from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet
from .views import RegisterView
from .views import LoginView
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]