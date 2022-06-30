<template>
Movie Detail {{$route.params.id}}

{{movie.name}}

{{movie.genres}}

</template>

<script>
export default {
  name: "MovieDetail",
  data() {
    return {
      movie: {}
    }
  },
  async mounted() {
      const res = await fetch(`/api/${this.$route.params.id}`)
      const data = await res.json()
      this.movie = data;
  }
}
</script>

<style scoped>
</style>