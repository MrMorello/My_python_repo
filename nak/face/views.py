from django.shortcuts import render
from .forms import OrderForm


def face(request):
    form = OrderForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        form = form.save()
    return render(request, 'face/index.html', locals())
