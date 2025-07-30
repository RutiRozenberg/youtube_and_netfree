def get_link_json_data(name, author, duration_or_number_of_parts, language, link, notes):
    return {
        "name": name,
        "author": author,
        "durationOrNumberOfParts": duration_or_number_of_parts,
        "language": language,
        "link": link,
        "notes": notes
    }

def get_table_json_data(title_page, name, author, duration_or_number_of_parts, language, link, notes):
    return {
        "titlePage": title_page,
        "table": [get_link_json_data(name, author, duration_or_number_of_parts, language, link, notes)]
    }