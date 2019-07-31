from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.CateListView.as_view()),
    path('items/', views.ItemListView.as_view()),
]
