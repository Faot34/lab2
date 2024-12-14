import xml.etree.ElementTree as ET

def extract_charcode_and_value(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    charcode_list = []
    value_list = []
    
    for elem in root.iter():
        if elem.tag == "CharCode":  
            charcode_list.append(elem.text)
        elif elem.tag == "Value":  
            value_list.append(elem.text)
    
    return charcode_list, value_list


charcodes, values = extract_charcode_and_value('currency.xml')


print("CharCode List:", charcodes)
print("Value List:", values)
