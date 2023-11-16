
import xml.etree.ElementTree as ET


# Get specified element value from xml
def get_ele_value(xml_path, parent_path, find_tag):
    tree = ET.parse(f'{xml_path}')
    root = tree.getroot()
    path = root.iter(f'{parent_path}')
    for node in path:
        print(node[0].text)
        print(node.find(f'{find_tag}').text)
