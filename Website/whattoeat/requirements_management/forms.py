from crispy_forms.bootstrap import InlineField, PrependedAppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Hidden, HTML
from django import forms
from whattoeat.models import DefiniteDietRequirement, RestrictedDietRequirement, DailyRequirementsSet, MealRequirementsSet


class DailyRequirementsSetForm(forms.ModelForm):
    num_meals_per_day = forms.IntegerField(
        widget=forms.NumberInput({'step': 1, 'max': 8, 'min': 1}),
        label="Number of Meals Per Day",
        required=True,
        min_value=1,
        max_value=8,
    )

    class Meta:
        model = DailyRequirementsSet
        fields = ("num_meals_per_day",)

    def __init__(self, *args, **kwargs):
        super(DailyRequirementsSetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        helper = self.helper
        helper.form_tag = False
        helper.disable_csrf = True
        helper.error_text_inline = False
        helper.layout = Layout(
            Field('num_meals_per_day'),
        )


class MealRequirementsSetForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
    )

    class Meta:
        model = MealRequirementsSet
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super(MealRequirementsSetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        helper = self.helper
        helper.form_tag = False
        helper.disable_csrf = True
        helper.error_text_inline = False
        helper.layout = Layout(
            Field('name'),
        )


class DefiniteRequirementForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())


    value = forms.FloatField(
        min_value=0,
        initial=0,
    )
    error = forms.IntegerField(
        max_value=100,
        min_value=0,
        initial=5,
    )


    class Meta:
        model = DefiniteDietRequirement
        fields = ("id", "name", "value", "error")
        #note id is required as it this form will be used in a ModelFormSet (see Django Docs)


    def __init__(self, *args, **kwargs):
        super(DefiniteRequirementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        helper = self.helper
        helper.form_tag = False
        helper.disable_csrf = True
        helper.field_template = 'bootstrap3/layout/inline_field.html'
        helper.layout = Layout(
            'id',
            InlineField('name', css_class="nutrient_name_field"),
            HTML("within"),
            'error',
            HTML("% of"),
            InlineField('value', css_class="rounded_decimal"),
            HTML(
                '<span class="requirements_unit" style="padding: 0px 10px 0px 10px;min-width:60px;display:inline-block;"></span>'),
            HTML('<a href="#" class="btn btn-danger delete_definite">Remove</a><br/>'),
        )


class RestrictedRequirementForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())

    value = forms.FloatField(
        min_value=0,
        initial=0,
    )

    class Meta:
        model = RestrictedDietRequirement
        fields = ("id", "name", "value", "restriction")
        #note id is required as it this form will be used in a ModelFormSet (see Django Docs)

    def __init__(self, *args, **kwargs):
        super(RestrictedRequirementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        helper = self.helper
        helper.form_tag = False
        helper.field_template = 'bootstrap3/layout/inline_field.html'
        helper.disable_csrf = True
        helper.layout = Layout(
            'id',
            InlineField('name', css_class="nutrient_name_field"),
            'restriction',
            InlineField('value', css_class="rounded_decimal"),
            HTML(
                '<span class="requirements_unit" style="padding: 0px 10px 0px 10px;min-width:60px;display:inline-block;"></span>'),
            HTML('<a href="#" class="btn btn-danger delete_restricted">Remove</a><br/>'),
        )
