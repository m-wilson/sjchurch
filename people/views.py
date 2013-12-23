from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from .models import Individual
from django.contrib.sites.models import Site, RequestSite
from django.contrib.syndication.views import add_domain
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


class IndividualDetailView(DetailView):
    model = Individual
    
def individualDetailView(request, individual_slug):
    individual=Individual.objects.filter(slug= individual_slug)
    individual= individual[0]
    individualItemDict= {'slug':individual_slug, 'individual': individual,}
    return render_to_response('individual/individual_detail.html',individualItemDict, context_instance=RequestContext(request))