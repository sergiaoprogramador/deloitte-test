from cronos.views import FileViewSet, ServiceViewSet
from rest_framework import routers

app_name = "cronos"

router = routers.DefaultRouter()
router.register(r"files", FileViewSet, basename="files")
router.register(r"services", ServiceViewSet, basename="services")

urlpatterns = router.urls
