<script >
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import ButtonNextPrev from '@/components/ui/ButtonNextPrev.vue';

export default {
  components: {
    ButtonNextPrev
  },

  setup() {
    const comment = ref('')
    const store = useStore()
    const router = useRouter()

    onMounted(() => {
      comment.value = store.getters.getRequirements
    })

    const next_page = () => {
      router.push({ name: 'finish' })
      store.dispatch('addrequirements', comment)
    }

    const prev_page = () => {
      router.push({ name: 'first' })
    }

    return {
      lengthLoadingTexts: computed(() => store.getters.lengthTexts ? true : false),
      next_page,
      prev_page,
      comment
    };
  },
};
</script>

<template>
  <div>
    <h4>Введите ключевые слова для поиска во всех резюме</h4>
    <textarea placeholder="Введите ключевые слова..." v-model="comment" class="form-control"></textarea>
    <div class="button_container">
      <ButtonNextPrev @clicks="prev_page" :active=true :right=false>Шаг №1</ButtonNextPrev>
      <ButtonNextPrev @clicks="next_page" :active="lengthLoadingTexts ? comment.length ? true : false : false"
        :right=true>
        Шаг №3</ButtonNextPrev>
    </div>
  </div>
</template>

<style scoped>
.button_container,
h4 {
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

textarea {
  width: 100%;
  height: 50vh;
  max-height: 70vh;
  padding: 12px 20px;
  box-sizing: border-box;
  border: 2px solid #777;
  border-radius: 4px;
  background-color: #f8f8f8;
  font-size: 16px;
  resize: none;
}

textarea:focus {
  outline: none;
  border: 2px solid #008000;
}
</style>
