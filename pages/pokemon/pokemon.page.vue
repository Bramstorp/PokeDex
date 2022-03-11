<template>
  <div class="container mx-auto pt-4">
      <PokemonSearch />
      <PokemonList :pokemonListData="pokemonListData"  />
  </div>
</template>

<script>
import PokemonSearch from './components/PokemonSearch.vue'
import PokemonList from './components/PokemonList.vue'
const pageProps = ['pokemonListData']

export default { components: { PokemonSearch, PokemonList }, props: pageProps }

</script>


