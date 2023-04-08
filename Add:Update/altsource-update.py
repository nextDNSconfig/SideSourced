import json
import datetime

# Load the JSON data from a file
with open('wuxu-complete++.json', 'r') as f:
    data = json.load(f)

# Display a numbered list of app names for the user to choose from
print('\n' + '--------------------------' + '\n')
print('\033[1;96mHere are your apps:\033[0m')
print("\n")

for i, app in enumerate(data['apps']):
    print(f"(\033[1;96m{i+1}\033[0m) \033[1m{app['name']}\033[0m")

print('\n' + '--------------------------' + '\n')

# Get the app number from the user
while True:
    app_num = input('\033[1;96mPlease select an app to update: \033[0m')
    try:
        app_num = int(app_num)
        if app_num < 1 or app_num > len(data['apps']):
            raise ValueError
        break
    except ValueError:
        print('\033[31mError: Invalid app number\033[0m')

# Get the selected app
selected_app = data['apps'][app_num - 1]

# Get the version data from the user
while True:
    print("\n")
    version_date = input('\033[1;96mNew version date (YYYY-MM-DD): \033[0m')
    try:
        new_date = datetime.datetime.strptime(version_date, '%Y-%m-%d')
        old_date = datetime.datetime.strptime(selected_app['versions'][0]['date'], '%Y-%m-%d')
        if new_date > old_date:
            new_version_num = input('\033[1;96mNew version: \033[0m')
            old_version_num = selected_app['versions'][0]['version']
            if new_version_num > old_version_num:
                break
            else:
                print('\033[31mError: The updated version must be greater than the existing version.\033[0m')
        else:
            print('\033[31mError: The updated version date must be greater than the existing version date.\033[0m')
    except ValueError:
        print('\033[31mError: Date must be in the format YYYY-MM-DD\033[0m')

new_size = input('\033[1;96mNew size in bytes (leave blank if not changed): \033[0m')
if new_size == '':
    new_size = selected_app['versions'][0]['size']
else:
    new_size = int(new_size)

new_version = {
    'date': version_date,
    'downloadURL': input('\033[1;96mNew download URL: \033[0m'),
    'localizedDescription': input('\033[1;96mNew changelog: \033[0m'),
    'size': new_size,
    'version': new_version_num
}

# Add the new version to the beginning of the versions list
selected_app['versions'].insert(0, new_version)

# Update the app data with the new version information
selected_app['versionDate'] = new_version['date']
selected_app['downloadURL'] = new_version['downloadURL']
selected_app['versionDescription'] = new_version['localizedDescription']
selected_app['size'] = new_version['size']
selected_app['version'] = new_version['version']

# Find the news with the matching bundle identifier and update its date
for news in data['news']:
    if news['appID'] == selected_app['bundleIdentifier']:
        news['date'] = new_version['date']
        break

# Save the updated JSON data
with open('wuxu-complete++.json', 'w') as f:
    json.dump(data, f, indent=2)

print("\n")
print('\033[1;96mUpdated apps and news!\033[0m')
