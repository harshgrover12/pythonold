import json
from urllib.request import urlopen

people_string = '''
{
"people":[
{
  "name": "john smith",
  "phone": "615-555-7164",
  "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
  "has_license": false
},
{
  "name":"Jane Doe",
  "phone": "560-555-5153",
  "emails": null,
  "has_license": true
}
]
}
'''

# Json string to python object

data = json.loads(people_string)
print(data)
print(type(data))  # <class 'dict'>
print(type(data['people']))  # <class 'list'>
for person in data['people']:
    print(person['name'])

'''
output:

john smith
Jane Doe
'''

# Converts Python object to Json string
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

'''
output:
{
  "people": [
    {
      "emails": [
        "johnsmith@bogusemail.com",
        "john.smith@work-place.com"
      ],
      "has_license": false,
      "name": "john smith",
      "phone": "615-555-7164"
    },
    {
      "emails": null,
      "has_license": true,
      "name": "Jane Doe",
      "phone": "560-555-5153"
    }
  ]
}
'''

# load method loads the file and loads method loads the string

with open('states.json', 'r') as f:
    data = json.load(f)
for state in data['states']:
    print(state)
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)

'''
Output:
{'name': 'Albama', 'abbreviation': 'AL', 'area_codes': ['205', '251', '256', '334', '938']}
{'name': 'Alaska', 'abbreviation': 'AK', 'area_codes': ['907']}
{'name': 'Arizona', 'abbreviation': 'AZ', 'area_codes': ['480', '520', '602', '623', '928']}
{'name': 'Arkansas', 'abbreviation': 'AR', 'area_codes': ['479', '501', '870']}
'''

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()
#
# data = json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data['list']['resources']))
#
# usd_rates = dict()
#
# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price
#
# print(usd_rates['USD/EUR'])