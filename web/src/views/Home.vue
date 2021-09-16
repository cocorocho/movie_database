<template>
  <div class="max-w-4xl lg:max-w-7xl mx-auto px-5 py-3 space-y-5">
    <AdvancedSearch/>
    <div id="movie-content">
        <div class="grid grid-cols-1 md:grid-cols-3 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6">
            <MovieCard v-for="movie in movies" 
                :key="movie.id"
                :name="toTitle(movie.name)"
                :movieUrl="movie.url"
                :poster="movie.poster"
                :year="movie.year"
            />
        </div>        
    </div>
  </div>
</template>

// https://bestofvue.com/repo/vueform-slider-vuejs-slider#multiple-slider

<style src="@vueform/slider/themes/default.css">
#grow {
    -moz-transition: height .5s;
    -ms-transition: height .5s;
    -o-transition: height .5s;
    -webkit-transition: height .5s;
    transition: height .5s;
    height: 0;
    overflow: hidden;
}
</style>

<script>
import axios from "axios"
import Slider from '@vueform/slider'
import AdvancedSearch from "@/components/AdvancedSearch"
import MovieCard from "@/components/MovieCard"

export default {
    data() {
        return {
            genres: null,
            checkedGenres: [],
            yearValue: [1800, this.getYear()],
            scoreImdb: 7,
            scoreRottenTomatoes: 60,
            movies: this.$store.state.movies
        }
    },
    methods: {
        rotateSvg(elem) {
            const ROTATE_X = (!this.advancedSearchToggle) ? 0 : 270
            this.advancedSearchToggle = !this.advancedSearchToggle
            elem.setAttribute("transform", "rotate(" + ROTATE_X + ")")
        },
        getGenres() {
            let baseUrl = "movies/genres/"
            var vm = this
            axios
                .get(baseUrl)
                .then(function(response) {
                    vm.genres = response.data
                })
        },
        getYear() {
            let date = new Date
            let year = date.getFullYear()
            return year
        },
        toTitle(string) {
            let str = string[0].toUpperCase() + string.slice(1)
            return str
        },
    },
    components: {
        Slider,
        AdvancedSearch,
        MovieCard
    },
    beforeMount() {
        this.getGenres()
    },
    mounted() {
    },
}
</script>
