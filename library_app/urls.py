from django.urls import path

from library_app import views

urlpatterns = [
path('',views.Books.as_view()),
    path("Books_RUD/<int:pk>/",views.Books_RUD.as_view())
]