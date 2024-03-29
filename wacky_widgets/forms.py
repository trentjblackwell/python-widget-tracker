from django.forms import ModelForm
from .models import Widget

class WidgetForm(ModelForm):
  class Meta:
    model = Widget
    fields = 'name', 'description', 'quantity'