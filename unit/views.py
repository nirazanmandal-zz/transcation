from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .forms import UnitCreateForm
from .models import Unit


# Create your views here.
def create(request):
    form = UnitCreateForm(request.POST or None)
    context = {}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("units:list")

    context['form'] = form
    return render(request, 'unit/create.html', context)


def update(request, pk):
    context = {}
    try:
        data = Unit.objects.get(id=pk)
    except Unit.DoesNotExist:
        messages.error(request, "Object not found.")
        return redirect("units:list")

    form = UnitCreateForm(instance=data)
    if request.method == "POST":
        form = UnitCreateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("units:list")

    context['form'] = form
    return render(request, 'unit/create.html', context)


def list(request):
    context = {}
    data = Unit.objects.all()

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
    return render(request, 'unit/list.html', context)


# def detail(request, pk):
#     context = {}
#     try:
#         data = Unit.objects.get(id=pk)
#     except Unit.DoesNotExist:
#         messages.error(request, "Details not found")
#         return redirect("units:create")
#
#     context['data'] = data
#     return render(request, 'unit/detail.html', context)


def delete(request, pk):
    try:
        data = Unit.objects.get(id=pk)
    except Unit.DoesNotExist:
        messages.error(request, "Data not found")
        return redirect("units:list")
    data.delete()
    messages.success(request, 'Deleted successfully.')
    return redirect("units:list")
