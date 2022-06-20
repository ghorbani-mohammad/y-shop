from rest_framework.routers import DefaultRouter

from .views import ProductViewset

router = DefaultRouter()
router.register('product', ProductViewset, basename='product')

urlpatterns = []

urlpatterns += router.urls
