from rest_framework import viewsets
from .models import Team, Sport, Product, Customer
from .serializers import TeamSerializer, SportSerializer, ProductSerializer, CustomerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all().order_by('name')
    serializer_class = SportSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer
