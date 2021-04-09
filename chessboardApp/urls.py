from django.urls import path

from . import views
app_name = "chess"
urlpatterns = [
    path('', views.home, name = "home"),
    path('reset', views.reset, name = "reset"),
    path('rules', views.rules),
    path('history', views.history),
    path('about', views.about),
]