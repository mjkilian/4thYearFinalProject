from dajax.core import Dajax
from django.template.loader import render_to_string
from dajaxice.decorators import dajaxice_register
from Website.views.search_ingredient import fatSecretSearchCall, extractResults, pagination_numbers, NUMBER_PAGES_TO_DISPLAY
import math

'''
Contains all DAJAX functions for dynamic page updates. Note these must be kept here to conform with the DAJAX methodology
'''

'''
DAJAX method to update results to show a new page of results
'''
@dajaxice_register
def update_results(search_text,page_number,max_results = 50):
    page_number = int(page_number)
    
    #call API search
    result = fatSecretSearchCall(search_text, page_number, max_results)

    #get the total results found and the total number of pages
    total_results = int(result['foods']['total_results'])
    total_number_pages = int(math.ceil(total_results / max_results)) + 1

    #extract the food descriptions from the results
    foods = extractResults(result)

    page_numbers_to_display = pagination_numbers(page_number, NUMBER_PAGES_TO_DISPLAY, total_number_pages)

    results_render = render_to_string('meal_pages/ingredient_search/ingredient_search_results.html',
                                       {'search_results':foods,
                                        'search_text':search_text,
                                       'total_results':total_results,
                                       'total_pages':total_number_pages,
                                       'page_number': page_number,
                                       'page_numbers_to_display':page_numbers_to_display,
                                       'last_page':total_number_pages-1,
                                      })

    dajax = Dajax()
    dajax.assign('#results', 'innerHTML', results_render)
    return dajax.json()


