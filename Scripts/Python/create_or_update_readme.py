import sys
import json
import os

def create_readme(readme_path, template):
    readme_filename = os.path.join(os.path.dirname(__file__), f"..\\..\\{readme_path}")
    with open(readme_filename, 'w', encoding='utf-8') as f:
        f.write(template)
    print(f"{readme_filename} has been created.")

def main():
    json_file_path = sys.argv[1]
    readme_path = sys.argv[2]

    with open(json_file_path, 'r') as f:
        json_data = json.load(f)

    table_data = json_data['table']
    
    table_template = ''
    for column_data in table_data:
        table_template += f'''<tr>
            <td style="text-align: right;">{column_data.get('name', '')}</td>
            <td style="text-align: right;">{column_data.get('author', '')}</td>
            <td style="text-align: right;">{column_data.get('durationOrNumberOfParts', '')}</td>
            <td style="text-align: right;">{column_data.get('language', '')}</td>
            <td style="text-align: right;">
                <a href="{column_data.get('link', '')}">{column_data.get('link', '')}</a>
            </td>
            <td style="text-align: right;">{column_data.get('notes', '')}</td>
        </tr>'''

    template = f'''<div dir="rtl">
        <h1>{json_data.get('title_page', '')}</h1>
        <table>
            <tr>
                <th style="text-align: right;">שם</th>
                <th style="text-align: right;">מחבר</th>
                <th style="text-align: right;">משך הזמן/מס' חלקים</th>
                <th style="text-align: right;">שפה</th>
                <th style="text-align: right;">קישור</th>
                <th style="text-align: right;">הערות</th>
            </tr>
            {table_template}
        <table>
    </div>'''

    create_readme(readme_path, template)

if __name__ == "__main__":
    main()