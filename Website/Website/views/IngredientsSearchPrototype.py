from django.shortcuts import render_to_response
import requests
import json
from requests_oauthlib import OAuth1
from requests_oauthlib.oauth1_session import OAuth1Session
from Website.API_Info import API_Codes
from Website.fatsecret_wrappers.foods import BrandedFoodDescription, GenericFoodDescription


def search_ingredient(request,search_text,max_results = 20, format = 'json'):
    #set up url for request
    url = API_Codes.FAT_SECRET_URL

    #set upt OAuth1 authentication using FatSecret keys
    auth = OAuth1(API_Codes.FAT_SECRET_API_KEY,
                  API_Codes.FAT_SECRET_API_SECRET,
                  signature_type='query')

    #add params for search
    params = {'search_expression':search_text,
              'method':'foods.search',
              'format':'json', #json output
              'max_results':max_results,}

    #make the request
    request = requests.get(url,auth=auth,params=params)

    #parse the returned json
    result = json.load(request.text)

    #throw away parts we dont need: only need food data
    result = result['foods']['food']

    #build the results into an array
    foods = []
    for i in range(0,len(result)):
        name=result[i]['food_name'],
        id=result[i]['food_id'],
        url=result[i]['food_url'],
        description=result[i]['food_description']

        if result[i]['food_type'] == 'Branded': #deal with branded food types
            foods.append(BrandedFoodDescription(name=name,
                                                id=id,
                                                url=url,
                                                description=description,
                                                brand=result[i]['brand_name']))
        else:
            foods.append(GenericFoodDescription(name=name,
                                                id=id,
                                                descritption=description,
                                                url=url))

    return render_to_response('ingredients_search_output.html',{'search_results':foods})
