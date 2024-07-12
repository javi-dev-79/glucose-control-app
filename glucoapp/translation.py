# glucoapp/translation.py

from modeltranslation.translator import TranslationOptions, register
from .models import PatientProfile, GlucoseReading, UserPreferences

@register(PatientProfile)
class PatientProfileTranslationOptions(TranslationOptions):
    fields = ("preferred_unit",)


@register(GlucoseReading)
class GlucoseReadingTranslationOptions(TranslationOptions):
    fields = ("notes",)


@register(UserPreferences)
class UserPreferencesTranslationOptions(TranslationOptions):
    fields = ("view_option",)
