from elasticsearch_dsl import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from .models import Product
from .documents import ProductDocument
from .serializers import ProductSerializer, ProductDocumentSerializer


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSearch(APIView):
    serializer_class = ProductSerializer
    document_class = ProductDocument

    def generate_q_expression(self, query):
        return Q("match", name={"query": query, "fuzziness": "auto"})

    def get(self, request, query):
        q = self.generate_q_expression(query)
        search = self.document_class.search().query(q)
        return Response(self.serializer_class(search.to_queryset(), many=True).data)


class ProductDocumentViewSet(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductDocumentSerializer

    filter_backends = (
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    )

    search_fields = ("name",)

    filter_fields = {
        "id": {"field": "id", "lookups": [LOOKUP_QUERY_IN]},
        "price": {"field": "price", "lookups": [LOOKUP_QUERY_GTE, LOOKUP_FILTER_RANGE]},
    }

    suggester_fields = {
        "name_suggest": {"field": "name.suggest", "suggesters": [SUGGESTER_COMPLETION]}
    }
