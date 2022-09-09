from rest_framework import generics
from .serializer import SpiceSerializer
from .models import Spice


class SpiceList(generics.ListAPIView):
    queryset = Spice.objects.all()
    serializer_class = SpiceSerializer


class SpiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spice.objects.all()
    serializer_class = SpiceSerializer
