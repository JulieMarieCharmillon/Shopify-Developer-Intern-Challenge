"""SHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from BackLog.views import deleteProduct, deleteWarehouse, index, products, updateProduct, updateWarehouse, warehouses

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('delete-product/<int:id>', deleteProduct, name="delete-product"), 
    path('update-product/<int:id>', updateProduct, name="update-product"),
    path('warehouses/', warehouses, name="warehouses"),
    path('delete-warehouse/<int:id>', deleteWarehouse, name="delete-warehouse"),
    path('update-warehouse/<int:id>', updateWarehouse, name="update-warehouse"),
    
]
