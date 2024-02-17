from .views import DataAnalyzer
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', DataAnalyzer, basename='data')
urlpatterns = router.urls
