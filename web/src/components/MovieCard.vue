<template>
    <div class="container flex py-3 sm:movie-container px-1">
        <a class="mx-auto shadow-xl rounded-md w-12/13" :href="movieUrl">
            <div class="poster-box" @mouseenter="toggle">
                <img :src="poster.path" ref="posterImage" class="rounded-md poster"
                >
                <div ref="infoBox" class="absolute top-0 info-box w-full h-full p-4 font-medium" @mouseenter="fadePosterInOut" @mouseleave="fadePosterInOut">
                    <p class="font-bold">Year: <span class="font-medium">{{ year }}</span></p>
                    <p class="font-bold">Language: <span class="font-medium capitalize">{{ language }}</span></p>
                    <p class="font-bold">
                        Genres: 
                        <span class="font-medium" v-for="genre in genres" v-bind="genre">
                            {{ genre.name }}, 
                        </span>
                    </p>
                    <p class="font-bold" v-if="imdb_score">IMDB Score:
                        <span class="font-medium">{{ imdb_score }}</span>
                    </p>
                    <p class="font-bold" v-if="imdb_vote_count">IMDB Vote Count: 
                        <span class="font-medium">{{ imdb_vote_count }}</span>
                    </p>
                    <p class="font-bold" v-if="metacritic_critic_score">Metacritic Score:
                        <span class="font-medium">{{ metacritic_critic_score }}</span>
                    </p>
                    <p class="font-bold" v-if="metacritic_viewer_score">Metacritic Viewer Score:
                        <span class="font-medium">{{ metacritic_viewer_score }}</span>
                    </p>
                    
                    <!-- <p class="font-bold" v-if="metacritic_vote_count">Metacritic Vote Count:
                        <span class="font-medium">{{ metacritic_vote_count }}</span>
                    </p>
                    <p class="font-bold" v-if="metacritic_vote_count_critic">Metacritic Critics Vote Count:
                        <span class="font-medium">{{ metacritic_vote_count_critic }}</span>
                    </p> -->
                    <!-- <p class="font-bold">Description: 
                        <span class="truncate ...">{{ description }}</span>
                    </p> -->

                    
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
    height: 22.5rem;
    min-height: 22.5rem;
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
    background-color: rgba(130, 240, 50, 0.2);
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
        year: {"required":true, type:Number},
        description: {"required": false, type:String},
        genres: {"required":false, type:String},
        language: {"required":false, type:String},
        imdb_score: {"required":false, type:Number},
        imdb_vote_count: {"required": false, type:String},
        rottentomatoes_viewer_score: {"required":false, type:String},
        rottentomatoes_critic_score: {"required":false, type:String},
        metacritic_viewer_score: {"required":false, type:String},
        metacritic_critic_score: {"required":false, type:Number},
        metacritic_vote_count_viewer: {"required":false, type:String},
        metacritic_vote_count_critic: {"required":false, type:String},
    },
    data() {
        return {
            posterOpacity: 1
        }
    },
    methods: {
        fadePosterInOut() {
            var poster = this.$refs.posterImage
            this.posterOpacity = (this.posterOpacity === 1) ? 0.15 : 1;
            poster.style.opacity = this.posterOpacity;
        }
    }
}
</script>

# TODO Poster Scaling
# TODO Movie info tab