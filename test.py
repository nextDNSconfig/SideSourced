import datetime
import xml.etree.ElementTree as ET
import json

# Parse XML and JSON
tree = ET.parse('RSS Feed/wuxu-complete.xml')
root = tree.getroot()
with open('wuxu-complete.json') as f:
    data = json.load(f)

# Loop through XML items
for item in root.findall('item'):
    # Get the title of the current item
    title = item.find('title').text
    # Find the corresponding JSON item
    json_item = next((x for x in data if x['title'] == title), None)
    if json_item:
        # Get the date from the JSON item
        date_str = json_item['date']
        # Convert to datetime object
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        # Format as RSS pubDate string
        pubdate_str = date_obj.strftime('%a, %d %b %Y %H:%M:%S GMT')
        # Update the pubDate in the XML item
        pubdate_elem = item.find('pubDate')
        pubdate_elem.text = pubdate_str

# Save the updated XML
tree.write('RSS Feed/wuxu-complete.xml')
