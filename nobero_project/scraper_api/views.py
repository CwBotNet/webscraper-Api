from rest_framework.views import APIView
from rest_framework.response import Response
from .db_connection import MongoDB


# Create your views here.
class ProductListView(APIView):
    def get(self, request):
        db = MongoDB("nobero_products")
        collection = db.get_collection("products")
        products = list(collection.find())
        for product in products:
            product["_id"] = str(product["_id"])
        return Response(products)
    
