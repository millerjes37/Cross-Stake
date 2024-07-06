from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, TrainerViewSet, HorseViewSet

router = DefaultRouter()
router.register(r'owners', OwnerViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'horses', HorseViewSet)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('add_horse/', views.add_horse, name='add_horse'),
    path('', include(router.urls)),
]
