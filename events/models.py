from pyexpat import model
from tabnanny import verbose
from unicodedata import name
from wsgiref import validate
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator
from .validators import datetime_future


User = get_user_model()

# Create your models here.


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DateMixin):
    name = models.CharField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(
        null=True, blank=True, help_text="Die Beschreibung der Kategorie")
    slug = models.SlugField(unique=True)  # example.com/categories/abend-sport

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("events:category_detail", kwargs={"slug": self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Category._meta.fields]

    # def clean(self):
    #     print("Clean Model")
    #     return super().clean()

    def __str__(self):
        return self.name


class Event(DateMixin):

    class Group(models.IntegerChoices):
        BIG = 20
        MEDIUM = 10
        SMALL = 5
        MIN = 1

    class Meta:
        ordering = ["name"]
        permissions = (("can_say_hello", "Set event active"),)

    name = models.CharField(max_length=150, unique=True,
                            validators=[MinLengthValidator(3)])

    description = models.TextField(blank=True, null=True)
    #date = models.DateTimeField(validators=[datetime_future])
    date = models.DateTimeField()
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    min_group = models.IntegerField(choices=Group.choices)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="events")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events")
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"slug": self.slug})

    def related_events(self):
        related_events = Event.objects.filter(
            min_group=self.min_group,
            category=self.category
        )
        return related_events.exclude(pk=self.id)

    def clean(self):
        # if self.sub_title != "egal":
        if self.category.name != "Sport":
            datetime_future(self.date)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
