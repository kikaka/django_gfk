from django.contrib.auth.models import Group
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views import generic


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        """ gibt http response zurück """

        # http response objekt holen
        response = super(SignUpView, self).form_valid(form)

        # Gruppe aus Group selektieren
        user_group = Group.objects.get(name='Moderator')

        # user die gruppe zuornden
        self.object.groups.add(user_group)

        # dann erst http response objekt zurückgeben
        return response
