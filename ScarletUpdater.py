import json

# Open the "wuxu-complete-plus.json" file and load its contents into a dictionary
with open('wuxu-complete-plus.json', 'r') as plus_file:
    plus_data = json.load(plus_file)
    # Extract the "apps" list from the dictionary and assign it to a variable
    plus_apps = []
    for key in plus_data:
        if isinstance(plus_data[key], list):  # check if value is a list
            plus_apps.extend(plus_data[key])

# Open the "wuxu-complete-scarlet.json" file and load its contents into a dictionary
with open('wuxu-complete-scarlet.json', 'r') as scarlet_file:
    scarlet_data = json.load(scarlet_file)
    # Extract the "apps" list from each key in the dictionary and combine them into one list
    scarlet_apps = []
    for key in scarlet_data:
        if isinstance(scarlet_data[key], list):  # check if value is a list
            scarlet_apps.extend(scarlet_data[key])

# Iterate over each app in the "applications" list of the scarlet_data dictionary
for scarlet_app in scarlet_apps:
    # Extract the bundle ID, version, and changelog from the current scarlet_app dictionary
    scarlet_bundle_id = scarlet_app['bundleID']
    scarlet_version = scarlet_app['version']
    scarlet_changelog = scarlet_app['changelog']
    
    # Iterate over each app in the "apps" list of the plus_data dictionary
    for plus_app in plus_apps:
        # Extract the bundle identifier, version, and version description from the current plus_app dictionary
        plus_bundle_id = plus_app['bundleIdentifier']
        plus_version = plus_app['version']
        plus_changelog = plus_app['versionDescription']
        
        # If the bundle ID of the current scarlet_app matches the bundle identifier of the current plus_app
        # and the versions are not the same, update the scarlet_app with information from the plus_app
        if scarlet_bundle_id == plus_bundle_id and scarlet_version != plus_version:
            # Print a message indicating that the app is being updated
            print(f"Updating {scarlet_app['name']} from version {scarlet_version} to {plus_version}")
            # Update the version, download URL, and changelog of the scarlet_app with information from the plus_app
            scarlet_app['version'] = plus_version
            scarlet_app['down'] = plus_app['downloadURL']
            scarlet_app['changelog'] = plus_changelog
            # Exit the inner loop, since we've found the matching plus_app and updated the scarlet_app
            break

# Write the updated scarlet_data dictionary to the "wuxu-complete-scarlet.json" file
with open('wuxu-complete-scarlet.json', 'w') as scarlet_file:
    json.dump(scarlet_data, scarlet_file)
