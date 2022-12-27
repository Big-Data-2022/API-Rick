import requests

#API - aplication protocol information

def get_info(gets):
    url = f'https://rickandmortyapi.com/api/{gets}' 
    response = requests.get(url)
    data = response.json()
    return data

def get_location(gets):
    get_id = get_info(f'character/{gets}')
    for i in get_id.keys():
        if i == 'location':
            location_name = get_id['location']['name'] 
            location_url = get_id['location']['url']
            if location_url not in '':
                location_id = location_url.split('/')[-1]
                location = get_info(f'location/{location_id}')
                dimension_name = location['dimension']
                location_type = location['type']
                location_info = f'''
                Название локации: {location_name}
                Тип локации: {location_type}
                Измерение: {dimension_name}
                '''
            else:               
                location_info = f'''
                Название локации: {location_name}
                Тип локации: Unknown
                Измерение: Unknown
                '''
    return location_info



def get_episode(gets):
    get_id = get_info(f'character/{gets}')
    for i in get_id.keys():
        if i == 'episode':
            episode_url = get_id['url']
            episode_id = episode_url.split('/')[-1]
            episode = get_info(f'episode/{episode_id}')
            episode_name =episode['name']
            episode_number = episode['episode']
            episode_date = episode['air_date']
            episode_info = f'''
                Название серии: {episode_name}
                Номер серии и сезона: {episode_number}
                Дата выхода: {episode_date}
                '''
    return episode_info



def get_character_info(gets):
    if gets <= 826:
        character = get_info(f'character/{gets}')
        information = f"""
            Идентификатор персонажа: {character['id']}
            Имя персонажа: {character['name']}
            Пол персонажа: {character['gender']}
            Вид: {character['species']}
            Статус: {character['status']}
            Личность: {character['type']}
            Дата создания: {character['created']}
            {get_location(gets)}
            {get_episode(gets)}
            """
        return information
    return 'Не правильный id персонажа'

print(get_character_info(19))
