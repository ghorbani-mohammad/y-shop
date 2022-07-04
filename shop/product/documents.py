from django_elasticsearch_dsl import Document, Index

from .models import Product

product_index = Index("product")
product_index.settings(
    number_of_shards=1,
    number_of_replicas=0,
)


@product_index.doc_type
class ProductDocument(Document):
    class Django:
        model = Product
        fields = ["id", "name", "price"]
