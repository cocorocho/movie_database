<template>
    <div class="container flex py-3 sm:movie-container">
        <a class="mx-auto shadow-xl rounded-md w-12/13" :href="movieUrl">
            <div class="poster-box" @mouseenter="toggle">
                <img :src="poster" ref="posterImage" class="rounded-md poster"
                >
                <div ref="infoBox" class="absolute top-0 info-box w-full h-full p-4" @mouseenter="fadePosterInOut" @mouseleave="fadePosterInOut">
                    <h1>Hello</h1>
                </div>                
            </div>
            <div class="my-auto">
                <h1 class="font-bold font-2xl text-center">{{ name }} ({{ year }})</h1>
            </div>
        </a>
    </div>    
</template>

<style>
.poster-box{
    height: 19rem;
    min-height: 19rem;
    min-width: 200px;
    position: relative;
}
.info-box {
    opacity: 0;
    -webkit-transition: opacity .5s ease-in-out;
    -moz-transition: opacity .5s ease-in-out;
    -ms-transition: opacity .5s ease-in-out;
    -o-transition: opacity .5s ease-in-out;
    transition: opacity .5s ease-in-out;
}
.poster {
    opacity: 1;
    -webkit-transition: opacity .5s ease-in-out;
    -moz-transition: opacity .5s ease-in-out;
    -ms-transition: opacity .5s ease-in-out;
    -o-transition: opacity .5s ease-in-out;
    transition: opacity .5s ease-in-out;
}
.movie-container {
    height: 23rem!important;
}
.movie-container-sm {
    height: 20rem!important;
}
.poster-box img + .info-box:hover {
    opacity: 1;
}
</style>

<script>
export default {
    setup() {
    },
    props: {
        name: {"required":true, type:String},
        movieUrl: {"required":false, type:String},
        poster: {"required":true, type:String},
        year: {"required":true, type:Number}
    },
    data() {
        return {
            posterOpacity: 1
        }
    },
    methods: {
        fadePosterInOut() {
            var poster = this.$refs.posterImage
            this.posterOpacity = (this.posterOpacity === 1) ? 0 : 1;
            poster.style.opacity = this.posterOpacity;
        }
    }
}
</script>

# TODO Poster Scaling
# TODO Movie info tab