from django.shortcuts import render
from django.contrib import messages

from things.forms import ThingForm

def home(request):
    form = ThingForm()
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submission was successful.')
        else:
            messages.error(request, 'Invalid submission!')
            messages.error(request, form.errors)
    return render(request, 'home.html', {'form': form})
