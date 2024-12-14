import xml.etree.ElementTree as ET

def unique_tags(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    tags = set()
    for elem in root.iter():
        tags.add(elem.tag)
    
    return sorted(tags)

tags = unique_tags('currency.xml')
print("Уникальные XML теги:")
for tag in tags:
    print(tag)
