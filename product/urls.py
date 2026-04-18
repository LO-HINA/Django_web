from . import views
from django.urls import path

app_name = 'product'

urlpatterns = [
    path('detail1', views.product_detail1, name='detail1'),
    path('detail2', views.product_detail2, name='detail2'),
    path('detail3', views.product_detail3, name='detail3'),
    path('detail4', views.product_detail4, name='detail4'),
    path('detail5', views.product_detail5, name='detail5'),
    path('detail6', views.product_detail6, name='detail6'),
]