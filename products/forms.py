from .models import Product
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = '/products/add_product'
        self.helper.layout = Layout(
            Fieldset("Products Descriptions",
                Row(
                    Column('description', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('product_name', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
             ),
            Submit('submit', 'Add products')
        )
    class Meta:
        model = Product
        fields = ('description', 'product_name')
