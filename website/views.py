from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404


from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.template import RequestContext
from website.forms import ContactForm

from django.core.mail import send_mail 
from django.conf import settings 

from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User 
import string

from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
# # from django.views.generic import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView

# from website.forms import UserSignUp, UserLogin

from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError


def hairstyleList(request):
    context = {}
    #i = get_object_or_404(Hairstyle, pk=1)
    print 'HI'
    hair_pics = Hairstyle.objects.all()

    context['hair_pics'] = hair_pics

    return render_to_response('hairstyle_list.html', context, context_instance=RequestContext(request))

# base view will be adapted into this view later (12/01/2015)
# #def main_page(request):
#     context = {}

#     return render_to_response('main_page.html', context, context_instance=RequestContext(request))


def navbar(request):
    context = {}

    return render_to_response('navbar.html', context, context_instance=RequestContext(request))


def services(request):
    context = {}

    return render_to_response('services.html', context, context_instance=RequestContext(request))


def young_pics(request):
    context = {}

    return render_to_response('young_pics.html', context, context_instance=RequestContext(request))


def stylish_seniors(request):
    context = {}

    return render_to_response('stylish_seniors.html', context, context_instance=RequestContext(request))


def updo(request):
    context = {}

    return render_to_response('updo.html', context, context_instance=RequestContext(request))


def message(request):
    context = {}

    return render_to_response('message.html', context, context_instance=RequestContext(request))


def account_activation(request):
    context = {}

    return render_to_response('account_activation.html', context, context_instance=RequestContext(request))


def base(request):
    context = {}

    return render_to_response('base.html', context, context_instance=RequestContext(request))

# Form / Contact Views, Permissions


@login_required
def contact_view(request):
    context = {}

    form = ContactForm()

    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        context['form'] = form
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(' WEBSITE MESSAGE FROM %s' % name,
                      'Message from %s, %s, %s' % (name, email, phone) + '\n\n' + message,
                      email,
                      [settings.EMAIL_HOST_USER],
                      fail_silently=False
                      )
            
            messages.success(request, 'Message has been sent!')
            return HttpResponseRedirect('/message')
        else:
            context['message'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form
       
    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))


def handler404(request):
    response = render_to_response('404.html', context, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', context, context_instance=RequestContext(request))
    response.status_code = 500
    return response
