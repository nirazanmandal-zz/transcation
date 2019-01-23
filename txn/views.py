from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transactions


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
    context['data'] = data
    return render(request, 'txn/list.html', context)
