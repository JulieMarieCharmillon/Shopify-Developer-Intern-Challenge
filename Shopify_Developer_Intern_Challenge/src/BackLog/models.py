from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(default=1000)

    def __str__(self) -> str:
        return self.name

    # class Meta:
    #     verbose_name = "Warehouse"


class Products(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=400)
    warehouse = models.ForeignKey(Warehouse,  on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

    # class Meta:
    #     verbose_name = "Product"

    