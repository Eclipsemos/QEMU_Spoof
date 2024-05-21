import xml.etree.ElementTree as ET
import random
import string
from xml.dom import minidom

def generate_random_string(length=10):
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def generate_xml():
    root = ET.Element("sysinfo", type="smbios")

    bios = ET.SubElement(root, "bios")
    ET.SubElement(bios, "entry", name="vendor").text = random.choice(["Microsoft","HP","Apple","Dell","Asus","Acer", "MSI", "Toshiba","Sony","Fujitsu"])

    system = ET.SubElement(root, "system")
    manufacturer_name = random.choice(["Microsoft","HP","Apple","Dell","Asus","Acer", "MSI", "Toshiba","Sony","Fujitsu"])
    ET.SubElement(system, "entry", name="manufacturer").text = manufacturer_name
    product_name = random.choice(["Windows10", "Windows11"])
    ET.SubElement(system, "entry", name="product").text = product_name
    ET.SubElement(system, "entry", name="version").text = random.choice(["22H2", "20H2"])

    baseBoard = ET.SubElement(root, "baseBoard")
    ET.SubElement(baseBoard, "entry", name="manufacturer").text = random.choice(["Microsoft","HP","Apple","Dell","Asus","Acer", "MSI", "Toshiba","Sony","Fujitsu"])
    ET.SubElement(baseBoard, "entry", name="product").text = random.choice(["Microsoft","HP","Apple","Dell","Asus","Acer", "MSI", "Toshiba","Sony","Fujitsu"])
    ET.SubElement(baseBoard, "entry", name="version").text = generate_random_string()
    ET.SubElement(baseBoard, "entry", name="serial").text = generate_random_string()

    chassis = ET.SubElement(root, "chassis")
    ET.SubElement(chassis, "entry", name="manufacturer").text = random.choice(["Microsoft","HP","Apple","Dell","Asus","Acer", "MSI", "Toshiba","Sony","Fujitsu"])
    ET.SubElement(chassis, "entry", name="version").text = generate_random_string()
    ET.SubElement(chassis, "entry", name="serial").text = generate_random_string()
    ET.SubElement(chassis, "entry", name="asset").text = generate_random_string()
    ET.SubElement(chassis, "entry", name="sku").text = generate_random_string()

    oemStrings = ET.SubElement(root, "oemStrings")
    ET.SubElement(oemStrings, "entry").text = "myappname:some arbitrary data"
    ET.SubElement(oemStrings, "entry").text = "otherappname:more arbitrary data"

    # Generate the XML string
    xml_str = ET.tostring(root, encoding="utf-8")
    
    # Pretty print the XML string
    parsed_str = minidom.parseString(xml_str)
    pretty_xml_str = parsed_str.toprettyxml(indent="    ")

    with open("sysinfo.xml", "w", encoding="utf-8") as f:
        f.write(pretty_xml_str)

generate_xml()
