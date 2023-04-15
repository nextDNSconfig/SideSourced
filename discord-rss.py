import json
import xml.etree.ElementTree as ET

# Load the JSON file
with open('wuxu-complete.json') as f:
    data = json.load(f)

# Load the XML file
tree = ET.parse('wuxu-complete.xml')
root = tree.getroot()

# Find the News section in the XML file
news_section = root.find('News')

# Initialize a list of changes
changes = []

# Check for new or modified news items
for news in data['news']:
    # Find the News element in the XML file with the same identifier
    news_element = news_section.find(f"News[@identifier='{news['identifier']}']")
    if news_element is None:
        # If the News element doesn't exist, it is a new item
        changes.append(news)
    elif news_element.attrib['date'] != news['date']:
        # If the News element exists but the date has been modified, update it
        news_element.attrib['date'] = news['date']
        changes.append(news)

# Update the XML file with any changes
for news in changes:
    if news_section.find(f"News[@identifier='{news['identifier']}']") is None:
        # Add a new News element for new items
        news_element = ET.SubElement(news_section, 'News', {
            'title': news['title'],
            'identifier': news['identifier'],
            'caption': news['caption'],
            'tintColor': news['tintColor'],
            'imageURL': news['imageURL'],
            'appID': news['appID'],
            'date': news['date'],
            'notify': str(news['notify']).lower()
        })
    else:
        # Update the date attribute for modified items
        news_element.attrib['date'] = news['date']

# Write the updated XML file
tree.write('wuxu-complete.xml')
