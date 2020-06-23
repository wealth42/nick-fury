from django.urls import path
from . import views, client

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('search-therapists', client.SearchTherapistView.as_view(), name="search_therapists"),
    path('map-therapist/<int:id1>', client.MapTherapistView.as_view(), name="map_therapist"),
    path('mapped-therapists', client.MappedTherapistsView.as_view(), name="mapped_therapists"),
    path('therapists-with-journal', client.TherapistsWithJournalAccessView.as_view(), name="therapists_with_journal"),
]
