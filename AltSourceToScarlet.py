import json

# Open the file
with open("wuxu-complete.json", "r") as f:
    data = json.load(f)

# Convert each app's data to the new format
new_apps = []
for app in data["apps"]:
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

    # Add the contact information
    if app["developerName"] == "Cool developer name":
        new_app["contact"]["web"] = "https://cooldeveloper.com"
        new_app["contact"]["twitter"] = "https://twitter.com/cooldeveloper"

    new_apps.append(new_app)

# Create the new data object
new_data = {
    "name": data["name"],
    "version": "1.0",
    "down": "",
    "dev": "Cool developer name",
    "icon": "",
    "category": "category",
    "description": "",
    "bundleID": data["identifier"],
    "screenshots": [],
    "contact": {
        "web": "https://cooldeveloper.com",
        "twitter": "https://twitter.com/cooldeveloper"
    },
    "apps": new_apps
}

# Write the new data to a file
with open("wuxu-complete-scarlet-test2.json", "w") as f:
    json.dump(new_data, f)
