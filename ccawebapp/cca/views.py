from django.shortcuts import render
from .models import CustomUser
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404,render
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
        	# instance = ModelWithFileField(file_field=request.FILES['file'])
         #    instance.save()
            # file is saved
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def home(request):
    members=CustomUser.objects.all().order_by('-year')
    members=members.exclude(username='admin')
    return render(request, 'home.html', {'members':members})