from django.urls import path
from . import views


urlpatterns = [
    path('addcallrecord/', views.callrecord_add, name='Callrecord_Add'),
    path('record/<record_id>/update/', views.callrecord_update, name='Callrecord_Update'),
    path('firstcall/custom/<comp_id>/', views.firstcall, name='Firstcall'),
    path('record/<record_id>/comment/add/', views.comment_add, name='Comment_Add'),
    path('comment/<cmt_id>/', views.comment_update, name='Comment_Update'),
]
