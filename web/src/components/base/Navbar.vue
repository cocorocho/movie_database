<template>
    <header>
       	<nav class="bg-gray-800 shadow-md">
			<div class="max-w-6xl mx-auto px-6">
				<div class="flex justify-between">
					<div class="flex space-x-7">
						<div>
							<a href="#" class="flex items-center py-4 px-2">
								<img src="@/assets/video-player.png" alt="Logo" class="h-8 w-8 mr-2">
								<span class="font-semibold text-white text-lg">Movie Database</span>
							</a>
						</div>
						<!-- Primary Navbar items -->
						<div class="hidden md:flex items-center space-x-1">
							<!-- <a href="" class="py-4 px-2 text-green-500 border-b-4 border-green-500 font-semibold ">Home</a>
							<a href="" class="py-4 px-2 text-gray-500 font-semibold hover:text-green-500 transition duration-300">Services</a>
							<a href="" class="py-4 px-2 text-gray-500 font-semibold hover:text-green-500 transition duration-300">About</a>
							<a href="" class="py-4 px-2 text-gray-500 font-semibold hover:text-green-500 transition duration-300">Contact Us</a> -->
						</div>
					</div>
					<!-- Secondary Navbar items -->
					<div class="hidden md:flex items-center space-x-3 ">
						<input v-model="movieName" v-on:keyup="findMovie($event)" type="text" class="rounded-full outline-none px-2 focus:ring-4 focus:ring-green-500 hover:bg-green-100" placeholder="Search Movie">
					</div>
					<!-- Mobile menu button -->
					<div class="md:hidden flex items-center">
                        <button class="outline-none mobile-menu-button" v-on:click="() => {this.$refs.mobileMenu.classList.toggle('hidden')}">
						<svg class=" w-6 h-6 text-gray-500 hover:text-green-500 "
							x-show="!showMenu"
							fill="none"
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path d="M4 6h16M4 12h16M4 18h16"></path>
						</svg>
						</button>
					</div>
				</div>
			</div>
			<!-- mobile menu -->
			<div class="hidden py-5" ref="mobileMenu">
				<ul class="">
                    <input type="text" v-model="movieName" v-on:keyup="findMovie($event)" class="rounded-full outline-none px-2 focus:ring-4 focus:ring-green-500 hover:ring-green-300" placeholder="Search Movie">
					<!-- <li class="active"><a href="index.html" class="block text-sm px-2 py-4 text-white bg-green-500 font-semibold">Home</a></li>
					<li><a href="#services" class="block text-sm px-2 py-4 hover:bg-green-500 transition duration-300">Services</a></li>
					<li><a href="#about" class="block text-sm px-2 py-4 hover:bg-green-500 transition duration-300">About</a></li>
					<li><a href="#contact" class="block text-sm px-2 py-4 hover:bg-green-500 transition duration-300">Contact Us</a></li> -->
				</ul>
			</div>
		</nav>
    </header>
</template>

<script>
import axios from "axios"

export default {
    name: "Navbar",
    data() {
        return {
			movieName: ""
        }        
    },
    setup() {
    },
    methods: {
		async findMovie(e) {
			var vm = this
			const BASEURL = "movies/find/"

			if (e.keyCode === 13) {
				try {
					let response = await axios.get(BASEURL, {params: {movieName: vm.movieName}})
					let movies = response.data

					// Add poster url
					movies.forEach(movie => {
						movie.poster.path = `${axios.defaults.baseURL}${movie.poster.path}`
					})
					vm.$store.commit("addMovie", {obj: movies})
				} catch (error) {
					console.log(error)
					
				}
				vm.movieName = ""
			}
		}
    }
}
</script>