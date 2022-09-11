from rest_framework import generics
from .serializer import SpiceSerializer
from .models import Spice
from .permissions import IsOwnerOrReadOnly


class SpiceList(generics.ListCreateAPIView):
    queryset = Spice.objects.all()
    serializer_class = SpiceSerializer


class SpiceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Spice.objects.all()
    serializer_class = SpiceSerializer
