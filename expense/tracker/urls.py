from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('',views.homeview,name='home'),
    path('profile/<int:id>/',views.ProfileCreateView.as_view(),name='profile'),
]
