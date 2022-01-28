from email import message
import logging
from pyexpat import model
from django.forms import ValidationError
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Event, Category
from .forms import CategoryForm, EventForm, EventUpdateForm

logger = logging.getLogger("event_manager.events")

# Create your views here.


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events:list_events')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user != self.get_object().author:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventUpdateForm
    success_message = "Das Ändern des Events war erfolgreich."

    def form_valid(self, form):
        logger.debug("Es wurde ein Event upgedated")
        if form.instance.author != self.request.user:
            messages.info(self.request, "Hallo, das ist eine Testmessage!")
            raise ValidationError("Das ist nicht möglich")
        return super(EventUpdateView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user != self.get_object().author:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    success_message = "Das Anlegen des Events war erfolgreich."

    def form_valid(self, form):
        """ Das wird vor dem Speichern in der DB aufgerufen"""
        form.instance.author = self.request.user
        form.instance.category = self.category
        return super(EventCreateView, self).form_valid(form)

    def get_initial(self):
        """ Das wird zuerst aufgerufen"""
        print("Request: ", self.request.__dict__)
        self.category = get_object_or_404(
            Category, pk=self.kwargs["category_id"]
        )


class EventDetailView(DetailView):
    model = Event
    # template_name = "events/event_detail.html"
    # event_detail.html
    # context name object


class EventListView(ListView):
    """http://127.0.0.1/events"""
    model = Event
    paginate_by = 6
    context_object_name = "events"

    def get_queryset(self):
        # Das würde im default passieren: queryset = Event.objects.all()
        queryset = Event.objects.select_related("category").all()
        if self.request.GET.get("category"):
            slug = self.request.GET.get("category")
            queryset = queryset.filter(category__slug=slug)
        return queryset


@permission_required("events.can_say_hello")
def hello_world(request):
    print(request.user)
    # print("REQUEST object", type(request), request.__dict__, request.user)
    return HttpResponse("Hallo Welt")


def list_categories(request):
    categories = Category.objects.all()
    return render(request,
                  "events/category_list.html",
                  {"categories": categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    # category = Category.objects.get(slug=slug)
    return render(request,
                  "events/category_detail.html",
                  {"category": category})


def category_add(request):
    """http://127.0.0.1:8000/events/category/add"""
    if request.method == "POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            category = form.save(commit=False)
            category = form.save()
            # return redirect("events:list_categories")
            return redirect(category.get_absolute_url())
        else:
            print("Formular-Fehler: ", form.errors)
    else:
        form = CategoryForm()

    return render(request, "events/category_add.html", {"form": form})
