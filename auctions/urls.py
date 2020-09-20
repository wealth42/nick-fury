from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<id>", views.listing, name="listing"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("listing/<id>/close", views.close, name="close"),
    path("listing/<id>/comment", views.comment, name="comment"),
    path("categories", views.categorylist, name="categorylist"),
    path("categories/<category>", views.category, name="category"),
]
