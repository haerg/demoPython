from django.urls import path

from . import views

urlpatterns = [
    path('institutions/', views.InstitutionList.as_view()),
    path('notifications/', views.NotificationList.as_view()),
    path('notifications/<int:pk>/', views.NotificationDetail.as_view()),
]