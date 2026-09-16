from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailAPIView, LoginAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()),
    path('students/<int:id>/', StudentDetailAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),

]