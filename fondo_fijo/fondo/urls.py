from django.urls import path
from .views import dashboard, movimientos_view

urlpatterns = [

    path(
        '',
        dashboard,
        name='dashboard'
    ),

    path(
        'movimientos/',
        movimientos_view,
        name='movimientos'
    ),
]