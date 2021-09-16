import { createStore } from 'vuex'

export default createStore({
  state: {
    movies: []
  },
  mutations: {
    addMovie(state, payload) {
      let obj = payload.obj
      let many = payload.many
      console.log(many)
      if (state.movies.length && !many) state.movies = []
      state.movies.push(obj)
      console.log(state.movies)
    }
  },
  actions: {
  },
  modules: {
  }
})
