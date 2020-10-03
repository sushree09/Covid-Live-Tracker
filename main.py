#importing requests package

import requests

# fetching the covid live data from the website

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "c7c4a394f9msh56dbf3d433766c4p104386jsn043698b090b6"
    }

# converting the json data using online json convertor

response = requests.request("GET", url, headers=headers).json()



# searching by state names

def state_confirmed(state_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['confirmed']) != 0:
            if each.lower() == state_name.lower():
                return response['state_wise'][each]['confirmed']

def state_active(state_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['active']) != 0:
            if each.lower() == state_name.lower():
                return response['state_wise'][each]['active']

def state_recovered(state_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['active']) != 0:
            if each.lower() == state_name.lower():
                return response['state_wise'][each]['recovered']

def state_deceased(state_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['active']) != 0:
            if each.lower() == state_name.lower():
                return response['state_wise'][each]['deaths']


# searching by district names

def dist_confirmed(dist_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['confirmed']) != 0:
            for city in response['state_wise'][each]['district']:
                if city.lower() == dist_name.lower():
                    return response ['state_wise'][each]['district'][city]['confirmed']

def dist_active(dist_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['active']) != 0:
            for city in response['state_wise'][each]['district']:
                if city.lower() == dist_name.lower():
                    return response['state_wise'][each]['district'][city]['active']

def dist_recovered(dist_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['confirmed']) != 0:
            for city in response['state_wise'][each]['district']:
                if city.lower() == dist_name.lower():
                    return response['state_wise'][each]['district'][city]['recovered']


def dist_deceased(dist_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['confirmed']) != 0:
            for city in response['state_wise'][each]['district']:
                if city.lower() == dist_name.lower():
                    return response['state_wise'][each]['district'][city]['deceased']


#user input for state names

flag = 1
while flag != 0:


    state_name = input("Enter the state: ")
    if state_name == "0":
        break

    confirmed_cases = state_confirmed(state_name)
    print("Confirmed cases: " + confirmed_cases)

    active_cases = state_active(state_name)
    print("Active cases: " + active_cases)

    recover_cases = state_recovered(state_name)
    print("Recovered: " + recover_cases)

    death_cases = state_deceased(state_name)
    print("Deceased: " + death_cases)

#user input for district names

    dist_name = input("Enter the dist: ")
    if dist_name == "0":
        break

    confirmed_case = dist_confirmed(dist_name)
    print("Confirmed cases: " , confirmed_case)

    active_case = dist_active(dist_name)
    print("Active cases: " , active_case)

    recover_case = dist_recovered(dist_name)
    print("Recovered: " , recover_case)

    death_case = dist_deceased(dist_name)
    print("Deceased: " , death_case)
