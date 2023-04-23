import json

# read the first updated JSON file
with open('wuxu-complete.json') as f1:
    data1 = json.load(f1)

# read the second updated JSON file
with open('wuxu-complete-plus.json') as f2:
    data2 = json.load(f2)

# combine the two sets of apps into a single list
updated_apps = data1["apps"] + data2["apps"]

# read the outdated JSON file
with open('wuxu-complete-scarlet.json') as f3:
    old_data = json.load(f3)

# update the outdated JSON file with data from the updated JSON files
for app in updated_apps:
    app_found = False
    for old_app in old_data:
        if updated_apps[app['bundleIdentifier']] == old_app['bundleID']:
            app_found = True
            old_app['name'] = app['name']
            old_app['version'] = app['version']
            old_app['down'] = app['downloadURL']
            old_app['dev'] = app['developerName']
            old_app['icon'] = app['iconURL']
            old_app['changelog'] = app['versionDescription']
            old_app['description'] = app['localizedDescription']
            old_app['bundleID'] = app['bundleIdentifier']
            old_app['screenshots'] = app['screenshotURLs']
            break
    if not app_found:
        new_app_name = app['name']
        print(f'New app found: {new_app_name}')
        category = input('Please enter the category of this app: ')

        new_app = {
            "name": app["name"],
            "version": app["version"],
            "down": app["downloadURL"],
            "dev": app["developerName"],
            "icon": app["iconURL"],
            "category": "category",
            "changelog": app["versionDescription"],
            "description": app["localizedDescription"],
            "bundleID": app["bundleIdentifier"],
            "appstore": app["bundleIdentifier"],
            "screenshots": app["screenshotURLs"],
            "contact": {
                "web": "https://bit.ly/wuxus-sources",
                "discord": "https://bit.ly/wuxuslibrary-discord"
            }
        }
        old_data.append(new_app)

# write the updated outdated JSON file to disk
with open('scarlet-test.json', 'w') as f:
    json.dump(old_data, f)
