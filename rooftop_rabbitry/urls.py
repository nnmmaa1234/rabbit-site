from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact-us/", views.contact_us, name="contact-us"),
    path("fish-farm/", views.fish_farm, name="fish-farm"),
    path("rabbit-farm/", views.rabbit_farm, name="rabbit-farm"),
    path("add-rabbit/", views.add_rabbit, name="add-rabbit"),
    path("add-breed/", views.add_breed, name="add-breed"),
    # path('', views.RabbitListView.as_view(), name='index'),
    # path('rabbit/<int:pk>/', views.rabbitDetailView.as_view(), name='rabbit_detail'),
    # path('rabbit/new/', views.rabbitCreateView.as_view(), name='rabbit_create'),
    # path('rabbit/<int:pk>/update/', views.rabbitUpdateView.as_view(), name='rabbit_update'),
    # path('rabbit/<int:pk>/delete/', views.rabbitDeleteView.as_view(), name='rabbit_delete'),
]