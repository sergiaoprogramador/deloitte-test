from cronos.views import FileViewSet, MemberViewSet, PostViewSet, ServiceViewSet
from rest_framework import routers

app_name = "cronos"

router = routers.DefaultRouter()
router.register(r"files", FileViewSet, basename="files")
router.register(r"members", MemberViewSet, basename="members")
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"services", ServiceViewSet, basename="services")

urlpatterns = router.urls
