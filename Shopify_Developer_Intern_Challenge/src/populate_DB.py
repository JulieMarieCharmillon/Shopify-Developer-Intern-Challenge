from BackLog.models import Warehouse, Products

WS = ["wh-1", "wh-2", "wh-3", "wh-4"]

for w in WS:
    Warehouse.objects.create(name=w, location=f"{w}-location", capacity=2000)

PDTS = [
    ["pdt-1", 50, "Description of pdt-1", Warehouse.objects.get(pk=1)],
    ["pdt-2", 150, "Description of pdt-2", Warehouse.objects.get(pk=1)],
    ["pdt-3", 20, "Description of pdt-3", Warehouse.objects.get(pk=2)],
    ["pdt-4", 200, "Description of pdt-4", Warehouse.objects.get(pk=3)],
    ["pdt-5", 75, "Description of pdt-5", Warehouse.objects.get(pk=4)],
]

for pdt in PDTS:
    Products.objects.create(name=pdt[0], quantity=pdt[1], description=pdt[2], warehouse=pdt[3])

