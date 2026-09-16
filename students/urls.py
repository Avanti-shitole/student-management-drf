from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()),
    path('students/<int:id>/', StudentDetailAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

]