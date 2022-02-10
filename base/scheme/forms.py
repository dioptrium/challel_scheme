from ast import Eq
from django import forms
from .models import Channels, Equipment, Locations
from django.forms import formset_factory, inlineformset_factory


class LocationForm(forms.ModelForm):
    class Meta:
        model=Locations
        fields = ['location','address']
        widgets = {
           'location': forms.TextInput(attrs={'size':100}),
           'address': forms.TextInput(attrs={'size':100}),}
        
class EquipmentForm(forms.ModelForm):
    class Meta:
        model=Equipment
        fields = ['equipment','description','locations_connect']
        widgets = {
           'equipment': forms.TextInput(attrs={'size':60}),
           'description': forms.TextInput(attrs={'size':60}),}

EquipmentInlineFormset = inlineformset_factory(Locations, Equipment, form=EquipmentForm, extra=15)




'''Переопределение ModelMultipleChoiceField'''

from itertools import groupby
from django.forms.models import ModelChoiceIterator, ModelMultipleChoiceField

class GroupedModelMultipleChoiceField(ModelMultipleChoiceField):

    def __init__(self, group_by_field, group_label=None, *args, **kwargs):
        """
        ``group_by_field`` is the name of a field on the model
        ``group_label`` is a function to return a label for each choice group

        """
        super(GroupedModelMultipleChoiceField, self).__init__(*args, **kwargs)
        self.group_by_field = group_by_field
        if group_label is None:
            self.group_label = lambda group: group
        else:
            self.group_label = group_label

    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return GroupedModelChoiceIterator(self)
    choices = property(_get_choices, ModelMultipleChoiceField._set_choices)

class GroupedModelChoiceIterator(ModelChoiceIterator):

    def __iter__(self):
        """Now yields grouped choices."""            
        if self.field.empty_label is not None:
            yield ("", self.field.empty_label)
        for group, choices in groupby(
                self.queryset.all(),
                lambda row: getattr(row, self.field.group_by_field)):
            if group is None:
                for ch in choices:
                    yield self.choice(ch)
            else:
                yield (
                    self.field.group_label(group),
                    [self.choice(ch) for ch in choices])

"""дополнительно"""
class GroupedCheckboxSelectMultiple(forms.CheckboxSelectMultiple):

    def optgroups(self, name, value, attrs=None):
        """
        The group name is passed as an argument to the ``create_option`` method (below).

        """
        groups = []
        has_selected = False

        for index, (option_value, option_label) in enumerate(self.choices):
            if option_value is None:
                option_value = ''

            subgroup = []
            if isinstance(option_label, (list, tuple)):
                group_name = option_value
                subindex = 0
                choices = option_label
            else:
                group_name = None
                subindex = None
                choices = [(option_value, option_label)]
            groups.append((group_name, subgroup, index))

            for subvalue, sublabel in choices:
                selected = (
                    str(subvalue) in value and
                    (not has_selected or self.allow_multiple_selected)
                )
                has_selected |= selected
                subgroup.append(self.create_option(
                    name, subvalue, sublabel, selected, index,
                    subindex=subindex, attrs=attrs, group=group_name,
                ))
                if subindex is not None:
                    subindex += 1
        return groups

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None, group=None):
        """
        Added a ``group`` argument which is included in the returned dictionary.

        """
        index = str(index) if subindex is None else "%s_%s" % (index, subindex)
        if attrs is None:
            attrs = {}
        option_attrs = self.build_attrs(self.attrs, attrs) if self.option_inherits_attrs else {}
        if selected:
            option_attrs.update(self.checked_attribute)
        if 'id' in option_attrs:
            option_attrs['id'] = self.id_for_label(option_attrs['id'], index)
        return {
            'name': name,
            'value': value,
            'label': label,
            'selected': selected,
            'index': index,
            'attrs': option_attrs,
            'type': self.input_type,
            'template_name': self.option_template_name,
            'wrap_label': True,
            'group': group,
        }

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channels
        fields = ['channel_name', 'object_a', 'object_b','traffic','description','equipment_connect',]
        widgets = {
           'channel_name': forms.TextInput(attrs={'size':100}),
           'object_a': forms.TextInput(attrs={'size':100}),
           'object_b': forms.TextInput(attrs={'size':100}),
           'traffic': forms.TextInput(attrs={'size':100}),
           'description': forms.TextInput(attrs={'size':100}),}
        
    def __init__(self, *args, **kwargs):
        super(ChannelForm, self).__init__(*args, **kwargs)
        self.fields['equipment_connect'] = GroupedModelMultipleChoiceField(
            group_by_field='locations_connect',
            queryset=Equipment.objects.all(),
            widget=forms.CheckboxSelectMultiple(),
            required=False)
        
'''class ChannelFormCopy(forms.ModelForm):
    #field = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model=Channels
        fields =['channel_name', 'object_a', 'object_b','traffic','description','equipment_connect',]

    equipment_queryset = Equipment.objects.order_by('-locations_connect')
    
   
    equipment_connect = forms.ModelMultipleChoiceField(queryset=equipment_queryset, widget=forms.CheckboxSelectMultiple)
    locations_connect = Locations.objects.all()'''
    
