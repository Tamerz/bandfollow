from django import forms
from django.urls import reverse
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from bands.models import Artist, Venue, Event


class ArtistCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_add_artist_form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('add_event')
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Artist
        fields = ['name', 'website']


class VenueCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_add_venue_form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('add_venue')
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Venue
        fields = ['name', 'website']


class EventCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_add_event_form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('add_event')
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Event
        fields = ['title', 'date_and_time', 'venue', 'artists']
