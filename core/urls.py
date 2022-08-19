from django.urls import path
from . import views
from .ajax import ajax
from salescall import views as callviews

urlpatterns = [
    path('custom/', views.custom_index, name="Custom_Index"),
    path('custom/import/', views.custom_import, name="Custom_import"),
    path('custom/<comp_id>/', views.custom_detail, name="Custom_Detail"),
    path('addcustom/', views.custom_add, name="Custom_Add"),
    path('custom/<comp_id>/update/', views.custom_update, name='Custom_Update'),
    path('custom/<comp_id>/delete/', views.custom_delete, name='Custom_Delete'),
    path('custom/<comp_id>/firstcall/', callviews.firstcall, name='Custtom_First'),
    path('ajax/getcompinfo/', ajax.getcompinfo),
    path('ajax/delparti/', ajax.delparticipant),
    path('ajax/delcomment/', ajax.delcomment),
]
