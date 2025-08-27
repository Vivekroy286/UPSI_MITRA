from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('papers/', views.papers_view, name='papers'),
    path('test/<int:paper_id>/instructions/', views.test_instructions, name='test_instructions'),
    path('test/<int:paper_id>/', views.test_view, name='test'),
    path('submit/', views.submit_test, name='submit_test'),
    path('results/', views.results_view, name='results'),
]