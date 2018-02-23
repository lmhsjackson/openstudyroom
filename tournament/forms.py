from django import forms
from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import Tournament, TournamentGroup, Round
import pytz

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = [
            'name',
            'begin_time',
            'end_time',
            'tag',
            'main_time',
            'byo_time',
            'is_open',
            'is_public',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(),
            'begin_time': forms.SelectDateWidget(),
            'end_time': forms.SelectDateWidget(),
        }

class TournamentAboutForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['description', 'about']

class TournamentGroupForm(ModelForm):
    class Meta:
        model = TournamentGroup
        fields = ['name']

class RoundForm(ModelForm):
    class Meta:
        model = Round
        fields = ['name']