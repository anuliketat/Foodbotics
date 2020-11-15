from django import forms
from django.forms import formset_factory
from . models import Prep_methods
import re

class AddNewItem(forms.Form):
    item = forms.CharField(label="", max_length=70, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Item'}))
    cuisine_choices = (
                        (" ", "--- Cuisine ---"),
                        ("1", "Arabian"),
                        ("2", "Biryani"),
                        ("3", "Continental"),
                        ("4", "Chinese"),
                        ("5", "Desserts")
                    )
    cuisine = forms.ChoiceField(label='', choices=cuisine_choices, required=False,
                                            widget=forms.Select(attrs={'class':'form-control'}))

class AddItemTasks(forms.Form):
    #num_tasks = forms.IntegerField(label='Num Tasks', max_value=15, help_text="")
    task_choices = [(i, i) for i in range(5, 65, 5)] #range(n, (n * m) + 1, n)
    task_choices.insert(0, (1, 1))
    task_choices.insert(0, ('', 'Duration'))
    query = Prep_methods.objects.all().order_by('method')

    source_station = forms.ModelChoiceField(label='', queryset=query, empty_label="Source",
                                                widget=forms.Select(attrs={'class': 'form-control'}))
    dest_station = forms.ModelChoiceField(label='', queryset=query, empty_label="Destination",
                                                widget=forms.Select(attrs={'class': 'form-control'}))
    task_time = forms.ChoiceField(label='', choices=task_choices,
                                                widget=forms.Select(attrs={'class': 'form-control'}))


    def clean(self):
        pass
        #cleaned_data = super().clean()
        #station_data = cleaned_data.get("station")

ItemFormset = formset_factory(AddItemTasks, extra=1)



