from django.shortcuts import redirect, render

from BackLog.models import Products, Warehouse
from SHOP.forms import ProductsForm, WarehouseForm

def index(request):
    return render(request, "backlog/index.html")


## Products

def products(request):
    PRODUCTS = Products.objects.all()
    
    if request.method == "POST":
        
        PRODUCT_FORM = ProductsForm(request.POST)
        if PRODUCT_FORM.is_valid():
            PRODUCT_FORM.save()
    else:
        PRODUCT_FORM = ProductsForm()

    return render(request, "backlog/Products.html", context={
        "products":PRODUCTS, 
        "productForm":PRODUCT_FORM,
        })

def deleteProduct(request, id):
    pdt = Products.objects.get(id=id)
    pdt.delete()
    return redirect('products')

def updateProduct(request, id):
    pdt = Products.objects.get(id=id)
    pdt_form = ProductsForm(instance=pdt)

    if request.method == "POST":
        
        PRODUCT_FORM = ProductsForm(request.POST, instance=pdt)
        if PRODUCT_FORM.is_valid():
            PRODUCT_FORM.save()
            return redirect('products')
    else:
        PRODUCT_FORM = ProductsForm()
  
    return render(request, 'backlog/updateProduct.html', context = {"productForm":pdt_form})

## Warehouses 

def warehouses(request):

    WAREHOUSES = Warehouse.objects.all()
    

    def capacity_left():
        left = 0
        capacity_left_list=[]
        for w in WAREHOUSES:
            left = w.capacity
            for pt in w.products_set.all():
                left -= pt.quantity
            capacity_left_list.append(left)
        return capacity_left_list

    CAPACITY_LEFT = capacity_left()

    if request.method == "POST":
        
        WAREHOUSE_FORM = WarehouseForm(request.POST)
        if WAREHOUSE_FORM.is_valid():
            WAREHOUSE_FORM.save()
    else:
        WAREHOUSE_FORM = WarehouseForm()

    return render(request, "backlog/warehouses.html", context={
        "warehouseData":zip(WAREHOUSES, CAPACITY_LEFT),
        "warehouseForm":WAREHOUSE_FORM,
        })

def deleteWarehouse(request, id):
    w = Warehouse.objects.get(id=id)
    w.delete()
    return redirect('warehouses')

def updateWarehouse(request, id):
    w = Warehouse.objects.get(id=id)
    warehouse_form = WarehouseForm(instance=w)
    
    if request.method == "POST":
        
        WAREHOUSE_FORM = WarehouseForm(request.POST, instance=w)
        if WAREHOUSE_FORM.is_valid():
            WAREHOUSE_FORM.save()
            return redirect('warehouses')
    else:
        WAREHOUSE_FORM = WarehouseForm()

    return render(request, 'backlog/updateWarehouse.html', context = {"warehouseForm":warehouse_form})
