# ./routers.py

from rest_framework import routers

from accounts.viewsets import AccountViewSet
from documents.viewsets import DocumentViewSet
from organizations.viewsets import OrganizationViewSet

router = routers.SimpleRouter()

router.register(r"account", AccountViewSet, basename="accounts")
router.register(r"organization", OrganizationViewSet, basename="organizations")
router.register(r"document", DocumentViewSet, basename="documents")

urlpatterns = router.urls
