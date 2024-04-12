from django.contrib import admin

from .models import ComponentManufacturer, Brand, ProcessorSocket, ProcessorGeneration, Processor, Motherboard

admin.site.register(ComponentManufacturer)
admin.site.register(Brand)
admin.site.register(ProcessorSocket)
admin.site.register(ProcessorGeneration)
admin.site.register(Processor)
admin.site.register(Motherboard)
