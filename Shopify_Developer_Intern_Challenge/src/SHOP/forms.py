from django import forms

from BackLog.models import Warehouse, Products

WAREHOUSES = (
    (Warehouse.objects.get(pk=i), Warehouse.objects.get(pk=i)) for i in range(len(Warehouse.objects.all()))
)

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields= "__all__"
        