from django.urls import path
from .views import SpiceList, SpiceDetail

urlpatterns = [
    path('', SpiceList.as_view(), name='spice_list'),
    path('<int:pk>', SpiceDetail.as_view(), name='spice_detail'),
]
