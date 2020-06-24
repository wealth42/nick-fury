from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, client, therapist

router = DefaultRouter()
router.register('journals', therapist.ViewJournalView, basename='journals')
router.register('clients', therapist.ClientsView, basename="clients")
router.register('new-clients', therapist.AvailableClientView, basename="new_clients")

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('chat/<int:id1>', views.ChatView.as_view(), name="ChatView"),

    path('therapist/', include(router.urls)),

    path('search-therapists', client.SearchTherapistView.as_view(), name="search_therapists"),
    path('map-therapist/<int:id1>', client.MapTherapistView.as_view(), name="map_therapist"),
    path('mapped-therapists', client.MappedTherapistsView.as_view(), name="mapped_therapists"),
    path('therapists-with-journal', client.TherapistsWithJournalAccessView.as_view(), name="therapists_with_journal"),
    path('remove-journal-access/<int:id1>', client.RemoveJournalAccessView.as_view(), name="remove_journal_access"),
    path('record-emotion/', client.RecordEmotionView.as_view(), name="record_emotion"),
]
