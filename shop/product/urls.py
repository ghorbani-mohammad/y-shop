from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewset, ProductSearch

router = DefaultRouter()
router.register("product", ProductViewset, basename="product")

urlpatterns = [path("product_search/<str:query>/", ProductSearch.as_view())]

urlpatterns += router.urls
