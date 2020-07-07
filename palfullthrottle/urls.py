from django.urls import path

from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('user-activity-periods/', views.get_user_details, name='activity periods')
        ]
