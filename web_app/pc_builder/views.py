from django.shortcuts import render, redirect
from .models import Processor, GPU, Motherboard, RAM, Storage, PowerSupply, Case, Configuration, ComputerComponent, CpuCooler

from django.http import HttpResponse
# Create your views here.

def configure_pc(request):
    # if the user is not logged in, redirect them to the login page
    if not request.user.is_authenticated:
        return redirect('login')        
    
    # try and get the active configuration
    current_configuration = Configuration.objects.filter(user=request.user, active_user_configuration=True).first()
    if not current_configuration:
        current_configuration = Configuration.objects.create(name="New Configuration", user=request.user,active_user_configuration=True)

    context = {
        'configuration': current_configuration,
    }

    return render(request, "pc_builder/configure_pc.html", context)

TYPE_CLASS_RELATION = {
    'cpu': Processor,
    'mobo': Motherboard,
    'gpu': GPU,
    'ram': RAM,
    'storage': Storage,
    'psu': PowerSupply,
    'case': Case,
    'cpu_cooler': CpuCooler,
}

def choose_part(request, type):
    
    current_configuration = Configuration.objects.filter(user=request.user, active_user_configuration=True).first()
    parts = TYPE_CLASS_RELATION[type].objects.all()


    if type == 'mobo':
        if current_configuration.cpu:
            parts = parts.filter(socket=current_configuration.cpu.socket)
    
    context = {
        'configuration': current_configuration,
        'parts': parts,
        'type': type,
    }
    return render(request, "pc_builder/choose_part.html", context)

def add_part(request, type, id):
    
    current_configuration = Configuration.objects.filter(user=request.user, active_user_configuration=True).first()
    part = TYPE_CLASS_RELATION[type].objects.get(id=id)
    
    if type == 'ram':
        current_configuration.ram.add(part)
    elif type == 'storage':
        current_configuration.storage.add(part)
    else:
        setattr(current_configuration, type, part)
    
    current_configuration.calculate_msrp_price()
    current_configuration.save()
    
    return redirect('configure-pc')

def remove_part(request, type):
    current_configuration = Configuration.objects.filter(user=request.user, active_user_configuration=True).first()
    
    if type == 'ram':
        current_configuration.ram.clear()
    elif type == 'storage':
        current_configuration.storage.clear()
    else:
        setattr(current_configuration, type, None)
        
    current_configuration.save()
    
    return redirect('configure-pc')

