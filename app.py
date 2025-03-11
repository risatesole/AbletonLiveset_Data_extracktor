import xml.etree.ElementTree as xmlParser
import json

def extract_track_data(track, track_type):
    track_id = track.get("Id", "Unknown")
    track_name_elem = track.find("Name/EffectiveName")
    track_color_elem = track.find("Color")
    
    return {
        "Id": track_id if track_id else "Unknown",
        "name": track_name_elem.get("Value", "Unknown") if track_name_elem is not None else "Unknown",
        "color": track_color_elem.get("Value", "Unknown") if track_color_elem is not None else "Unknown",
        "type": track_type,
        "PluginDevices": {},
        "trackContent": {
            "clips": {},
            "takelanes": {},
            "automations": {}
        }
    }

def parse_ableton_xml(xml_file):
    tree = xmlParser.parse(xml_file)
    root = tree.getroot()
    
    project_data = {
        "projectName": "Unknown",
        "projectBPM": 0,
        "tracks": []
    }
    
    for track in root.findall(".//MidiTrack"):
        project_data["tracks"].append(extract_track_data(track, "midi"))
    
    for track in root.findall(".//AudioTrack"):
        project_data["tracks"].append(extract_track_data(track, "audio"))
    
    return json.dumps(project_data, indent=4)

# Example usage:
xml_file = "liveset.xml"  # Change to your actual file path
json_output = parse_ableton_xml(xml_file)
print(json_output)
