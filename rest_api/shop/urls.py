from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^categories/', views.CategoryListView.as_view()),
    url(r'^items/(?P<pk>\d+)/delete$', views.ItemDestroyView.as_view()),
    url(r'^items/(?P<pk>\d+)/update$', views.ItemUpdateView.as_view()),
    url(r'^items/(?P<pk>\d+)$', views.ItemDetailView.as_view()),
    url(r'^items', views.ItemListView.as_view()),

]
