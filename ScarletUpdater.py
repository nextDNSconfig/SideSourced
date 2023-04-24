import json

# Load the contents of the JSON files into variables
with open('wuxu-complete-plus.json', 'r') as f:
    plus_apps = json.load(f)
    
with open('wuxu-complete-scarlet.json', 'r') as f:
    scarlet_apps = json.load(f)

# Create a dictionary to store the updated app information
updated_apps = {}

# Loop through each app in the 'wuxu-complete-plus.json' file
for plus_app in plus_apps:
    plus_bundle_id = plus_app['bundleIdentifier']
    
    # Loop through each app in the 'wuxu-complete-scarlet.json' file
    for scarlet_app in scarlet_apps:
        scarlet_bundle_id = scarlet_app['bundleID']
        
        # Compare the bundle identifiers to see if they match
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
