from django.urls import path
from . import views


urlpatterns = [
    path('', views.createcrud, name='createcrud'),
    path('delete/<int:pk>', views.deleteview, name='delete'),
    path('update/<int:pk>', views.updateview,  name='update')
]