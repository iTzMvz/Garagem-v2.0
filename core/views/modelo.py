from rest_framework.viewsets import ModelViewSet

from .modelo import Modelo
from .modelo import ModeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer