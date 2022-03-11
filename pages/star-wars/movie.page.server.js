import fetch from 'node-fetch'

export async function onBeforeRender(pageContext) {
  const { movieId } = pageContext.routeParams

  const response = await fetch(`https://swapi.dev/api/films/${movieId}`)
  let movie = await response.json()

  const pageProps = { movie }

  return {
    pageContext: {
      pageProps
    }
  }
}

export const passToClient = ['pageProps']