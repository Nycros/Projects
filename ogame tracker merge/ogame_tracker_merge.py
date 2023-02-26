# beide json fiels einlesen
# prüfen, welche daten in der längeren nicht vorkommen
# beide dateiene zusammen führen ohne duplikate

# Export data from ozone
# write data from the 2 json exports from libra into the ozone export

# type: is just main data and should not be changed
# servers is just main data and should not be changed


import json
import csv

baseFile = 'ogame tracker merge/Base_OGame-Tracker-Export_2023-02-25_16-17-57.json'
extraFile = 'ogame tracker merge/OGame-Tracker-Export_2023-02-24_11-25-01.json'

# get all the data from first file
with open(baseFile, 'r') as fhandle:
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
with open(extraFile, 'r') as fhandle:
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
    # test


# find differences
count_comb_base = 0
for each in combat_rep:
    count_comb_base += 1

count_comb_extra = 0
for each in combat_rep_2:
    count_comb_extra += 1

 

# write all different combat data into a new file
# outComb = []
# count = 0
# with open("ogame tracker merge/sample.json", "w") as outfile:
#     for each in data_2['accounts'][0]['combatReports']:
#         if each['id'] not in combat_rep:
#             outComb.append(each)
#             count += 1
#     json.dump(outComb, outfile)

# print(f"{count} id´s read. {count_comb_base} in base file and {count_comb_extra} in extra file")

processedData = 0
with open("ogame tracker merge/new.json", "w") as newfile:
    newData = data.copy()
    outComb = []
    outExped = []
    outDeb = []
    outLife = []

    # Get combat data
    for each in data_2['accounts'][0]['combatReports']:
        if each['id'] not in combat_rep:
            processedData += 1
            outComb.append(each)
    # Get expedition data
    for each in data_2['accounts'][0]['expeditions']:
        if each['id'] not in exped:
            processedData += 1
            outExped.append(each)
    # Get debris data
    for each in data_2['accounts'][0]['debrisFieldReports']:
        if each['id'] not in debris:
            processedData += 1
            outDeb.append(each)
    # Get liffefroms data
    for each in data_2['accounts'][0]['lifeformDiscoveries']:
        if each['id'] not in life_forms:
            processedData += 1
            outLife.append(each)

    newData['accounts'][0]['combatReports'].extend(outComb)
    newData['accounts'][0]['expeditions'].extend(outDeb)
    newData['accounts'][0]['debrisFieldReports'].extend(outExped)
    newData['accounts'][0]['lifeformDiscoveries'].extend(outExped)

    json.dump(newData, newfile)

print(f"{processedData} data was processed")