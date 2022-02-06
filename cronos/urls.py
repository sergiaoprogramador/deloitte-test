from django.urls import path
from cronos.views import file_view
from cronos.views import service_view


urlpatterns = [
    path("files/", file_view.FileList.as_view()),
    path("files/<uuid:pk>/", file_view.FileDetail.as_view()),
    path("services/", service_view.ServiceList.as_view()),
    path("services/<uuid:pk>/", service_view.ServiceDetail.as_view()),
]
