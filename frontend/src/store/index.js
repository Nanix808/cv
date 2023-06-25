import { createStore } from 'vuex'

export const store = createStore({
  state: {
    count: 0,
    texts: []
  },
  mutations: {
    increment(state) {
      state.count++
    },
    decrement(state) {
      state.count--
    },
    pushText(state, { id, file_path, text}) {
      state.texts.push({
        id,
        file_path,
        text
     
      })
    },
  
  },
  actions: {
    increment: ({ commit }) => commit('increment'),
    decrement: ({ commit }) => commit('decrement'),
    addtext ({ state, commit }, text) {
      if (text.text.length > 0) {
          commit('pushText', { id: text.id,file_path: text.file_path, text: text.text})
      }
    }
  }
});