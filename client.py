# Client

import requests
from models.stats import Stats


# Calling API (server) from the client
def call_api_service():
    print("1.) Stats Only\n2.) Armor Only\n3.) Full Build\n4.) View Saved Builds\n5.) Exit\n")
    option = int(input("PLease select an option: "))
    while option != 5:
        match option:
            case 1:
                starting_class = input('Input starting class name (i.e. Hero, Astrologer, etc): ')
                requested_build = input('Input the build you would like to focus on (i.e. strength, magic, arcane, etc.): ')
                stats_only(starting_class, requested_build)
            case 2:
                requested_build = input('Input the build you need armor for (i.e. strength, magic, arcane, etc): ')
                armor_only(requested_build)
            case 3:
                starting_class = input('Input starting class name (i.e. Hero, Astrologer, etc): ')
                requested_build = input('Input the build you would like to focus on (i.e. strength, magic, arcane, etc): ')
                full_build(starting_class, requested_build)
            case 4:
                print_saved_builds()
            case _:
                print("Error: Invalid Option Given.")

        print("1.) Stats Only\n2.) Armor Only\n3.) Full Build\n4.) View Saved Builds\n5.) Exit\n")
        option = int(input("Please enter an option: "))

    print("Goodbye!")


# Connects th e client to the API to get the stats of a Character and its class./
def get_game_character(stats: Stats) -> None:
    api_url: str = 'http://127.0.0.1:40000/api/character'
    # print(f'\nURL: {api_url}')

    results = requests.post(api_url, json=stats.model_dump())

    if results.status_code == 200:
        try:
            ch = results.json()
            print(f"""
At level {ch['Level']} your stats should look like this:
Vigor: {ch['Vigor']}
Mind: {ch['Mind']}
Endurance: {ch['Endurance']}
Strength: {ch['Strength']}
Dexterity: {ch['Dexterity']}
Intelligence: {ch['Intelligence']}
Faith: {ch['Faith']}
Arcane: {ch['Arcane']}
Remaining Points: {ch['Remaining']} {'(Put them in any stat you want)' if int(ch['Remaining']) > 0 else ''}
            """)
        except requests.exceptions.JSONDecodeError:
            print(results.text)
    else:
        print(f'Status Code: {results.status_code} | Error Message: {results.text}')


# Connects the client to the API to get the armor
def get_armor(stats: Stats) -> None:
    api_url: str = 'http://127.0.0.1:40000/api/armor'

    results = requests.post(api_url, json=stats.model_dump())

    if results.status_code == 200:
        try:
            armor = results.json()
            print(f"""
Helmet: {armor['helmet']}
Chestpiece: {armor['chestpiece']}
Gauntlet: {armor['gauntlet']}
Legs: {armor['legs']}
""")

        except requests.exceptions.JSONDecodeError:
            print(results.text)
    else:
        print(f'Status Code: {results.status_code} | Error Message: {results.text}')


# Connects the client to the API to get the full build
def get_full_build(stats: Stats) -> None:
    api_url: str = 'http://127.0.0.1:40000/api/full-build'

    results = requests.post(api_url, json=stats.model_dump())


    if results.status_code == 200:
        try:
            ch = results.json()
            print(f"""
At level {ch['Level']} your stats should look like this:
Vigor: {ch['Vigor']}
Mind: {ch['Mind']}
Endurance: {ch['Endurance']}
Strength: {ch['Strength']}
Dexterity: {ch['Dexterity']}
Intelligence: {ch['Intelligence']}
Faith: {ch['Faith']}
Arcane: {ch['Arcane']}
Remaining Points: {ch['Remaining']} {'(Put them in any stat you want)' if int(ch['Remaining']) > 0 else ''}
            
Helmet: {ch['Helmet']}
Chestpiece: {ch['Chestpiece']}
Gauntlet: {ch['Gauntlet']}
Legs: {ch['Legs']}
            """)
        except requests.exceptions.JSONDecodeError:
            print(results.text)
    else:
        print(f'Status Code: {results.status_code} | Error Message: {results.text}')


# Option 1: only character data
def stats_only(requested_class: str, requested_build: str):
    char_request = Stats(build_type=requested_build, class_name=requested_class, save_build_name='')
    get_game_character(char_request)


# Option 2: only the armor data
def armor_only(requested_build: str):
    char_request = Stats(build_type=requested_build, class_name='', save_build_name='')
    get_armor(char_request)


# Option 3: Both character and armor data
def full_build(requested_class: str, requested_build: str) -> None:
    option = input('Would you like to eventually save this build? (y/n)')
    if option == 'y' or option == 'yes' or option == 'Y' or option == 'Yes':
        build_name = input('Name the build you want to save it as: ')
        char_request = Stats(build_type=requested_build, class_name=requested_class, save_build_name=build_name)
        get_full_build(char_request)
    elif option == 'n' or option == 'no' or option == 'N' or option == 'No':
        char_request = Stats(build_type=requested_build, class_name=requested_class, save_build_name='')
        get_full_build(char_request)
    else:
        print('Error: Incorrect Answer')


# Calls the API to print the saved builds from the database
def print_saved_builds():
    api_url: str = 'http://127.0.0.1:40000/api/builds'
    # print(f'\nURL: {api_url}')

    results = requests.get(api_url)

    if results.status_code == 200:
        try:
            for result in results.json():
                print(result)
        except requests.exceptions.JSONDecodeError:
            print(results.text)
    else:
        print(f'Status Code: {results.status_code} | Error Message: {results.text}')


if __name__ == '__main__':
    api_flag = input("Is the api service running? (y/n)")

    # Checking the api service
    if api_flag == 'yes' or api_flag == 'Y' or api_flag == 'Yes' or api_flag == 'y':
        # Calls function to connect to server
        call_api_service()

    else:
        print("Please make sure 'API_service.py' is running before you run the client.")