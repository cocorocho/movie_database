<template>
  <div class="max-w-4xl lg:max-w-7xl mx-auto px-5 py-3 space-y-5">
    <AdvancedSearch/>
    <div id="movie-content">
        <div class="grid grid-cols-1 md:grid-cols-3 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5 2xl:grid-cols-6">
            <MovieCard v-for="movie in movies" 
                :key="movie.name"
                :name="toTitle(movie.name)"
                :movieUrl="movie.url"
                :poster="movie.poster"
                :year="movie.year"
            />
            <MovieCard v-for="movie in movies" 
                :key="movie.name"
                :name="toTitle(movie.name)"
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
        findMovies() {
            let baseUrl = "movies/find/"
            var vm = this
            let args = {
                genres: vm.checkedGenres,
                yearMin: vm.yearValue[0],
                yearMax: vm.yearValue[1],
                scoreImdb: vm.scoreImdb,
                scoreRottenTomatoes: vm.scoreRottenTomatoes
            }
            axios.get(baseUrl, {params: args})
                .then(function(response) {
                    // TODO Advanced Search Request
                }).catch(function(err) {
                    console.log(err)
                })
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

