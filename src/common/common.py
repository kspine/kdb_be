import xml.etree.cElementTree as ET
import xml.etree.ElementTree as ElementTree

class Common:
    @staticmethod
    def gen_xml_start_stop(action, group_id, comp_type, comp_id):
        root = ET.Element("dip_command")
        command = ET.SubElement(root, "command").text = action

        data = ET.SubElement(root, "command_data")
        ET.SubElement(data, "group").text = group_id
        ET.SubElement(data, "type").text = comp_type
        ET.SubElement(data, "name").text = comp_id

        return ElementTree.tostring(root).decode('utf-8')
