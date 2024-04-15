from django.db import models
from django.conf.global_settings import STATICFILES_DIRS
from django.contrib.auth.models import User

# Create your models here.



def get_upload_path(type):
    return 'static/images/' + type + '/'


COMPONENT_TYPE = {
    'cpu': 'Processor',
    'mobo': 'Motherboard',
    'gpu': 'GPU',
    'ram': 'RAM',
    'storage': 'Storage',
    'psu': 'PowerSupply',
    'case': 'Case',
}

MANUFACTURER = {
    'intel': 'Intel',
    'amd': 'AMD',
    'nvidia': 'Nvidia'
}

# asus, gigabyte, msi, asrock, evga
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# 1151, 1200, AM4, AM5
class ProcessorSocket(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class ComputerComponent(models.Model):
    name = models.CharField(max_length=200)
    
    type = ""
    
    manufacturer = models.CharField(max_length=6,choices=MANUFACTURER, null=True)
    
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    
    msrp_price = models.FloatField()
    image = models.ImageField(upload_to=get_upload_path('components'), default='default.jpg', null=True)
    
    def __str__(self):
        return self.name[:100]
    
    class Meta:
        abstract = True

class Processor(ComputerComponent):
    type = COMPONENT_TYPE['cpu']
    
    socket = models.ForeignKey(ProcessorSocket, on_delete=models.SET_NULL, null=True)
    
    cores = models.IntegerField()
    # threads = models.IntegerField()
    # base_clock = models.FloatField()
    # boost_clock = models.FloatField()
    # tdp = models.IntegerField()
    # integrated_graphics = models.BooleanField()
    
class Motherboard(ComputerComponent):
    type = COMPONENT_TYPE['mobo']
    
    socket = models.ForeignKey(ProcessorSocket, on_delete=models.SET_NULL, null=True)
    # form_factor = models.CharField(max_length=100)
    
    ram_slots = models.IntegerField()
    # max_ram = models.IntegerField()
    # ram_speed = models.IntegerField()
    
    # m2_slots = models.IntegerField()
    
class GPU(ComputerComponent):
    type = COMPONENT_TYPE['gpu']
    
    vram = models.IntegerField()
    base_clock = models.FloatField()
    # boost_clock = models.FloatField()
    tdp = models.IntegerField()
    
    
class RAM(ComputerComponent):
    type = COMPONENT_TYPE['ram']
    
    capacity = models.IntegerField()
    module_count = models.IntegerField()
    
    speed = models.IntegerField()
    # cas_latency = models.IntegerField()
    # ecc = models.BooleanField()
    
    
class Storage(models.Model):
    type = COMPONENT_TYPE['storage']
    
    capacity = models.IntegerField()
    # form_factor = models.CharField(max_length=100)
    # interface = models.CharField(max_length=100)
    
class PowerSupply(models.Model):
    type = COMPONENT_TYPE['psu']
    
    wattage = models.IntegerField()
    # efficiency = models.CharField(max_length=100)
    # modular = models.BooleanField()
    
class Case(models.Model):
    type = COMPONENT_TYPE['case']

    # form_factor = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)
    
    
class Configuration(models.Model):
    name = models.CharField(max_length=300) # 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    active_user_configuration = models.BooleanField(default=False)
    
    cpu = models.ForeignKey(Processor, on_delete=models.SET_NULL, null=True)
    mobo = models.ForeignKey(Motherboard, on_delete=models.SET_NULL, null=True)
    gpu = models.ForeignKey(GPU, on_delete=models.SET_NULL, null=True)
    ram = models.ManyToManyField(RAM)
    storage = models.ManyToManyField(Storage)
    psu = models.ForeignKey(PowerSupply, on_delete=models.SET_NULL, null=True)
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
