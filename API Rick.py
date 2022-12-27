import requests

def get_info(gets):
    url = f'https://rickandmortyapi.com/api/{gets}'
    response = requests.get(url)
    data = response.json()
    return data

def get_location(gets):
    get_id = get_info(f'character/{gets}')
    for i in get_id.keys():
        if i == 'location':
            name_location = get_id['location']['name']
            url_location = get_id['location']['url']
            if url_location not in '':
                id_url = url_location.split('/')[-1]
                location = get_info(f'location/{id_url}')
                name_dimension = location['dimension']
                type_location = location['type']
                information_location = f"""
        Название локации: {name_location}
        Тип локации: {type_location}
        Измерение локации: {name_dimension}"""
                return information_location
            else:
                information_location = f"""
        Название локации: {name_location}
        Тип локации: Unknown
        Измерение локации: Unknown"""
                return information_location

def get_character_info(gets):
    if gets <= 826:
        character = get_info(f'character/{gets}')
        information = f"""
        Идентификатор персонажа: {character['id']}
        Имя персонажа: {character['name']}
        Пол персонажа: {character['gender']}
        Жизненное положение: {character['status']}
        Какой расе относится: {character['species']}
        Личность: {character['type']}
        Дата создание: {character['created']}
        
        {get_location(gets)}
        """

        return information
    return 'Не правильный id персонажа'
print(get_character_info(361))
