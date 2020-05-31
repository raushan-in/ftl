from django.urls import path

from . import views

urlpatterns = [
    path('member/', views.MemberActivityList.as_view(), name='member-activity'),
]
