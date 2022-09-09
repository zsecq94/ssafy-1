from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Travel
from .forms import TravelForm


# Create your views here.

@require_safe
def index(request):
    travels = Travel.objects.all()
    context = {
        'travels': travels,
    }
    return render(request, 'travels/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = TravelForm()
    context = { 
        'form': form,
    }
    return render(request, 'travels/create.html', context)


@require_safe
def detail(request, pk):
    travels = Travel.objects.get(pk=pk)
    context = {
        'travels': travels,
    }
    return render(request, 'travels/detail.html', context)


@require_POST
def delete(request, pk):
    travels = Travel.objects.get(pk=pk)
    travels.delete()
    return redirect('travels:index')

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    travels = Travel.objects.get(pk=pk)
    if request.method == 'POST':
        form = TravelForm(request.POST, instance=travels)
        if form.is_valid():
            form.save()
            return redirect('travels:detail', travels.pk)
    else:
        form = TravelForm(instance=travels)
    context = {
        'travels': travels,
        'form': form,
    }
    return render(request, 'travels/update.html', context)