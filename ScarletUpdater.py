import json

# Load the plus app data from file
with open('wuxu-complete-plus.json', 'r') as f:
    plus_data = json.load(f)

# Load the scarlet app data from file
with open('wuxu-complete-scarlet.json', 'r') as f:
    scarlet_data = json.load(f)

# Loop through each app in plus data
for plus_app in plus_data:
    # Get the bundle identifier for the plus app
    plus_bundle_id = plus_app['bundleIdentifier']

    # Loop through each app in scarlet data
    for scarlet_app in scarlet_data:
        # Get the bundle identifier for the scarlet app
        scarlet_bundle_id = scarlet_app['bundleID']

        # Compare bundle identifiers
        if plus_bundle_id == scarlet_bundle_id:
            
            # Compare the app version numbers to see if there is an update
            if plus_app['version'] > scarlet_app['version']:
                
                # Update the app information with the new version details
                updated_app = {
                    "name": plus_app['name'],
                    "version": plus_app['version'],
                    "down": plus_app['downloadURL'],
                    "dev": plus_app['developerName'],
                    "icon": plus_app['iconURL'],
                    "category": scarlet_app['category'],
                    "changelog": plus_app['versionDescription'],
                    "description": scarlet_app['description'],
                    "bundleID": plus_bundle_id,
                    "screenshots": scarlet_app['screenshots'],
                    "contact": scarlet_app['contact']
                }
                
                # Add the updated app information to the dictionary
                updated_apps[scarlet_bundle_id] = updated_app

# Loop through the scarlet apps and update any apps that have new versions
for scarlet_app in scarlet_apps:
    scarlet_bundle_id = scarlet_app['bundleID']
    
    if scarlet_bundle_id in updated_apps:
        scarlet_app.update(updated_apps[scarlet_bundle_id])

# Write the updated scarlet apps to the file
with open('wuxu-complete-scarlet.json', 'w') as f:
    json.dump(scarlet_apps, f, indent=4)
