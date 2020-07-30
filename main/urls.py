from django.urls import path
from . import views

urlpatterns = [
    # 홈 관리
    path('', views.home, name='home'),
    path('edit/', views.edit, name='edit'),

    # 프로젝트 관리
    path('detail/<int:pk>', views.project_detail, name='detail'),
    path('project_list/', views.project_list, name='project_list'),
    path('create_project/', views.create_project, name='create_project'),
    path('project_delete/<int:pk>', views.project_delete, name='project_delete'),
    path('project_edit/<int:pk>', views.project_edit, name='project_edit'),

    # 인트로덕션 관리
    path('intro_list/', views.intro_list, name='intro_list'),
    path('create_intro/', views.create_intro, name='create_intro'),
    path('intro_edit/<int:pk>', views.intro_edit, name='intro_edit'),
    path('intro_delete/<int:pk>', views.intro_delete, name='intro_delete'),
    path('intro/detail/<int:pk>', views.intro_detail, name='intro_detail'),

    # 프로필 관리
    path('profile_list/', views.profile_list, name='profile_list'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile_edit/<int:pk>', views.profile_edit, name='profile_edit'),
    path('profile_delete/<int:pk>', views.profile_delete, name='profile_delete'),
    path('profile/detail/<int:pk>', views.profile_detail, name='profile_detail'),
]