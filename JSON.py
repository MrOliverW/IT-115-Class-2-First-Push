#Imports the JSON library
import json


#Creates the data dictonary

data = {

    'name': 'John Doe',
    'age': '30',
    'city': 'New York, NY',
    'interests': ['Bowling','jogging','gaming'],
    'is_student': True
}

#Provides instruction for how data should be writted to the json file
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')


#Provides instruction for how data should be read 
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

#Overwrites data variable and appends an item to the json file
loaded_data['age'] = 34
loaded_data['interests'].append('Mini Golfing')

#Provides instruction for how data should be overwritten on the json file
with open('data.json', 'w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

    print('Modified data written to data.json')