from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils import timezone

from expirations.models import Expiration, Food
from .forms import ExpirationForm

def expirations(request):
    if request.method == 'POST':
        form = ExpirationForm(request.POST)
        if form.is_valid():
            upc = form.cleaned_data['upc']
            expiration_date = form.cleaned_data['expiration_date']
            Food.objects.get_or_create(upc=upc)
            Expiration.objects.create(upc=Food.objects.get(upc=upc), expiration_date=expiration_date)
            return redirect('expirations')
    else:
        form = ExpirationForm()

    expirations = Expiration.objects.all()

    data = {
        'expirations': expirations,
        'today': timezone.now().date(),
        'cvp': timezone.now().date() + timedelta(days=3),
        'form': form,
    }

    return render(request, 'expirations/expirations.html', data)