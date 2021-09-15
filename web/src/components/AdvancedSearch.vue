<template>
    <div id="advanced-search" class="px-5 py-3 max-w-4xl lg:max-w-7xl mx-auto bg-green">
        <div class="container rounded-md min-w-full border-opacity-50 border-4 border-green-100 bg-green-100 px-5 py-2 space-y-5">
            <div class="grid md:grid-cols-3 md:space-x-6 space-y-3" ref="advancedSearchBox">
                <div class="space-x-2" id="genres">
                    <h1 class="pt-1 font-extrabold text-2xl text-center">Genres</h1>
                    <label class="inline-flex items-center" v-for="genre in genres">
                    <input type="checkbox" class="form-checkbox" :value="genre.name" v-model="checkedGenres">
                    <span class="ml-2 font-semibold">{{ genre.name }}</span>
                    </label>
                </div>
                <div class="text-center">
                    <h1 class="pt-1 pb-8 font-extrabold text-2xl">Release Year</h1>
                    <Slider v-model="yearValue" :min="1800" :max="getYear()" />
                </div>
                <div class="text-center space-y-1">
                    <h1 class="pt-1 pb-1.5 font-extrabold text-2xl">Scores</h1>
                    <label for="score-imdb" class="font-bold">IMDB Score</label>
                    <Slider v-model="scoreImdb" :min="1" :max="10" name="score-imdb"/>
                    <br>
                    <label for="score-imdb" class="font-bold">Rotten Tomates Score</label>
                    <Slider v-model="scoreRottenTomatoes" :min="1" :max="100" name="score-imdb"/>

                    <!-- <label for="score-imdb font-semibold">IMDB Score</label>
                    <Slider v-model="scoreImdb" :min="0" :max="10" name="score-imdb"/> -->

                </div>
            </div>
            <div class="text-center">
                <button class="bg-green-500 hover:bg-grey-800 text-grey-darkest font-bold px-2 py-1 rounded-md inline-flex" v-on:click="findMovies">
                    Advanced Search
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" ref="advancedSearchArrow" id="test">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v3.586L7.707 9.293a1 1 0 00-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 10.586V7z" clip-rule="evenodd" />
                    </svg>
                </button>
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

export default {
    data() {
        return {
            advancedSearchToggle: false,
            genres: null,
            checkedGenres: [],
            yearValue: [1800, this.getYear()],
            scoreImdb: 7,
            scoreRottenTomatoes: 60,
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
                    console.log(this.$store)
                }).catch(function(err) {
                    console.log(err)
                })
        },
    },
    components: {
        Slider,
    },
    beforeMount() {
        this.getGenres()
    },
    mounted() {
      
    },
}
</script>

