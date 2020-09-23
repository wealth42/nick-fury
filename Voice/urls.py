from django.urls import path, include
from . import views


urlpatterns = [
    # path("", index),
    # path('dashboard', views.dashboard),
    # path('logout', views.logout),
    path('profile/', views.dashboard),
    path('profile/signature_upload', views.signature_upload, name = 'image_upload'),
    path("", include("django.contrib.auth.urls")),
    path("", include("social_django.urls")),
]

