import xml.etree.ElementTree as ET
import datetime
import pytz
import json

# load the JSON data
with open('wuxu-complete copy.json', 'r') as f:
    news_items = json.load(f)['news']

# parse the XML data
tree = ET.parse('RSS Feed/wuxu-complete.xml')
root = tree.getroot()

# create a dictionary of titles and dates from the JSON data
title_to_date = {item['title']: item['date'] for item in news_items}

# loop through the XML items and update their pubDate values
for item in root.iter('item'):
    title = item.find('title').text
    if title in title_to_date:
        date_str = title_to_date[title]
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        date_obj = date_obj.replace(tzinfo=pytz.utc)
        pubdate_str = date_obj.strftime('%a, %d %b %Y %H:%M:%S %Z')
        pubdate = ET.Element('pubDate')
        pubdate.text = pubdate_str
        item.find('pubDate').text = pubdate_str

# write the modified XML back to disk
tree.write('RSS Feed/wuxu-complete.xml')
