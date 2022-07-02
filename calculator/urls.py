from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sum', views.plus, name='plus'),
    path('minus',views.minus, name='minus'),
    path('prod', views.prod, name='prod'),
    path('quote', views.quote, name='quote'),
    path('ruijo', views.ruijo, name='ruijo'),
    path('about', views.about, name='about'),
    path('summation', views.summation),
    path('differ', views.difference),
    path('product', views.product),
    path('quotient', views.quotient),
    path('times', views.times),
]