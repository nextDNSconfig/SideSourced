import json

with open('wuxu-complete-plus.json', 'r') as plus_file:
    plus_data = json.load(plus_file)
    plus_apps = plus_data['apps']

with open('wuxu-complete-scarlet.json', 'r') as scarlet_file:
    scarlet_data = json.load(scarlet_file)
    scarlet_apps = scarlet_data['applications']

for scarlet_app in scarlet_apps:
    scarlet_bundle_id = scarlet_app['bundleID']
    scarlet_version = scarlet_app['version']
    scarlet_changelog = scarlet_app['changelog']
    for plus_app in plus_apps:
        plus_bundle_id = plus_app['bundleIdentifier']
        plus_version = plus_app['version']
        plus_changelog = plus_app['versionDescription']
        if scarlet_bundle_id == plus_bundle_id and scarlet_version != plus_version:
            print(f"Updating {scarlet_app['name']} from version {scarlet_version} to {plus_version}")
            scarlet_app['version'] = plus_version
            scarlet_app['down'] = plus_app['downloadURL']
            scarlet_app['changelog'] = plus_changelog
            break

with open('wuxu-complete-scarlet.json', 'w') as scarlet_file:
    json.dump(scarlet_data, scarlet_file)
