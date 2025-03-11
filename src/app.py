from abletonLivesetParser import parse_ableton_xml


if __name__=="__main__":
    # Example usage:
    xml_file = "myLiveset.xml"  # Change to your actual file path
    json_output = parse_ableton_xml(xml_file)
    print(json_output)
    