import { createStore, storeKey } from 'vuex'

export default createStore({
  state: {
    movies: []
  },
  mutations: {
    addMovie(state, payload) {
      let obj = payload.obj
      this.commit("resetMovies")
      obj.forEach(movie => {
        state.movies.push(movie)
      });
    },
    resetMovies(state) {
      state.movies.splice(0);
    }
  },
  getters: {
    getMovies(state) {
      return state.movies
    }
  },
  actions: {
  },
  modules: {
  }
})
