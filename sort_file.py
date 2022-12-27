import requests

def get_info(gets):
    url = f'https://rickandmortyapi.com/api/{gets}'
    response = requests.get(url)
    data = response.json()
    return data


def get_character_info(gets):
    if gets <= 826:
        character = get_info(f'character/{gets}')
        edit_sylka = character['location']['url']
        if edit_sylka is not None:
            id_locations = edit_sylka.split('/')[-1]
            location = get_info(f'location/{id_locations}')
            information = f"""
            Идентификатор персонажа: {character['id']}
            Имя персонажа: {character['name']}
            Пол персонажа: {character['gender']}
            Жизненное положение: {character['status']}
            Какой расе относится: {character['species']}
            Личность: {character['type']}
            Имя локации: {character['location']['name']}
            Тип локации: {location['type']}
            Измерения: {location['dimension']}
            Дата создание: {character['created']}
            """
            return information
        elif edit_sylka is None:
            information = f"""
            Идентификатор персонажа: {character['id']}
            Имя персонажа: {character['name']}
            Пол персонажа: {character['gender']}
            Жизненное положение: {character['status']}
            Какой расе относится: {character['species']}
            Личность: {character['type']}
            Имя локации: {character['location']['name']}
            Тип локации: Unknown
            Измерения: Unknown
            Дата создание: {character['created']}
            """
            return information
        return 'Не правильный id персонажа'
print(get_character_info(900))