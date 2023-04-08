import json
import re

# Load the JSON file
with open('wuxu-complete++.json') as f:
    data = json.load(f)

# Define a regular expression pattern for the date format (YYYY-MM-DD)
date_pattern = r'^\d{4}-\d{2}-\d{2}$'

print('\n' + '--------------------------' + '\n')

# Get user input for new app
new_app = {}
new_app['bundleIdentifier'] = input('\033[1;96m' + 'Enter the bundle identifier of the new app: ' + '\033[0m')
new_app['developerName'] = input('\033[1;96m' + 'Enter the developer name of the new app: ' + '\033[0m')
new_app['downloadURL'] = input('\033[1;96m' + 'Enter the download URL of the new app: ' + '\033[0m')
new_app['iconURL'] = input('\033[1;96m' + 'Enter the icon URL of the new app: ' + '\033[0m')
new_app['localizedDescription'] = input('\033[1;96m' + 'Enter the description of the new app: ' + '\033[0m')
new_app['name'] = input('\033[1;96m' + 'Enter the name of the new app: ' + '\033[0m')
new_app['screenshotURLs'] = input('\033[1;96m' + 'Enter a list of screenshot URLs of the new app separated by commas: ' + '\033[0m').split(',')
new_app['size'] = int(input('\033[1;96m' + 'Enter the size of the new app: ' + '\033[0m'))
new_app['subtitle'] = input('\033[1;96m' + 'Enter the subtitle of the new app: ' + '\033[0m')
new_app['tintColor'] = input('\033[1;96m' + 'Enter the hex tint color of the new app: ' + '\033[0m').strip()
if not new_app['tintColor'].startswith('#'):
    new_app['tintColor'] = '#' + new_app['tintColor']
new_app['version'] = input('\033[1;96m' + 'Enter the version of the new app: ' + '\033[0m')
new_app['versionDate'] = input('\033[1;96m' + 'Enter the version date of the new app (YYYY-MM-DD): ' + '\033[0m')
while not re.match(date_pattern, new_app['versionDate']):
    new_app['versionDate'] = input('\033[1;96m' + 'Invalid date format. Please enter the version date of the new app (YYYY-MM-DD): ' + '\033[0m')
new_app['versionDescription'] = input('\033[1;96m' + 'Enter the description of the version: ' + '\033[0m')
new_app['versions'] = []

# Get user input for new app version

new_app_version = {}
new_app_version['date'] = new_app['versionDate']
new_app_version['downloadURL'] = new_app['downloadURL']
new_app_version['localizedDescription'] = new_app['versionDescription']
new_app_version['size'] = new_app['size']
new_app_version['version'] = new_app['version']

new_app['versions'].append(new_app_version)

# Get user input for new news
new_news = {}
new_news['version'] = new_app['version']
new_news['versionDescription'] = input("Enter the version description of the new app: ")
new_news['date'] = new_app['versionDate']

# Add new app and news to the beginning of the list
data['apps'].insert(0, new_app)
data['apps'][0]['versions'][0]['date'] = new_news['date']
data['apps'][0]['versions'][0]['localizedDescription'] = new_news['versionDescription'] + '\n' + data['apps'][0]['versions'][0]['localizedDescription']
data['apps'][0]['versionDate'] = new_news['date']
data['apps'][0]['versionDescription'] = new_news['versionDescription'] + '\n' + data['apps'][0]['versionDescription']

# Save the JSON file
with open('wuxu-complete++.json', 'w') as f:
    json.dump(data, f, indent=4)