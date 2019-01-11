from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemCreateForm


def create(request):
    form = ItemCreateForm(request.POST or None)
    context = {}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("item:list")
    context['form'] = form
    return render(request, 'item/create.html', context)


def list(request):
    context = {}
    data = Item.objects.all()
    context['data'] = data
    return render(request, 'item/list.html', context)

