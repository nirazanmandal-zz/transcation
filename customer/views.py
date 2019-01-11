from django.contrib import messages
from django.shortcuts import render, redirect
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

    context['data'] = data
    return redirect(request, 'customer/create.html', context)


def delete(request, pk):
    try:
        data = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        messages.error(request, "Data not found")
        return redirect("customer:list")
    data.delete()
    messages.success(request, "Deleted Successfully.")
    return redirect("customer:list")


def list(request):
    context = {}
    data = Customer.objects.all()
    context['data'] = data
    return render(request, 'customer/list.html', context)
