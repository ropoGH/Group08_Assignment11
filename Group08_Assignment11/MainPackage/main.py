'''
Name: Roger Poduska, Mia Nguyen
email: poduskrd@mail.uc.edu, nguye2m6@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Utilizes an API to return an estimate of nationality based on the name
Citations: N/a
Anything else that's relevant: https://www.iban.com/country-codes -- useful website to decifier what country is associated to country_id
'''

import json
import requests

#URL to an API with the name you are estimating nationality at the end
#No API key required
response = requests.get('https://api.nationalize.io/?name=roger')
json_string = response.content
    
parsed_json = json.loads(json_string) #Python dictionary
    

#Printing some info about the results
#Use link in documentation at top for unknown country codes
print("The country with the highest probability is the following: " + str(parsed_json["country"][0]))
print("The country with the lowest probability is the following: " + str(parsed_json["country"][-1]))