from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .models import Product
from .documents import ProductDocument


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "image", "thumbnail")


class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument
        fields = ("id", "name", "price", "image", "thumbnail")
