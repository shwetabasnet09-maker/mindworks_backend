from rest_framework.viewsets import ModelViewSet
from .models import  Product,Service
from .serializer import ProductSerializer, ServiceSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    lookup_field = "slug"

