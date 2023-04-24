import json

with open('wuxu-complete-plus.json', 'r') as f1, open('wuxu-complete-scarlet.json', 'r') as f2:
    plus_apps = json.load(f1)
    scarlet_apps = json.load(f2)

# Loop through each app in plus_apps and compare it with each app in scarlet_apps
for plus_app in plus_apps:
    for scarlet_app in scarlet_apps:
        if plus_app['bundleID'] == scarlet_app['bundleIdentifier']:
            if plus_app['version'] != scarlet_app['version'] or plus_app['downloadURL'] != scarlet_app['downloadURL'] or plus_app['changelog'] != scarlet_app['versionDescription']:
                scarlet_app['version'] = plus_app['version']
                scarlet_app['versionDescription'] = plus_app['changelog']
                scarlet_app['downloadURL'] = plus_app['down']

# Write the updated scarlet_apps to wuxu-complete-scarlet.json
with open('wuxu-complete-scarlet.json', 'w') as f:
    json.dump(scarlet_apps, f)
