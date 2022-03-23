import os
import requests
from db import execute_query, create_db_connection
import base64
import urllib.request

pokemons = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151").json()

data = {
    "pokemons" : []
}

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

for pokemon in pokemons["results"]:
    name = pokemon["name"]
    id = pokemon["url"].split("/")[6]
    pokemonData = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/").json()
    value = [x for x in pokemonData["stats"]]
    imgURL = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'
    urllib.request.urlretrieve(imgURL,  f"../sprite/{name}_sprite.png")
    
    connection = create_db_connection("localhost", "root", "password", "db")
    cursor = connection.cursor()
    sql_insert_blob_query = """ INSERT INTO pokemon
                        (pokemon_id, height, weight, name, img, hp, attack, defense, speed, special_attack, special_defense) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """

    empPicture = convertToBinaryData(f"../sprite/{name}_sprite.png")

    insert_blob_tuple = (
        id, pokemonData["height"], pokemonData["weight"], name, empPicture,
        value[0]["base_stat"], value[1]["base_stat"], value[2]["base_stat"],
        value[3]["base_stat"], value[4]["base_stat"], value[5]["base_stat"]
    )
    cursor.execute(sql_insert_blob_query, insert_blob_tuple)
    connection.commit()

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