import xml.etree.ElementTree as ET
import json

def extract_track_data(track, track_type):
    track_id = track.get("Id", "Unknown")
    track_name_elem = track.find("Name/EffectiveName")
    track_user_name_elem = track.find("Name/UserName")  # Corrected path
    track_color_elem = track.find("Color")
    
    return {
        "Id": track_id if track_id else "Unknown",
        "name": track_name_elem.get("Value", "Unknown") if track_name_elem is not None else "Unknown",
        "user_name": track_user_name_elem.get("Value", "Unknown") if track_user_name_elem is not None else "Unknown",  # Fixed reference
        "color": track_color_elem.get("Value", "Unknown") if track_color_elem is not None else "Unknown",
        "type": track_type,
        "PluginDevices": None,
        "trackContent": {
            "clips": None,
            "takelanes": None,
            "automations": None
        }
    }

def extract_project_data(xml):
    # extrackt bpm data
    tempoXmlElement = xml.find(".//Tempo/Manual")
    project_bpm = int(tempoXmlElement.get("Value", 0)) if tempoXmlElement is not None else 0
    return project_bpm


def extract_ableton_live_version(xml):
    return None # in construction




def parse_ableton_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    projectBPM=extract_project_data(root) 
    abletonLiveVersion = None
    
    project_data = {
        "projectName": "Unknown",
        "projectBPM": projectBPM,
        "abletonVersion":abletonLiveVersion,
        "tracks": []
    }
    
    for track in root.findall(".//MidiTrack"):
        project_data["tracks"].append(extract_track_data(track, "midi"))
    
    for track in root.findall(".//AudioTrack"):
        project_data["tracks"].append(extract_track_data(track, "audio"))
    
    return json.dumps(project_data, indent=4)

if __name__=="__main__":
    # Example usage:
    xml_file = "myLiveset.xml"  # Change to your actual file path
    json_output = parse_ableton_xml(xml_file)
    print(json_output)
