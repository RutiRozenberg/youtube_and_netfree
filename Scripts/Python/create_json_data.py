import sys
import json
import os
from format_json import get_table_json_data

def create_json_file(json_file_path, json_data):
    json_file_name = os.path.join(os.path.dirname(__file__), f"..\\..\\{json_file_path}")
    with open(json_file_name, 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"{json_file_name} has been created.")

if __name__ == "__main__":

    if len(sys.argv) < 8 :
        print("Error: Please provide all arguments:")
        sys.exit(1)

    json_file_path = sys.argv[1]
    page_title = sys.argv[2]
    name = sys.argv[3]
    author = sys.argv[4]
    duration_or_number_of_parts = sys.argv[5]
    language = sys.argv[6]
    link = sys.argv[7]
    notes = sys.argv[8] if len(sys.argv) > 8 else ""

    table_json_data = get_table_json_data(page_title, name, author, duration_or_number_of_parts, language, link, notes)
    create_json_file(json_file_path, table_json_data)