from django import forms
from django.core.exceptions import ValidationError
from .models import Category, Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = "slug", "author", "category"
        widgets = {
            "date": forms.DateTimeInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
        }


class EventUpdateForm(EventForm):
    class Meta(EventForm.Meta):
        exclude = "slug", "author"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = "__all__"
        exclude = "slug",

        labels = {
            "sub_title": "Slogan"
        }

    message = forms.CharField(max_length=5)

    def clean_message(self):
        """clean_<feldname>"""
        print("Clean message")
        message = self.cleaned_data["message"]
        if isinstance(message, str) and message.startswith(("@", "?")):
            raise ValidationError("Diese Zeichen sind nicht legal")

        return message

    # def clean(self):
    #     """ Methode zum Vergleich zweier Formularfelder miteinander"""
    #     print("Form clean")
