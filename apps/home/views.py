from multiprocessing import context
from django.shortcuts import render, redirect , HttpResponse
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from decimal import Decimal

from apps.home.models import Roles

from .forms import UserProfileForm, RolesModel


@login_required(login_url="/login/")
def user_create(request):
    
    form = UserProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user.profile, data=request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'home/bid_payment.html',context={'form':form})

def roles_for_adm(request):
    if Roles.objects.first():
        instance = Roles.objects.first()
    else:
        instance = Roles.objects.create(percentage=0)
    form = RolesModel(instance=instance)
    if request.method == 'POST':
        form = RolesModel(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    if request.user.is_staff:
        context = {'form': form}
        return render(request, 'home/roles.html',context)
    else:
        return HttpResponse("You are not allowed here")


@login_required(login_url="/login/")
def index(request):
    if Roles.objects.first():
        instance = Roles.objects.first()
    else:
        instance = Roles.objects.create(percentage=1)
    daily_profit = Decimal((instance.percentage/100)) * request.user.profile.balance
    weekly_profit = daily_profit * 7 
    monthly_profit = daily_profit * 30 #oikik 
    context = {'segment': 'index', 'instance':instance, 'daily_profit': daily_profit,'weekly_profit':weekly_profit, 'monthly_profit':monthly_profit}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
