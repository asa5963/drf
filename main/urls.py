from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'post', views.PostViewsSet, basename='posts')

urlpatterns = router.urlsc