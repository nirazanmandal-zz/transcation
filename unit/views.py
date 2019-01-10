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
            return redirect("units:lists")

    context['form'] = form
    return render(request, 'unit/create.html', context)


def lists(request):
    pass


def detail(request, pk):
    context = {}
    try:
        data = Unit.objects.get(id=pk)
    except Unit.DoesNotExist:
        return redirect("units:lists")

    context['data'] = data
    return render(request, 'unit/detail.html', context)
