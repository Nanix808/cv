<script >
import { useRouter } from 'vue-router'
import ButtonNextPrev from '@/components/ui/ButtonNextPrev.vue';
import { UrlApi } from '@/api/index.js';
import { ref, computed, watch } from 'vue'
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
    const fromArray = ref({})
    const algoritm = ref({})
    const indexButton = ref(0)
    const accuracy = ref([])
    const loader = ref(false);

    const prev_page = async () => {
      router.push({ name: 'second' })
    }

    const sort_array = computed(() => {
      const order = Object.values(fromArray.value)
      let sortarray = store.getters.getAllTexts
      sortarray = sortarray.sort((a, b) => order.indexOf(a.id) - order.indexOf(b.id))
      sortarray.forEach((element, index) => element.accuracy= accuracy.value[index] )
      return sortarray
    });

    watch(data, () => {
      algoritm.value = Object.keys(data.value)
      choiseAlgoritm(0)
    }, { deep: true });


    const choiseAlgoritm = (index) => {
      indexButton.value = index
      fromArray.value = data.value[Object.keys(data.value)[index]].range
      accuracy.value = data.value[Object.keys(data.value)[index]].accuracy
    }


    const post_reqest = async () => {
      loader.value = true
      const body = {
        content: store.getters.getRequestTexts.sort(( a,b ) => a.id - b.id),
        requirements: store.getters.getRequirements
      }
    
    

      return await UrlApi.postResume(body).then((res) => {
       
        data.value = res.data
        console.log(res.data)
        loader.value = false
        return res
      }).catch((error) => {
        loader.value = false
        console.log("Ошибка загрузки данных на сервер", error)
      })
    }

    return {
      data,
      prev_page,
      post_reqest,
      sort_array,
      choiseAlgoritm,
      algoritm,
      fromArray,
      indexButton,
      loader,
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
      <p v-if="getRequirements.length > 0" class="requirement">Посмотреть выбранные требования
      <div class="tooltip">.
        <span class="tooltiptext">{{ getRequirements }}</span>
      </div>
      </p>
    </div>
    <div class="algoritm" v-if="algoritm">
      <button v-for="(items, index) in algoritm" :key="index" :data-index="index"
        :class="indexButton == index ? 'activebuttonalgoritm' : ''" class="buttonalgoritm" @click="choiseAlgoritm(index)">
        {{ items }}
      </button>
    </div>

 
    <TableWithStore v-if="Object.keys(data).length" @clear_all="$store.dispatch('clear')" :texts="sort_array">
   
    </TableWithStore>
  
    <div class="button_container">
      <ButtonNextPrev @clicks="prev_page" :active=true :right=false>Шаг №2</ButtonNextPrev>
      <ButtonNextPrev @clicks="post_reqest" :active=lengthLoadingTexts :right=true :next_icon=true>Отправить
      </ButtonNextPrev>
    </div>
    <div class="loader" v-if="loader"> </div>


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

.requirement {
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


.algoritm {
  display: flex;
  justify-content: center;
  align-items: stretch;
}

.buttonalgoritm {
  flex: 1 0 0px;
  appearance: none;
  backface-visibility: hidden;
  background-color: green;
  border-radius: 8px;
  border-style: none;
  box-shadow: rgba(26, 147, 76, 0.15) 0 4px 9px;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  position: relative;
  margin: 0 15px;
  font-weight: 600;
  letter-spacing: normal;
  line-height: 1.5;
  outline: none;
  overflow: hidden;
  padding: 10px;
  position: relative;
  text-align: center;
  text-decoration: none;
  transform: translate3d(0, 0, 0);
  transition: all .3s;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: top;
  white-space: nowrap;
}
.buttonalgoritm:active,
.activebuttonalgoritm {
  transform: translateY(5px);
  transition-duration: .35s;
  background-color: rgb(23, 142, 64);
}

</style>
