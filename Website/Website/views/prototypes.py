from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.forms.formsets import formset_factory
from Website.forms.meal_generation_prototype import IngredientSelectForm, RequirementsInputForm
#from Website.meals.MealClasses import DefiniteNutrientRequirement, RestrictedNutrientRequirement


def meal_generation_prototype(request, numIngredients, numRequirements):
    #prototype meal generation implemented 24/11/2013
    numIngredients =  int(numIngredients)
    numRequirements = int(numRequirements)

    IngredientsFormSet = formset_factory(IngredientSelectForm, extra=numIngredients)
    RequirementsFormSet = formset_factory(RequirementsInputForm, extra=numRequirements)
    if request.method == 'POST':
        ingredients_formset = IngredientsFormSet(request.POST, request.FILES, prefix='ingredients')
        requirements_formset = RequirementsFormSet(request.POST, request.FILES, prefix='requirements')
        if ingredients_formset.is_valid() and requirements_formset.is_valid():
            requirements = []
            restrictedRequirements = []
            #for form in requirements_formset:
                #if(form.clean_data['restriction']== '='):
                    #requirements.append(DefiniteNutrientRequirement(form.clean_data['amount'],form.clean_data['error']))
                #else:
                   # restrictedRequirements.append(RestrictedNutrientRequirement(threshold=form.clean_data['amount'],restriction=form.clean_data['restriction'])
            #return HttpResponseRedirect("prototype/meal_generator_form_output.html")
    else:
        ingredients_formset = IngredientsFormSet( prefix='ingredients')
        requirements_formset = RequirementsFormSet( prefix='requirements')
    return render_to_response("meal_pages/meal_generation.html", {
        'requirements_formset': requirements_formset,
        'ingredients_formset': ingredients_formset,
                              })