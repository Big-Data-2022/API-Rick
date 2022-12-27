
import requests

def get_info(gets):
    url = f'https://rickandmortyapi.com/api/{gets}'
    response = requests.get(url)
    data = response.json()
    return data

def get_episode(gets):
    get_id_episodes = get_info(f'character/{gets}')
    for i in get_id_episodes['episode']:
        response = requests.get(i)
        episode = response.json()
        information_episode = f'''
    Эпизод где участвует персонаж 
        Название эпизода: {episode['name']}
        Дата релиза: {episode['air_date']}
        Эпизод: {episode['episode']}

        '''
        return information_episode




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
        Дата создания: {character['created']}
        Эпизоды где есть персонаж: {' ' .join(character['episode']) .center(10)}
       
        """
        return information
    return 'Не правильный id персонажа'
character = int(input('Введите id персонажа: '))
print(get_character_info(character))
    