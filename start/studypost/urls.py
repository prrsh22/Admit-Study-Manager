from django.urls import path
from . import views

app_name = 'studypost'

urlpatterns = [
    path('notice/<int:id>', views.notice_home, name='notice_home'),
    path('notice_new/<int:id>', views.notice_new, name='notice_new'),

    path('notice_detail/<int:id>/', views.notice_detail, name='notice_detail'),

    path('notice_list/<int:id>/', views.notice_list, name='notice_list'),
    path('notice_edit/<int:id>/', views.notice_edit, name='notice_edit'),
    path('notice_delete/<int:id>/', views.notice_delete, name='notice_delete'),
    path('notice_download/<str:file_path>/', views.file_download, name='notice_download'),

    path('homework_new/<int:id>', views.homework_new, name='homework_new'),

    path('homework_detail/<int:id>/', views.homework_detail, name='homework_detail'),

    path('homework_list/<int:id>/', views.homework_list, name='homework_list'),
    path('homework_edit/<int:id>/', views.homework_edit, name='homework_edit'),
    path('homework_delete/<int:id>/', views.homework_delete, name='homework_delete'),
    path('homework_download/<str:file_path>/', views.file_download, name='homework_download'),
]