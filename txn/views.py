from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transactions
from .models import Customer


# Create your views here.
def index(request):
    form = TransactionForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction Saved.')
            return redirect('txn:index')

    context['form'] = form
    return render(request, 'txn/index.html', context)


def list(request):
    context = {}
    data = Transactions.objects.all()

    per_page = 5
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context['data'] = data
    return render(request, 'txn/list.html', context)


def paid(request, pk):
    context = {}
    data = Transactions.objects.filter(id=pk).first()
    if request.method == 'POST':
        data.cname = Customer.objects.get(cname__iexact='cash')
        data.save()
        return redirect('txn:list')

    context['cname'] = data
    return render(request, 'snippest/paid.html', context)
