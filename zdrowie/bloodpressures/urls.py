from django.urls import path
from .views import bloodpressure_list_view, bloodpressure_detail_view, bloodpressure_create_view, bloodpressure_update_view, bloodpressure_delete_view


app_name = "bloodpressures"
urlpatterns = [
    path('', view=bloodpressure_list_view, name="list"),
    path("<int:pk>/", bloodpressure_detail_view, name="detail"),
    path("add/", bloodpressure_create_view, name="add"),
    path("<int:pk>/update/", bloodpressure_update_view, name="update"),
    path("<int:pk>/delete/", bloodpressure_delete_view, name="delete"),
]
