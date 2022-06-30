<template>

    <div class="row">
        <div class="col" v-for="movie in movies">
          <div class="card" style="width: 18rem;">
              <img src="..." class="card-img-top" alt="...">
              <div class="card-body">
              <h5 class="card-title">{{movie.name}}</h5>
              <p class="card-text">{{movie.genres}}</p>
              <a :href="`/movie/${movie.id}/`" class="btn btn-primary">More</a>
              </div>
          </div>
        </div>
    </div>


</template>

<script>
export default {
  name: "MoviesList",
  data() {
    return {
      movies: [
      ],
      nextLink: null,
      previousLink: null,
      pageNo: null
    }
  },
  async mounted() {
    await this.fetchMovies()
  },
  methods: {
    async fetchMovies(url) {
      const targetUrl = url ? url : '/api/'
      const res = await fetch(targetUrl)
      const data = await res.json()
      this.movies = data;
      this.nextLink = data["next"]
      this.previousLink = data["previous"]
    },
    async addMovie(url) {
      await fetch('/api/', {
        'method': 'POST',
        'data': {
        }
      } )
    }
  }
}
</script>

<style scoped>
</style>