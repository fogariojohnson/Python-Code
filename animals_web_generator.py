import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r') as handle:
        return json.load(handle)


def read_html():
    """Load HTML file"""
    with open("animals_template.html", "r") as file_obj:
        data = file_obj.read()
        return data


def replace_animal_info():
    """Replace and write HTML file"""
    with open("animals.html", "w") as new_file:
        old_data = read_html()
        new_data = animal_info()
        new_content = old_data.replace("__REPLACE_ANIMALS_INFO__", new_data)
        new_file.write(new_content)


def serialize_animal(animal_data):
    """ Structuring the animal data

     No Args:
        list: nested dictionaries

    Returns:
        HTML structure
    """
    output = ' '
    output += f'<li class="cards__item">'
    output += f'<div class="card__title">{animal_data["name"]}</div>\n'
    output += f'<p class="card__text">'
    output += f'<ul style="list-style-type:none;">'
    if 'characteristics' in animal_data and 'diet' in animal_data['characteristics']:
        output += f'<li style="padding: 0.5rem;"><strong> Diet: </strong> {animal_data["characteristics"]["diet"]}\n'
    if 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) > 0:
        output += f'<li style="padding: 0.5rem;"><strong> Location: </strong> {animal_data["locations"][0]}\n'
    if 'characteristics' in animal_data and 'type' in animal_data['characteristics']:
        output += f'<li style="padding: 0.5rem;"><strong> Type: </strong> {animal_data["characteristics"]["type"]}\n'
    if 'characteristics' in animal_data and 'distinctive_feature' in animal_data['characteristics']:
        output += f'<li style="padding: 0.5rem;"><strong> Distinctive Feature: </strong> ' \
                  f'{animal_data["characteristics"]["distinctive_feature"]}<br/>\n'
    if 'characteristics' in animal_data and 'most_distinctive_feature' in animal_data['characteristics']:
        output += f'<li style="padding: 0.5rem;"><strong> Most Distinctive Feature: </strong> ' \
                  f'{animal_data["characteristics"]["most_distinctive_feature"]}<br/>\n'
    if 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) > 1:
        output += f'<li style="padding: 0.5rem;"><strong>Other Locations</strong>'
        output += f'<ul style="list-style-type:square">'
        output += f'<li>{animal_data["locations"][1]}\n'
        if 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) == 3:
            output += f'<li>{animal_data["locations"][2]}\n'
        elif 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) == 4:
            output += f'<li>{animal_data["locations"][2]}\n'
            output += f'<li>{animal_data["locations"][3]}\n'
        elif 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) == 5:
            output += f'<li>{animal_data["locations"][2]}\n'
            output += f'<li>{animal_data["locations"][3]}\n'
            output += f'<li>{animal_data["locations"][4]}\n'
        output += f'</ul>'
    if 'name' in animal_data or ('characteristics' in animal_data and 'diet' in animal_data['characteristics']) \
            or ('locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) > 0)\
            or ('characteristics' in animal_data and 'type' in animal_data['characteristics'])\
            or ('characteristics' in animal_data and 'distinctive_feature' in animal_data['characteristics'])\
            or ('locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) > 1)\
            or ('characteristics' in animal_data and 'most_distinctive_feature' in animal_data['characteristics']):
        output += f'</ul>'
        output += f'</p>'
    output += '</li>'
    return output


def animal_info():
    """ Creates HTML tags

    Returns:
        HTML Structure

    Raises:
        ValueError: If input is not in the list of options
    """
    data = load_data('animals_data.json')
    # Get available skin types
    skin_types = list(set(animal['characteristics']['skin_type'] for animal in data))

    # Display available skin types to user
    counter = 1
    print("Available skin types: ")
    for skin_type in skin_types:
        print(f"{counter}. {skin_type}")
        counter += 1

    # Ask user to select a skin type
    selected_skin_type = None
    while selected_skin_type is None:
        try:
            choice = input("Enter a skin type to display animals with that skin type: ")
            if choice in skin_types:
                selected_skin_type = choice
        except ValueError:
            continue

    # HTML structure
    filtered_animals = [animal for animal in data if animal['characteristics']['skin_type'] == selected_skin_type]
    output = ' '
    for animal_data in filtered_animals:
        output += serialize_animal(animal_data)
    output += f'<label><em><strong>Notes/Comments: <br/></strong> </em></label>'
    output += f'<textarea style="background: linear-gradient(to right, white, pink);" rows="10" cols="75"></textarea>'
    return output


if __name__ == "__main__":
    replace_animal_info()
