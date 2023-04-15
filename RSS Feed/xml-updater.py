import json
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
from datetime import datetime

########################
## WUXU-COMPLETE
########################

try:
    # read the JSON file
    with open('wuxu-complete.json', 'r') as f:
        data = json.load(f)

    # read the XML file
    tree = ET.parse('RSS Feed/wuxu-complete.xml')
    root = tree.getroot()

    # get the current date and time in the desired format
    current_date = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %Z')

    # check if any news item has been updated or added
    updated = False
    for news_item in data['news']:
        # check if the news item is already in the XML file
        item_found = False
        for item in root.findall('channel/item'):
            if item.find('title').text == news_item['title']:
                # check if the pubDate element needs to be updated
                pub_date = item.find('pubDate').text
                item_date = datetime.strptime(news_item['date'], '%Y-%m-%d')
                if pub_date != item_date.strftime('%a, %d %b %Y %H:%M:%S %Z'):
                    item.find('pubDate').text = item_date.strftime('%a, %d %b %Y %H:%M:%S %Z' + 'GMT')
                    updated = True
                    print(f"{news_item['title'].replace('Added!', '').replace('Updated!', '').strip()} pubDate updated in XML file")
                item_found = True
                break
        # if the news item is not in the XML file, add it to the top
        if not item_found:
            item = ET.Element('item')
            title = ET.Element('title')
            title.text = news_item['title']
            item.append(title)
            description = ET.Element('description')
            description.text = news_item['caption']
            item.append(description)
            enclosure = ET.Element('enclosure')
            enclosure.set('url', news_item.get("imageURL", ""))
            enclosure.set('type', 'image/png')
            item.append(enclosure)
            pub_date = datetime.strptime(news_item['date'], '%Y-%m-%d')
            pub_date_element = ET.Element('pubDate')
            pub_date_element.text = pub_date.strftime('%a, %d %b %Y %H:%M:%S %Z')
            item.append(pub_date_element)
            root.find('channel').insert(3, item)
            updated = True
            print(f"{news_item['title'].replace('Added!', '').replace('Updated', '').strip()} added to XML file")

    # if any news item was updated or added, save the XML file
    if updated:
        tree.write('RSS Feed/wuxu-complete.xml')
        ET.indent(tree, space="\t")  # add this line to format the XML
        print("XML file updated")
    else:
        print("No updates or additions made to XML file")

except FileNotFoundError as e:
    print("Error: File not found")
except json.JSONDecodeError as e:
    print("Error: Invalid JSON format")
except ET.ParseError as e:
    print("Error: Invalid XML format")
except Exception as e:
    print("Error:", e)

########################
## WUXU-COMPLETE++
########################

try:
    # read the JSON file
    with open('wuxu-complete-plus.json', 'r') as f:
        data = json.load(f)

    # read the XML file
    tree = ET.parse('RSS Feed/wuxu-complete-plus.xml')
    root = tree.getroot()

    # get the current date and time in the desired format
    current_date = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %Z')

    # check if any news item has been updated or added
    updated = False
    for news_item in data['news']:
        # check if the news item is already in the XML file
        item_found = False
        for item in root.findall('channel/item'):
            if item.find('title').text == news_item['title']:
                # check if the pubDate element needs to be updated
                pub_date = item.find('pubDate').text
                item_date = datetime.strptime(news_item['date'], '%Y-%m-%d')
                if pub_date != item_date.strftime('%a, %d %b %Y %H:%M:%S %Z'):
                    item.find('pubDate').text = item_date.strftime('%a, %d %b %Y %H:%M:%S %Z' + 'GMT')
                    updated = True
                    print(f"{news_item['title'].replace('Added!', '').replace('Updated!', '').strip()} pubDate updated in XML file")
                item_found = True
                break
        # if the news item is not in the XML file, add it to the top
        if not item_found:
            item = ET.Element('item')
            title = ET.Element('title')
            title.text = news_item['title']
            item.append(title)
            description = ET.Element('description')
            description.text = news_item['caption']
            item.append(description)
            enclosure = ET.Element('enclosure')
            enclosure.set('url', news_item.get("imageURL", ""))
            enclosure.set('type', 'image/png')
            item.append(enclosure)
            pub_date = datetime.strptime(news_item['date'], '%Y-%m-%d')
            pub_date_element = ET.Element('pubDate')
            pub_date_element.text = pub_date.strftime('%a, %d %b %Y %H:%M:%S %Z')
            item.append(pub_date_element)
            root.find('channel').insert(3, item)
            updated = True
            print(f"{news_item['title'].replace('Added!', '').replace('Updated', '').strip()} added to XML file")

    # if any news item was updated or added, save the XML file
    if updated:
        tree.write('RSS Feed/wuxu-complete-plus.xml')
        print("XML file updated")
    else:
        print("No updates or additions made to XML file")

except FileNotFoundError as e:
    print("Error: File not found")
except json.JSONDecodeError as e:
    print("Error: Invalid JSON format")
except ET.ParseError as e:
    print("Error: Invalid XML format")
except Exception as e:
    print("Error:", e)
