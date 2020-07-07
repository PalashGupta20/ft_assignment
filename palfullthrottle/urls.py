from django.urls import path

from . import views

urlpatterns = [
            path('user-activity-periods/', views.get_user_details, name='activity periods')
        ]
