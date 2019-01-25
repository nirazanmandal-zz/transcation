from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CustomerForm
from .models import Customer


# from item.views import create


# Create your views here.
def create(request):
    form = CustomerForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("customer:list")
    context['form'] = form
    return render(request, 'customer/create.html', context)


def update(request, pk):
    context = {}
    try:
        data = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        messages.error(request, "Object Not Found")
        return redirect("customer:list")

    form = CustomerForm(instance=data)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("customer:list")

    context['form'] = form
    return render(request, 'customer/create.html', context)


def delete(request, pk):
    context = {}
    choice = request.GET.get('choice')
    context['status'] = choice

    if request.method == "POST":
        try:
            data = Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            messages.error(request, "Customer not found")
            return redirect("customer:list")

        if choice == "undo":
            data.is_deleted = False
            data.save()
            messages.success(request, 'Undo successfully.')

        elif choice == "Trash":
            data.is_deleted = True
            data.save()
            messages.success(request, 'Trashed successfully.')

        elif choice == "delete" and data.is_deleted is True:
            data.delete()
            messages.success(request, 'Deleted successfully.')

        return redirect("customer:list")

    context['url'] = reverse("customer:list")
    return render(request, 'snippest/delete.html', context)


def list(request):
    context = {}
    data = Customer.objects.all()

    per_page = 2
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context['data'] = data
    return render(request, 'customer/list.html', context)


def trash_list(request):
    context = {}
    data = Customer.objects.filter(is_deleted=True)

    per_page = 2
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context['data'] = data
    return render(request, 'customer/list.html', context)
