from django.urls import path
from .views import glucose_list_view, glucose_detail_view, glucose_create_view, glucose_update_view, glucose_delete_view


app_name="glucoses"
urlpatterns = [
    path('', glucose_list_view, name="list"),
    path('<int:pk>/', glucose_detail_view, name='detail'),
    path("add/", glucose_create_view, name='add'),
    path("<int:pk>/update/", glucose_update_view, name='update'),
    path("<int:pk>/delete/", glucose_delete_view, name='delete'),
]
