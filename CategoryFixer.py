import json

# Dictionary mapping categories to their names
categories = {
    "Tweaked Apps": "Tweaked Apps",
    "Cracked/Paid Apps": "Cracked/Paid Apps",
    "Free Streaming": "Free Streaming",
    "Games": "Games",
    "Utilities": "Utilities",
    "Jailbreaks/Tweaks": "Jailbreaks/Tweaks"
}

# Load the JSON file
with open('wuxu-complete-scarlet-test.json') as f:
    data = json.load(f)

# Iterate through each app
for category in categories:
    for app in data[category]:
        # Update the category name
        app['category'] = categories[category]

# Save the updated data to the JSON file
with open('wuxu-complete-scarlet-test.json', 'w') as f:
    json.dump(data, f)
