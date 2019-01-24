import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
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


def edit(request, pk):
    context = {}
    try:
        data = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        messages.error(request, 'Data not found')
        return redirect('item:list')
    form = ItemCreateForm(instance=data)
    if request.method == 'POST':
        form = ItemCreateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('item:list')

    context['form'] = form
    return render(request, 'item/create.html', context)


def delete(request, pk):
    context = {}
    choice = request.GET.get('choice')
    context['status'] = choice

    if request.method == "POST":
        try:
            data = Item.objects.get(id=pk)
        except Item.DoesNotExist:
            messages.error(request, "Item not found")
            return redirect("item:list")

        if choice == "undo":
            data.is_deleted = False
            data.save()
        elif choice == "trash":
            data.is_deleted = True
            data.save()
        elif choice == "delete" and data.is_deleted is True:
            data.delete()

        messages.success(request, 'Deleted successfully.')
        return redirect("item:list")

    context['url'] = reverse("item:list")
    return render(request, 'snippest/delete.html', context)


def list(request):
    context = {}
    data = Item.objects.filter(is_deleted=False)
    context['data'] = data
    return render(request, 'item/list.html', context)


def trash_list(request):
    context = {}
    data = Item.objects.filter(is_deleted=True)
    context['data'] = data
    return render(request, 'item/list.html', context)


def item_unit_price(request, pk):
    try:
        data = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return HttpResponse("Unable to find data.", status=400)

    context = {"unit_price": str(data.price)}
    context = json.dumps(context)
    return HttpResponse(context, "application/json", status=200)
