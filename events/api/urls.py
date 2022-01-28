from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("category", views.CategoryViewset)
router.register("event", views.EventViewset)
