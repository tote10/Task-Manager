from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet
from .views import RegisterView
from .views import LoginView
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
]