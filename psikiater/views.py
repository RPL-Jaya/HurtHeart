from django.shortcuts import render
from .models import Psikiater
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.


# Profile View
def psikiater_detail(request, username):
    # Get psikiater by id
    psikiater = Psikiater.objects.get(username=username)
    context = {'psikiater': psikiater}
    return render(request, 'profile.html', context)

def psikiater_detail_api(request, username):
    # Get psikiater by id
    psikiater = Psikiater.objects.get(username=username)
    context = {'psikiater': model_to_dict(psikiater)}
    # Return psikiater detail in JSON format
    return JsonResponse(context)
