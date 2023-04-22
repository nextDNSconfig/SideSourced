import json

# Load the existing "wuxu-complete-scarlet.json" file
with open('wuxu-complete-scarlet.json', 'r') as f:
    existing_data = json.load(f)

# Load the "wuxu-complete-plus.json" file
with open('wuxu-complete-plus.json', 'r') as f:
    data = json.load(f)

# Convert the JSON data to the new format
new_apps = []
for app in data['apps']:
    new_app = {
        'name': app['name'],
        'version': app['version'],
        'icon': app['iconURL'],
        'down': app['downloadURL'],
        'dev': app['developerName'],
        'changelog': app['versionDescription'],
        'description': app['localizedDescription'],
        'bundleID': app['bundleIdentifier'],
        'appstore': app['bundleIdentifier'],
        'screenshots': app['screenshotURLs'],
        'contact': {
            'web': 'https://bit.ly/wuxus-sources',
            'discord': 'https://bit.ly/wuxuslibrary-discord'
        }
    }
    new_apps.append(new_app)

# Add the new app data to the existing data
existing_data['apps'].extend(new_apps)

# Write the updated data back to the "wuxu-complete-scarlet.json" file
with open('wuxu-complete-scarlet.json', 'w') as f:
    json.dump(existing_data, f, indent=4)
