import requests
from db import execute_query, create_db_connection
import base64
import urllib.request

pokemons = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1").json()

data = {
    "pokemons" : []
}

def get_as_base64(url):
    data = base64.b64encode(requests.get(url).content).decode()
    return data

for pokemon in pokemons["results"]:
    name = pokemon["name"]
    id = pokemon["url"].split("/")[6]
    pokemonData = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/").json()
    value = [x for x in pokemonData["stats"]]
    imgURL = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'
    urllib.request.urlretrieve(imgURL, "../sprite/", f"{name}_sprite.png")

    pop_pokemon = f"""
    INSERT INTO pokemon VALUES
    ({id},  {pokemonData["height"]}, {pokemonData["weight"]}, {name}, {img}, {value[0]["base_stat"]}, {value[1]["base_stat"]}, {value[2]["base_stat"]}, {value[3]["base_stat"]}, {value[4]["base_stat"]}, {value[5]["base_stat"]}),
    """

    connection = create_db_connection("localhost", "root", "password", "db") 
    #execute_query(connection, pop_pokemon)
    


    """
    data["pokemons"].append({
        "id" : id,
        "height": pokemonData["height"],
        "weight": pokemonData["weight"],
        "name": name,
        "img": f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png',
        "hp": value[0]["base_stat"],
        "attack": value[1]["base_stat"],
        "defense": value[2]["base_stat"],
        "special_attack": value[3]["base_stat"],
        "special_defense": value[4]["base_stat"],
        "speed": value[5]["base_stat"],
    })
    """