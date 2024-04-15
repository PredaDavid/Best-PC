from django.shortcuts import render, redirect
from .models import Processor, GPU, Motherboard, RAM, Storage, PowerSupply, Case, Configuration, ComputerComponent

from django.http import HttpResponse
# Create your views here.

def configure_pc(request):
    new_configuration = Configuration.objects.create(name="New Configuration", user=request.user,active_user_configuration=True)
    return render(request, "pc_builder/configure_pc.html")

TYPE_CLASS_RELATION = {
    'cpu': Processor,
    'mobo': Motherboard,
    'gpu': GPU,
    'ram': RAM,
    'storage': Storage,
    'psu': PowerSupply,
    'case': Case,
}

def choose_part(request, type):
    
    current_configuration = Configuration.objects.filter(user=request.user, active_user_configuration=True).first()
    parts = TYPE_CLASS_RELATION[type].objects.all()


    if type == 'mobo':
        if current_configuration.processor:
            parts = parts.filter(socket=current_configuration.processor.socket)
    
    context = {
        'configuration': current_configuration,
        'parts': parts,
        'type': type,
    }
    return render(request, "pc_builder/choose_part.html", context)

def add_part(request, type, id):
    
    current_configuration = Configuration.objects.filter(user=request.user, active_user_configuration=True).first()
    part = TYPE_CLASS_RELATION[type].objects.get(id=id)
    setattr(current_configuration, type, part)
    
    return redirect('configure-pc')