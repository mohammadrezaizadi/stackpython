from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('time/<str:timeframe>/<str:symbolname>', views.MyTime, name='timef'),
    path('getsymbols/', views.GetSymbols, name='getsymbols'),
]