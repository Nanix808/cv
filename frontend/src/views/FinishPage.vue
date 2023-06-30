<script >
import { useRouter } from 'vue-router'
import ButtonNextPrev from '@/components/ui/ButtonNextPrev.vue';
import { UrlApi } from '@/api/index.js';
import { ref, computed } from 'vue'
import { useStore } from 'vuex'
import TableWithStore from '@/components/Table_with_store.vue';

export default {
  components: {
    ButtonNextPrev,
    UrlApi,
    TableWithStore,
  },

  setup() {
    const data = ref({})
    const router = useRouter()
    const store = useStore()

    const prev_page = async () => {
      router.push({ name: 'second' })
    }

    const sort_array = computed(() => {
      const order = Object.values(data.value);
      return store.getters.getAllTexts.sort((a, b) => order.indexOf(a.id) - order.indexOf(b.id))
    })


    const post_reqest = async () => {
      const body = {
        content: store.getters.getRequestTexts,
        requirements: store.getters.getRequirements
      }
      return await UrlApi.postResume(body).then((res) => {
        data.value = res.data
        return res
      }).catch((error) => {
        console.log("Ошибка загрузки данных на сервер", error)
      })
    }

    return {
      data,
      prev_page,
      post_reqest,
      sort_array,
      allLengthTexts: computed(() => store.getters.lengthTexts),
      lengthLoadingTexts: computed(() => store.getters.lengthTexts ? store.getters.getRequestTexts ? true : false : false),
      getRequirements: computed(() => store.getters.getRequirements),
    
    };
  },
};
</script>

<template>
  <div>
    <h3>Отправьте запрос на сервер</h3>
    <div class="info">
      <p>Загруженно <span>{{ allLengthTexts }}</span> резюме</p>
      <p 
      v-if="getRequirements.length>0"
      class="requirement">Посмотреть выбранные требования <div class="tooltip">.
        <span class="tooltiptext">{{ getRequirements }}</span></div> </p>
    </div>
    <TableWithStore v-if="data.length" @clear_all="$store.dispatch('clear')" :texts="sort_array"></TableWithStore>
    <div class="button_container">
      <ButtonNextPrev @clicks="prev_page" :active=true :right=false>Шаг №2</ButtonNextPrev>
      <ButtonNextPrev @clicks="post_reqest" :active=lengthLoadingTexts :right=true :next_icon=true>Отправить
      </ButtonNextPrev>
    </div>
  </div>
</template>

<style scoped>
.button_container,
h3 {
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.requirement{
  display: flex;
  align-items: center;


}
.tooltip {
    margin-left: 5px;
    position: relative;
    display: inline-block;
    width: 20px;
    height: 20px;
    background-size: cover;
    background: url(../src/assets/images/question.svg);
  
   
}
.tooltip .tooltiptext {
    visibility: hidden;
    max-width: 60vw;
    width: max-content;
    background-color: #fbfafa;
    color: black;
    text-align: center;
    border: 4px dotted #eee;
    border-radius: 15px;
    padding: 10px;
    top: 20px;
    left: 5px;
    position: absolute;
    z-index: 15;
}
.tooltip:hover .tooltiptext {
    visibility: visible;
}
</style>
