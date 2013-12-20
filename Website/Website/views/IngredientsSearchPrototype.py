from django.shortcuts import render_to_response
import requests
import json
import math
from requests_oauthlib import OAuth1
from requests_oauthlib.oauth1_session import OAuth1Session
from Website.API_Info import API_Codes
from Website.fatsecret_wrappers.foods import BrandedFoodDescription, GenericFoodDescription
from Website.forms.food_search import FoodSearchForm

NUMBER_PAGES_TO_DISPLAY = 5

def pagination_numbers(active_page, number_pages_displayed, total_pages):
    if active_page <= (number_pages_displayed/2):
        return range(0,number_pages_displayed + 1)
    elif active_page >= (total_pages - (number_pages_displayed/2)) :
        return range(total_pages - number_pages_displayed + 1, total_pages + 1)
    else:
        return range(active_page-(number_pages_displayed/2), active_page + (number_pages_displayed/2) + 1)


def search_ingredient(request, page_number=0, max_results = 50, format = 'json'):
    #catch input errors to call
    if max_results < 1 :
        max_results = 1
    if page_number < 0:
        page_number = 0

    #should be set to true only if at least one result was found from search
    some_results_found = False
    #page numbers to be displayed in the pagination bar
    page_numbers_to_display = []

    if request.method.upper() == 'GET':
        search_form = FoodSearchForm(request.GET)
        if search_form.is_valid():
            #retrieve search text
            search_text = search_form.cleaned_data['search_text']

            #set up url for request
            url = API_Codes.FAT_SECRET_URL

            #set upt OAuth1 authentication using FatSecret keys
            auth = OAuth1(API_Codes.FAT_SECRET_API_KEY,
                          API_Codes.FAT_SECRET_API_SECRET,
                          signature_type='query')

            #add params for search
            params = {'search_expression': search_text,
                      'method': 'foods.search',
                      'format': format, #json output by default
                      'max_results': max_results,
                      'page_number':page_number,}

            #make the request
            request = requests.get(url, auth=auth, params=params)

            #parse the returned json
            result = json.loads(request.text)



            #make sure something was returned
            try:
                #get the total results found and the total number of pages
                total_results = int(result['foods']['total_results'])
                total_number_pages = int(math.ceil(total_results/max_results)) + 1


                #throw away parts we dont need: only need food data
                result = result['foods']['food']

                #build the results into an array
                foods = []
                for i in range(0, len(result)):
                    name = result[i]['food_name'],
                    id = result[i]['food_id'],
                    url = result[i]['food_url'],
                    description = result[i]['food_description']


                    if result[i]['food_type'] == 'Brand': #deal with branded food types
                        foods.append(BrandedFoodDescription(name=name,
                                                            id=id,
                                                            url=url,
                                                            description=description,
                                                            brand=result[i]['brand_name']))
                    else:
                        foods.append(GenericFoodDescription(name=name,
                                                            id=id,
                                                            description=description,
                                                            url=url))
                some_results_found = True
                page_numbers_to_display = pagination_numbers(active_page=page_number,number_pages_displayed=NUMBER_PAGES_TO_DISPLAY,total_number_pages=total_number_pages)

            except (KeyError,TypeError):
                foods = []

            test_cond = 5/2
            return render_to_response('meal_pages/ingredients_search.html',
                                      {'search_results':foods,
                                       'form':search_form,
                                       'some_results_found':some_results_found,
                                       'total_results':total_results,
                                       'total_pages':total_number_pages,
                                       'page_number': page_number,
                                       'first_cond': page_number == 5/2,
                                       'test_cond' : 5/2 ,
                                       'page_numbers_to_display':page_numbers_to_display,
                                      })
    search_form = FoodSearchForm()
    return render_to_response('meal_pages/ingredients_search.html',
                              {'form':search_form,
                               'results_found':some_results_found,
                               })