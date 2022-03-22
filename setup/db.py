import requests

pokemons = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151").json()


data = {
    "pokemons" : []
}

for pokemon in pokemons["results"]:
    name = pokemon["name"]
    id = pokemon["url"].split("/")[6]
    pokemonData = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/").json()

    data["pokemons"].append({
        "name": name,
        "id" : id,
        "img": f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png',
        "abilityList": [x["ability"]["name"] for x in pokemonData["abilities"]],
        "form": [x["name"] for x in pokemonData["forms"]],
        "height": pokemonData["height"],
        "weight": pokemonData["weight"],
        "types": [x["type"]["name"] for x in pokemonData["types"]],
    })
    
print(data)


