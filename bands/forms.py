from django import forms

from bands.models import Artist, Venue, Event


class ArtistCreationForm(forms.ModelForm):

    name = forms.CharField(
        max_length=100, widget=forms.fields.TextInput(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = Artist
        fields = ['name']


class VenueCreationForm(forms.ModelForm):

    name = forms.CharField(
        max_length=100, widget=forms.fields.TextInput(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = Venue
        fields = ['name']


class EventCreationForm(forms.ModelForm):

    title = forms.CharField(
        max_length=100, widget=forms.fields.TextInput(attrs={
            'class': 'form-control',
        })
    )
    date_and_time = forms.DateTimeField(
        widget=forms.fields.DateTimeInput(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = Event
        fields = ['title', 'date_and_time']
