import { createStore, storeKey } from 'vuex'

export default createStore({
  state: {
    movies: []
  },
  mutations: {
    addMovie(state, payload) {
      let obj = payload.obj
      let many = payload.many
      if (state.movies.length && !many) {
        for (let i=0; i < state.movies.length; i++) {
          state.movies.pop()
        }
      }
      state.movies.push(obj)
    },
    resetMovies(state) {
      state.movies.splice(0);
    }
  },
  actions: {
  },
  modules: {
  }
})
