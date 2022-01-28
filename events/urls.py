from django.urls import path
from . import views


app_name = "events"

urlpatterns = [
    path("hello", views.hello_world, name="hello_world"),
    # http://127.0.0.1:800/events/categories

    path("categories", views.list_categories, name="list_categories"),

    path("category/add", views.category_add, name="category_add"),
    path("category/<slug:slug>", views.category_detail, name="category_detail"),

    path("", views.EventListView.as_view(), name="list_events"),

    # http://127.0.0.1:8000/events/event/<slug-name>
    path("event/<slug:slug>", views.EventDetailView.as_view(), name="event_detail"),

    # http://127.0.0.1:8000/events/event/create/3
    path("event/create/<int:category_id>",
         views.EventCreateView.as_view(),
         name="event_create"),

    # http://127.0.0.1:8000/events/event/update/42
    path("event/update/<int:pk>",
         views.EventUpdateView.as_view(),
         name="event_update"),

    path("event/delete/<int:pk>",
         views.EventDeleteView.as_view(),
         name="event_delete")


]
