from django.urls import path
from . import views

urlpatterns = [
    path('addcustom/', views.custom_add, name="Custom_Add"),
    path('custom/<comp_id>/update/', views.custom_update, name='Custom_Update'),
]
