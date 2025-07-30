import sys
import json

from format_json import get_link_json_data

def write_update_data_to_json_file(json_filename, json_data):
    with open(json_filename, 'w') as f:
        json.dump(json_data, f, indent=4)

def add_link_data(json_link_data, json_filename):
    try:
        with open(json_filename, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        json_data = {"table": []}

    json_data["table"].append(json_link_data)
    write_update_data_to_json_file(json_filename, json_data)

if __name__ == "__main__":
    if len(sys.argv) < 7 :
        print("Error: Please provide all arguments:")
        sys.exit(1)

    json_filename = sys.argv[1]
    name = sys.argv[2]
    author = sys.argv[3]
    duration_or_number_of_parts = sys.argv[4]
    language = sys.argv[5]
    link = sys.argv[6]
    notes = sys.argv[7] if len(sys.argv) > 7 else ""
    
    json_link_data =  get_link_json_data(name, author, duration_or_number_of_parts, language, link, notes)

    add_link_data(json_link_data, json_filename)