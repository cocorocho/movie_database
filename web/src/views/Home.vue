<template>
  <div>
    <AdvancedSearch/>
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

export default {
    data() {
        return {
            genres: null,
            checkedGenres: [],
            yearValue: [1800, this.getYear()],
            scoreImdb: 7,
            scoreRottenTomatoes: 60,
            movies: []
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
        AdvancedSearch
    },
    beforeMount() {
        this.getGenres()
    },
    mounted() {
      
    },
}
</script>

