# beide json fiels einlesen
# prüfen, welche daten in der längeren nicht vorkommen
# beide dateiene zusammen führen ohne duplikate

import json

# get all the data from first file
with open('ogame tracker merge/OGame-Tracker-Export_2023-01-26_08-00-43.json', 'r') as fhandle:
    data = json.loads(fhandle.read())

    # get data reports
    def get_data(data, field):
        res_list = []
        json_dict = data['accounts'][0][field]
        for each in json_dict:
            res_list.append(each['id']) # i can now check, if this id is somewhere else in another file
            # print(each['id']) 
        return res_list
     
    field = 'combatReports'
    combat_rep = get_data(data, field)
    field = 'expeditions'
    exped = get_data(data, field)
    field = 'debrisFieldReports'
    debris = get_data(data, field)
    field = 'lifeformDiscoveries'
    life_forms = get_data(data, field)

    # print(combat_rep)
    # print(exped)
    # print(debris)
    # print(life_forms)
    
# get all the data from second file
with open('ogame tracker merge/OGame-Tracker-Export_2023-01-26_08-09-25.json', 'r') as fhandle:
    data_2 = json.loads(fhandle.read())

        # get data reports
    def get_data(data, field):
        res_list = []
        json_dict = data['accounts'][0][field]
        for each in json_dict:
            res_list.append(each['id']) # i can now check, if this id is somewhere else in another file
            # print(each['id']) 
        return res_list
    
    field = 'combatReports'
    combat_rep_2 = get_data(data_2, field)
    field = 'expeditions'
    exped_2 = get_data(data_2, field)
    field = 'debrisFieldReports'
    debris_2 = get_data(data_2, field)
    field = 'lifeformDiscoveries'
    life_forms_2 = get_data(data_2, field)

    # print(combat_rep_2)
    # print(exped_2)
    # print(debris_2)
    # print(life_forms_2)


# find differences
for each in combat_rep:
    if each in combat_rep_2:
        print(each)

for each in exped:
    if each in exped_2:
        print(each)
