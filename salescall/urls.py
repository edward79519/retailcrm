from django.urls import path
from . import views


urlpatterns = [
    path('', views.callrecord_index, name='Callrecord_Index'),
    path('record/add/', views.record_add, name='Callrecord_Add'),
    path('record/<record_id>/', views.record_detail, name='Callrecord_Detail'),
    path('record/<record_id>/lock/', views.record_lock, name='Callrecord_Lock'),
    path('record/<record_id>/delete/', views.record_delete, name='Callrecord_Delete'),
    path('record/<record_id>/update/', views.record_update, name='Callrecord_Update'),
    path('comment/', views.comment_index, name='Comment_Index'),
]
