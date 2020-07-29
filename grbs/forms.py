from .models import GRB
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

class GRBForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GRBForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = '/grbs/add_grb'
        self.helper.layout = Layout(
            Fieldset("Add information about a new GRB",
                Row(
                    Column('grb_name', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('ra', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('dec', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('comments', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
             ),
            Submit('submit', 'Add grbs')
        )
    class Meta:
        model = GRB
        fields = ('comments', 'grb_name', 'ra', 'dec')
