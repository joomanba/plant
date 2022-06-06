from django.shortcuts import render, get_object_or_404
from .models import Plant


def plant_list(request):
    plants = Plant.objects.order_by('이름')
    return render(request, 'plant/plant_list.html', {'plants': plants})


def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'plant/plant_detail.html', {'plant': plant})
