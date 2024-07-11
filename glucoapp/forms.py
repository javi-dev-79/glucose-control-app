# glucoapp/forms.py

from django import forms
from .models import GlucoseReading
from crispy_forms.helper import FormHelper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nombre:",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "mb-4 p-2 border border-gray-300 rounded w-full"}
        ),
        required=True,
    )
    password = forms.CharField(
        label="Contraseña:",
        widget=forms.PasswordInput(
            attrs={"class": "mb-4 p-2 border border-gray-300 rounded w-full"}
        ),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("username", placeholder="Introduzca su nombre"),
            Field("password", placeholder="Introduzca su contraseña"),
            Submit(
                "submit",
                "Acceder",
                css_class="bg-petroleum text-white mt-4 px-4 py-2 rounded hover:bg-bright_red",
            ),
        )
        self.helper.form_class = (
            "bg-light_salmon p-8 rounded-sm shadow lg:w-1/2 xl:w-2/5 w-full"
        )
        self.helper.label_class = "block text-2xl text-slate-800 pb-2"


class GlucoseReadingForm(forms.ModelForm):
    class Meta:
        model = GlucoseReading
        fields = ["date", "level", "notes"]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Reading"))
