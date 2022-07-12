import base64
from django.test import Client
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        image = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
        )
        img = SimpleUploadedFile("image.png", image, content_type="image/png")
        self.creation_resp = self.client.post(
            "/product/", {"name": "product-01", "price": "500", "image": img}
        )

    def test_product_creation(self):
        self.assertEqual(self.creation_resp.status_code, 201)

    def test_product_list(self):
        response = self.client.get("/product/")
        self.assertEqual(len(response.json()), 1)

    def test_product_update(self):
        obj = self.creation_resp.json()
        response = self.client.patch(
            f'/product/{obj["id"]}/',
            data={"name": "product-01 updated"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_product_delete(self):
        obj = self.creation_resp.json()
        response = self.client.delete(f'/product/{obj["id"]}/')
        self.assertEqual(response.status_code, 204)
