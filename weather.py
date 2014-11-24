import requests

weather_url = "http://www.wunderground.com/history/airport/KNYC/2013/1/1/CustomHistory.html?dayend=1&monthend=1&yearend=2014&req_city=NA&req_state=NA&req_statename=NA&format=1"
content = requests.get(weather_url).text

content = content.replace("<br />","").split('\n')[1:]

''' Removed the first element since it was not necessary (date). '''
fields = content[0].split(',')
fields.pop(0)

''' Removed blank first line and empty line at the end of the text. '''
content = content[1:-1]

''' Create the dictionary of dates and temperature values for those dates. '''
weather_data = {}
counter = 0

for row in content:
    row = row.split(',')
    weather_data[row[0]] = {}
    for field in fields:
        counter += 1
        weather_data[row[0]][field] = row[counter]
    counter = 0

