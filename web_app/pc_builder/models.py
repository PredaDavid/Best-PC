from django.db import models

# Create your models here.

# Intel, AMD, Nvidia
class ComponentManufacturer(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# asus, gigabyte, msi, asrock, evga
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# 1151, 1200, AM4, AM5
class ProcessorSocket(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(ComponentManufacturer, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class ProcessorGeneration(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(ComponentManufacturer, on_delete=models.SET_NULL, null=True)
    socket = models.ForeignKey(ProcessorSocket, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Processor(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(ComponentManufacturer, on_delete=models.SET_NULL, null=True)    
    generation = models.ForeignKey(ProcessorGeneration, on_delete=models.SET_NULL, null=True)
    
    cores = models.IntegerField()
    # threads = models.IntegerField()
    # base_clock = models.FloatField()
    # boost_clock = models.FloatField()
    # tdp = models.IntegerField()
    # integrated_graphics = models.BooleanField()
    
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg', null=True)
    
    def __str__(self):
        return self.name
    
class Motherboard(models.Model):
    name = models.CharField(max_length=100)
    
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    socket = models.ForeignKey(ProcessorSocket, on_delete=models.SET_NULL, null=True)
    # form_factor = models.CharField(max_length=100)
    
    ram_slots = models.IntegerField()
    # max_ram = models.IntegerField()
    # ram_speed = models.IntegerField()
    
    # pcie_slots = models.IntegerField()
    # m2_slots = models.IntegerField()
    
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg', null=True)
    
    def __str__(self):
        return self.name