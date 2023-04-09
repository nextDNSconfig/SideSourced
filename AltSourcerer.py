import json
import datetime
import re

print('\n' + '--------------------------' + '\n')

source_action = input('\033[1;96mWhat source would you like to use:\033[0m' + "\n" + "\n" + '(\033[1;96m1\033[0m) wuxu-complete++' + "\n" '(\033[1;96m2\033[0m) wuxu-complete' + "\n" + '(\033[1;96m3\033[0m) other' + "\n" + "\n" + '\033[1;96mEnter 1, 2 or 3: ' + '\033[0m').lower()

if source_action == '1':

    userfile = 'wuxu-complete++.json'

elif source_action == '2':

    userfile = 'wuxu-complete.json'

elif source_action == '3':

    userfile = input('\033[1;96m' + 'Please enter the name of your JSON or the path following the name (include .json): ' + '\033[0m')

# Load the JSON data from a file
with open(userfile, 'r') as f:
    data = json.load(f)

print('\n' + '--------------------------' + '\n')
app_action = input('\033[1;96m' + 'Do you want to:' + '\033[0m' + "\n" + "\n" + '(\033[1;96m1\033[0m) Update an existing app' + "\n" '(\033[1;96m2\033[0m) Add a new app' + "\n" + "\n" + '\033[1;96mEnter 1 or 2 : ' + '\033[0m').lower()

if app_action == '1':

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

    # Display the previous version data
    print("\n")
    print(f"\033[1mPrevious Version Data for {selected_app['name']}:\033[0m")
    print("\n")
    for i, version in enumerate(selected_app['versions']):
        print(f"\n\033[1mVersion {i+1}:\033[0m")
        print("\n")
        print(f"\033[1;96mDate:\033[0m {version['date']}")
        print(f"\033[1;96mVersion Number:\033[0m {version['version']}")
        print(f"\033[1;96mDownload URL:\033[0m {version['downloadURL']}")
        print(f"\033[1;96mChangelog:\033[0m {version['localizedDescription']}")
        print(f"\033[1;96mSize (in bytes):\033[0m {version['size']}")
        print("\n")

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
    with open(userfile, 'w') as f:
        json.dump(data, f, indent=2)

    print("\n")

elif app_action == '2':

    # Define a regular expression pattern for the date format (YYYY-MM-DD)
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'

    print('\n' + '--------------------------' + '\n')

    # Get user input for new app
    new_app = {}
    new_app['bundleIdentifier'] = input('\033[1;96m' + 'Enter the bundle identifier of the new app: ' + '\033[0m')
    new_app['developerName'] = input('\033[1;96m' + 'Enter the developer name of the new app: ' + '\033[0m')
    new_app['downloadURL'] = input('\033[1;96m' + 'Enter the download URL of the new app: ' + '\033[0m')
    new_app['iconURL'] = input('\033[1;96m' + 'Enter the icon URL of the new app: ' + '\033[0m')
    new_app['localizedDescription'] = input('\033[1;96m' + 'Enter the description of the new app: ' + '\033[0m')
    new_app['name'] = input('\033[1;96m' + 'Enter the name of the new app: ' + '\033[0m')
    new_app['screenshotURLs'] = input('\033[1;96m' + 'Enter a list of screenshot URLs of the new app separated by commas: ' + '\033[0m').split(',')
    new_app['size'] = int(input('\033[1;96m' + 'Enter the size of the new app: ' + '\033[0m'))
    new_app['subtitle'] = input('\033[1;96m' + 'Enter the subtitle of the new app: ' + '\033[0m')
    new_app['tintColor'] = input('\033[1;96m' + 'Enter the hex tint color of the new app: ' + '\033[0m').strip()
    if not new_app['tintColor'].startswith('#'):
        new_app['tintColor'] = '#' + new_app['tintColor']
    new_app['version'] = input('\033[1;96m' + 'Enter the version of the new app: ' + '\033[0m')
    new_app['versionDate'] = input('\033[1;96m' + 'Enter the version date of the new app (YYYY-MM-DD): ' + '\033[0m')
    while not re.match(date_pattern, new_app['versionDate']):
        new_app['versionDate'] = input('\033[1;96m' + 'Invalid date format. Please enter the version date of the new app (YYYY-MM-DD): ' + '\033[0m')
    new_app['versionDescription'] = input('\033[1;96m' + 'Enter the description of the version: ' + '\033[0m')
    new_app['versions'] = []

    # Get user input for new app version

    new_app_version = {}
    new_app_version['date'] = new_app['versionDate']
    new_app_version['downloadURL'] = new_app['downloadURL']
    new_app_version['localizedDescription'] = new_app['versionDescription']
    new_app_version['size'] = new_app['size']
    new_app_version['version'] = new_app['version']

    new_app['versions'].append(new_app_version)

    # Get user input for new news
    new_news = {}
    new_news['version'] = new_app['version']
    ew_news['versionDescription'] = input("Enter the version description of the new app: ")
    new_news['date'] = new_app['versionDate']

    # Add new app and news to the beginning of the list
    data['apps'].insert(0, new_app)
    data['apps'][0]['versions'][0]['date'] = new_news['date']
    data['apps'][0]['versions'][0]['localizedDescription'] = new_news['versionDescription'] + '\n' + data['apps'][0]['versions'][0]['localizedDescription']
    data['apps'][0]['versionDate'] = new_news['date']
    data['apps'][0]['versionDescription'] = new_news['versionDescription'] + '\n' + data['apps'][0]['versionDescription']

    # Save the JSON file
    with open(userfile, 'w') as f:
        json.dump(data, f, indent=4)
else:
    print('Invalid input. Please enter either "update" or "add".')
