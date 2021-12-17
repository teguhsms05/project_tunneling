from django.urls import path
from . import views

app_name = 'domregis'

urlpatterns = [
    path('domain-register/', views.register_dom, name='register_dom'),
    path('delete/<int:task_id>', views.delete_dom, name='delete_dom'),
    path('cpanel-register/', views.register_cpanel, name='register_cpanel'),
    path('delete-cpanel/<int:task_id>', views.delete_cpanel, name='delete_cpanel'),
]

