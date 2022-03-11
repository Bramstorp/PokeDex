import fetch from 'node-fetch'

export async function onBeforeRender(pageContext) {
  const response = await fetch(`https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151`)
  let pokemon = await response.json()
  pokemonData = pokemon.results

  const pokemonListData = []
  pokemonData.forEach(function (item) {
    pokemonId = item.url.split("/")[6]
    pokemonListData.push(
      {
        "pokemonId": pokemonId, 
        "name": item.name, 
        "img": `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemonId}.png` 
      }
    )
  });
  const pageProps = { pokemonListData }

  return {
    pageContext: {
      pageProps
    }
  }
}

export const passToClient = ['pageProps']