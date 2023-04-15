import json
import xml.etree.ElementTree as ET
import datetime

# Load the JSON file
with open('wuxu-complete.json') as f:
    data = json.load(f)

# Load the XML file
tree = ET.parse('RSS Feed/wuxu-complete.xml')
root = tree.getroot()

# Check for updates in the news section
for news_item in data['news']:
    # Get the date of the news item
    news_date = datetime.datetime.strptime(news_item['date'], '%Y-%m-%d').date()
    # Check if the news item is already in the XML file
    news_item_exists = False
    for item in root.findall('NewsItem'):
        if item.attrib['title'] == news_item['title']:
            # Check if the date of the news item has been updated
            item_date = datetime.datetime.strptime(item.attrib['date'], '%Y-%m-%d').date()
            if news_date > item_date:
                # Update the date of the news item in the XML file
                item.attrib['date'] = news_item['date']
            news_item_exists = True
            break
    # Add the news item to the XML file if it doesn't exist
    if not news_item_exists:
        new_item = ET.SubElement(root, 'NewsItem', title=news_item['title'], caption=news_item['caption'], date=news_item['date'])
        if 'tintColor' in news_item:
            new_item.attrib['tintColor'] = news_item['tintColor']
        if 'imageURL' in news_item:
            new_item.attrib['imageURL'] = news_item['imageURL']
        if 'appID' in news_item:
            new_item.attrib['appID'] = news_item['appID']
        if 'notify' in news_item:
            new_item.attrib['notify'] = str(news_item['notify'])

# Save the updated XML file
tree.write('wuxu-complete.xml')
