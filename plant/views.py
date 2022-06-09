from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Plant


def plant_list(request):
    plants = Plant.objects.order_by('이름')
    return render(request, 'plant/plant_list.html', {'plants': plants})


def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'plant/plant_detail.html', {'plant': plant})


def plant_search(request):
    search_keyword = request.GET.get('q', '')
    plants = Plant.objects.order_by('이름')
    if search_keyword:
        if len(search_keyword) > 1:
            search_plants = plants.filter(이름__icontains=search_keyword)

    return render(request, 'plant/plant_list.html', {'plants': search_plants})
