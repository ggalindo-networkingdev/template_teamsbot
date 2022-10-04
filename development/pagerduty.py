import requests
import json
from prettytable import PrettyTable
token = "y_NbAkKc66ryYTWUXYEu"
auth={"Authorization": f"Token token={token}", "Accept": "application/vnd.pagerduty+json;version=2", "Content-Type": "application/json"}
baseUrl = "https://api.pagerduty.com"

def find_user(check_dict):
    try:
        user = check_dict['user']
    except:
        user = None
    return user

def find_email(ID):
    endpoint=f"{baseUrl}/users/{ID}"
    r = requests.get(endpoint, headers=auth)
    response = r.json()
    final_user = response['user']
    email = "Not available"
    time_zone = "Not available"
    try:
        email = final_user['email']
        time_zone = final_user['time_zone']
        if email is None:
            email = "Not available"
        if time_zone is None:
            time_zone="Not available"
    except:
        email = "Not available"
        time_zone="Not available"
    response_dict = {'email': email, 'time_zone': time_zone}
    return response_dict

def get_table(list, column_name):
    return_table = PrettyTable()
    elements = []
    for list_element in list:
        elements.append(list_element)
    return_table.add_column(column_name, elements)
    return_table.align[column_name] = "l"

    return return_table.get_html_string()

def get_table_calls(list_name, list_email, list_time):
    return_table = PrettyTable()
    return_table.add_column("Name", list_name)
    return_table.align["Name"] = "l"
    return_table.add_column("Email",list_email)
    return_table.align["Email"] = "l"
    return_table.add_column("Time", list_time)
    return_table.align["Time"] = "l"
    return return_table.get_html_string()


def get_teams_list():
    endpoint=f"{baseUrl}/teams"
    query="""{
        
    }"""
    r = requests.get(endpoint, headers=auth)
    response = r.json()
    #Get all teams values as list
    list_teams=response['teams']
    return list_teams

def get_calls(ID_ESCALATION):
    list_id = [ID_ESCALATION]
    endpoint=f"{baseUrl}/oncalls?escalation_policy_ids[]={ID_ESCALATION}"
    users = []
    r = requests.get(endpoint, headers=auth)
    response = r.json()
    oncalls = response['oncalls']
    for call in oncalls:
        checking_user = find_user(call)
        if checking_user is not None:
            users.append(checking_user)
    return users

def get_escalations():
    endpoint=f"{baseUrl}/escalation_policies/"
    query="""{
        
    }"""
    r = requests.get(endpoint, headers=auth)
    response = r.json()
    escalation_policies = response['escalation_policies']
    return escalation_policies

def get_user(USER_ID):
    endpoint=f"{baseUrl}/users"
    query="""{
        id: {USER_ID}
    }"""
    r = requests.get(endpoint, headers=auth)
    response = r.json()
    #print(response)


def filter_escalations(ID_TEAM):
    list_escalations = get_escalations()
    #Return filtered escalations if you want all information about escalation policies
    filtered_escalations = []
    #Return filtered summaries if you want only the summary title and url
    list_summary = []
    for escalation in list_escalations:
        team = escalation['teams']
        if team[0]['id'] == ID_TEAM:
            summary_dict = {'title': escalation['summary'], 'id': escalation['id']}
            #print(summary_dict)
            list_summary.append(summary_dict)
            filtered_escalations.append(escalation)
    #table_summary = get_table(list_summary,'Summary Escalations')
    filtrered_info = {'escalations': filtered_escalations, 'escalations_titles': list_summary}
    return filtrered_info
    
def filter_escalations_byId(ID):
    list_escalations = get_escalations()
    info_name = []
    info_email = []
    info_time = []
    for escalation in list_escalations:
        #print(escalation)
        if escalation['id'] == ID:
            name = escalation['summary']
            users_list = get_calls(escalation['id'])
            for user in users_list:
                name = user['summary']
                id_tempuser = user['id']
                finded_email = find_email(id_tempuser)
                email = finded_email['email']
                time_zone = finded_email['time_zone']
                info_name.append(f'{name}')
                info_email.append(f'{email}')
                info_time.append(f'{time_zone}')
                # info.append('---------')
    #print(info)
    table_info = get_table_calls(info_name, info_email, info_time)
    return table_info


def get_teams_names():
    endpoint=f"{baseUrl}/teams"
    query="""{
        
    }"""
    r = requests.get(endpoint, headers=auth)
    response = r.json()
    list_teams=response['teams']
    names = []
    for team in list_teams:
        dict_team = {}
        dict_team['id'] = team['id']
        dict_team['name'] = team['name']
        names.append(dict_team)
    return names


# print("==================================")
# print("==================================")
# print("GET CALLS FUNCTION")
# get_calls()
# print("==================================")
# print("//////////////////////////////////")
# print("GET FILTRERED FUNCTION")
# print("//==============//===============//")
# get_user("PRH0AAE")
# print("==================================")
# get_calls("P6F7EI2")
# print("==================================")
# print("==================================")
# print("FILTRANDO POR ID")
