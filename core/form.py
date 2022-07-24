from django.forms import ModelForm
from delivery.models import Delivery


class NovaForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__' 


class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__' 