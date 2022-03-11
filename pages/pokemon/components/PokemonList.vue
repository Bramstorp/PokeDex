<template>
  <div class="flex flex-wrap">
    <div class="bg-teal-500 m-2 p-4 rounded-md" v-for="pokemon in pokemonListData" :key="pokemon.id">
        <p class="text-white">{{ pokemon.pokemonId }}</p>
        <p class="text-white">{{ pokemon.name }}</p>
        <img :src="pokemon.img" width="96" height="96" alt="">
    </div>
  </div>
</template>

<script>
  export default {
    props: [
      'pokemonListData',
    ],
    data: () => {
      return {
        pokemonListData: [],
      }
    },
  }
</script>