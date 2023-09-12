import { createStore } from 'vuex'

export const store = createStore({
  state: {
    countId: 0,
    texts: [],
    requirements: ''
  },
  getters: {
    lengthTexts(state) {
      return state.texts.length
    },
    lengthRequirements(state) {
      return state.requirements.length > 0 ? true : false
    },
    getAllTexts(state) {
      return state.texts
    },
    getRequirements(state) {
      return state.requirements
    },
    getRequestTexts(state) {

      return state.texts.map((item) => ({ id: item.id, text: item.text }));
    },

  },
  mutations: {
    increment(state) {
      state.countId++
    },
    clear_all(state) {
      state.texts = []
      state.countId = 0
    },
    delText(state, { id }) {
      state.texts.splice(id, 1)
    },
    pushText(state, { id, file_path, text }) {
      state.texts.push({ id, file_path, text })
    },

    pushRequirements(state, text) {
      state.requirements = text
    },

  },
  actions: {
    increment: ({ commit }) => commit('increment'),
    clear: ({ commit }) => commit('clear_all'),
    addtext({ commit }, text) {
      if (text.text.length > 0) {
        text.text = text.text.replace(/(~|`|!|@|#|$|%|^|&|\*|\(|\)|{|}|\[|\]|;|:|\"|'|<|,|\.|>|\?|\/|\\|\||-|_|\+|=|«|»|—|•)/g, ' ')
                         .replace(/\s\s+/g, ' ').toLowerCase();
        commit('increment'),
        commit('pushText', { id: store.state.countId, file_path: text.file_path, text: text.text})
      }
    },
    del_by_id({ commit }, id) {
      commit('delText', { id: id })
    },
    addrequirements({ commit }, text) {
      text = text.value.replace(/(~|`|!|@|#|$|%|^|&|\*|\(|\)|{|}|\[|\]|;|:|\"|'|<|,|\.|>|\?|\/|\\|\||-|_|\+|=|«|»|—|•)/g, ' ')
        .replace(/\s\s+/g, ' ').toLowerCase();
      commit('pushRequirements', text)

    }
  }
});