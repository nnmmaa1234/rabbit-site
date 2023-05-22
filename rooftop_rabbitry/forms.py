from django.forms import ModelForm, forms
from rooftop_rabbitry.models import Rabbit, RabbitBreed

class RabbitForm(ModelForm):
    
    class Meta:
        model = Rabbit
        fields = '__all__'

class breedForm(ModelForm):
    class Meta:
        model = RabbitBreed
        fields = '__all__'