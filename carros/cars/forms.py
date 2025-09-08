from django import forms
from .models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 20000:
            self.add_error('value', 'O valor do carro não pode ser menor que 20.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is not None and (factory_year < 1975):
            self.add_error('factory_year', 'O ano de fabricação não pode ser menor que 1985')
        return factory_year