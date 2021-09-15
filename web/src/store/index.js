import { createStore } from 'vuex'

export default createStore({
  state: {
    movies: []
  },
  mutations: {
    addMovie(state, obj) {
      if (state.movies.length) state.movies = []
      state.movies.push(obj)
    }
  },
  actions: {
  },
  modules: {
  }
})
