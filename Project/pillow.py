# import module
import xml.etree.ElementTree as ET
# to read file --> use ET.parse() function in order to create object ElementTree
tree = ET.parse('Shiba.xml')
# Object ElementTree can query elements in file xml by using getroot()
root = tree.getroot()
first_name = root.find('While').text
for name in root.findall('While'):
    print(name.text)


