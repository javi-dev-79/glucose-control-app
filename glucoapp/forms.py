# glucoapp/forms.py

from django import forms
from .models import GlucoseReading
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Submit
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(
        label=_("Nombre:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "mb-4 p-2 border border-gray-300 rounded w-full"}
        ),
        required=True,
    )
    password = forms.CharField(
        label=_("Contraseña:"),
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
            Field("username", placeholder=_("Introduzca su nombre")),
            Field("password", placeholder=_("Introduzca su contraseña")),
            Submit(
                "submit",
                _("Acceder"),
                css_class="bg-petroleum text-white mt-4 px-4 py-2 rounded hover:bg-bright_red",
            ),
        )
        self.helper.form_class = (
            "bg-light_salmon p-8 rounded-lg shadow lg:w-1/2 xl:w-2/5 w-full"
        )
        self.helper.label_class = "block text-2xl text-slate-800 pb-2"


class GlucoseReadingForm(forms.ModelForm):
    class Meta:
        model = GlucoseReading
        fields = ["date", "level", "notes", "test_type", "location", "medium_used"]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "test_type": forms.Select(
                choices=[
                    ("fingerstick", "Punción de dedo"),
                    ("blood_test", "Análisis de sangre"),
                ]
            ),  # Add options as necessary
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("date"),
            Field("level"),
            Field("notes"),
            Field("test_type"),
            Field("location"),
            Field("medium_used"),
            Submit(
                "submit",
                _("Guardar Lectura"),
                css_class="bg-petroleum text-white mt-4 px-4 py-2 rounded hover:bg-bright_red",
            ),
        )

        # Translate field labels
        self.fields["date"].label = _("Fecha")
        self.fields["level"].label = _("Nivel")
        self.fields["notes"].label = _("Notas")
        self.fields["test_type"].label = _("Tipo de prueba")
        self.fields["location"].label = _("Ubicación")
        self.fields["medium_used"].label = _("Medio utilizado")
