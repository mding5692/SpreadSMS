from django import forms
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from tracker.models import Object, Person, Contact
from tracker.serializers import ObjectSerializer, PersonSerializer

import datetime


class AllEntities(APIView):
    """
    Handles adding entity locations.
    Handles retrieving entity locations.
    """
    def get(self, request, format=None):
        entity = Object.objects.all()
        serializer = ObjectSerializer(entity, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EntityRange(APIView):
    """
    Handle retrieving entity locations in a given datetime range.
    """
    def get_object(self, start, end):
        try:
            start_date = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
            end_date = datetime.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")
            return Object.objects.filter(date__range=(start_date, end_date))
        except Object.DoesNotExist:
            raise Http404

    def get(self, request, start, end, format=None):
        entities = self.get_object(start, end)
        serializer = ObjectSerializer(entities, many=True)
        print(serializer.data)
        return Response(serializer.data)


class RegistrationApi(APIView):
    """
    Handle retrieving and adding registered users.
    """
    def get(self, request, format=None):
        entity = Person.objects.all()
        serializer = PersonSerializer(entity, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationForm(forms.Form):
    """
    HTML Form to be displayed when adding a new registered user.
    """
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)
    number = forms.CharField(label='Number', max_length=30)


def register_view(request):
    """
    Handles viewing of the registration form.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            person = Person(first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            number=form.cleaned_data['number'])
            person.save()
            return HttpResponseRedirect('/tracker/')
        return HttpResponseRedirect('/tracker/')
    else:
        form = RegistrationForm()
        return render(request, 'tracker/register.html', {'form': form})


def proximity_view(request):
    """
    Display button for detecting collisions between registered entities
    """
    return render(request, 'tracker/proximity.html')

from twilio.rest import TwilioRestClient
def process_proximity(request, text, format=None):
    account_sid = "AC8de5647be33d99d308304fa8e883b576"
    auth_token = "4c4d9a787a1cb511f0e84a9c43863466"
    my_twilio_number = "+12897685697"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+19058695733", from_=my_twilio_number, body=text)
    return HttpResponseRedirect('/tracker/')


def homepage(request):
    """
    Homepage redirect frorgot why
    """
    entity = Object.objects.all()
    serializer = ObjectSerializer(entity, many=True)
    entities = serializer.data
    return render(request, 'tracker/index.html', {'entities': entities})

