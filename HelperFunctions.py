import re # regular Expression  :

def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""


def get_items(input_list):
    output_string = ", ".join([word.title() for word in input_list])
    return output_string


