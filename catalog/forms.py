from django import forms

from catalog.models import Product, Version

class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'purchase_price', 'created_at')

    def clean_data(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                           'бесплатно', 'обман', 'полиция', 'радар']

        if self.cleaned_data['name'] not in forbidden_words:
            return self.cleaned_data['name']
        raise forms.ValidationError(f'Название товара не должно содержать запрещенные слова:{forbidden_words}')


    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                           'бесплатно', 'обман', 'полиция', 'радар']

        if self.cleaned_data['description'] not in forbidden_words:
            return self.cleaned_data['description']
        raise forms.ValidationError(f'Описание товара не должно содержать запрещенные слова:{forbidden_words}')


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        #fields = ('product', 'version_number', 'version_name', 'current_version_indicator')
        fields = '__all__'

