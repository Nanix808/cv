import { createStore } from 'vuex'

export const store = createStore({
  state: {
    countId: 0,
    texts: []
  },
  getters: {
    lengthTexts (state) {
      return state.texts.length
    },
    getAllTexts (state) {
      return state.texts
    }
  },
  mutations: {
    increment(state) {
      state.countId++
    },
    delText(state,{id}) {
      state.texts.splice(id, 1)
    },
    pushText(state, { id, file_path, text}) {
      state.texts.push({id, file_path, text})
    },
  
  },
  actions: {
    increment: ({ commit }) => commit('increment'),
    addtext ({ commit }, text) {
      if (text.text.length > 0) {
          commit('increment'),
          commit('pushText', { id: store.state.countId,file_path: text.file_path, text: text.text})
      }
    },
    del_by_id({ commit }, id){
      commit('delText', { id: id })
    }
  }
});