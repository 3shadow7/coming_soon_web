from django.shortcuts import render, redirect
from .forms import SubscriberForm , ContactForm
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def home(request):
    form = None
    form1 = None
    if request.method == "POST":
        print(request.POST)
        if "name" in request.POST :
            form1 = ContactForm(request.POST)
            if form1.is_valid():
                form1.save()
                return redirect(request.path_info + '?success1=true')
        else:
            form = SubscriberForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path_info + '?success=true')
    else:
        form = SubscriberForm()
        form1 = ContactForm()

    if form is None:
        form = SubscriberForm()

    return render(request, 'blog/index.html', {'title': '', 'form': form, 'form1': form1})