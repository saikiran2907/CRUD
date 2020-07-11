from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_user,name='create_user'),
    path('view/',views.list_user, name='list_user'),
    path('delete/<int:id>/',views.delete_list, name='delete_list'),
    path('update/<int:id>/', views.update_list, name='update_list')
]