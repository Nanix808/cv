<script >
import { useRouter} from 'vue-router'
import ButtonNextPrev from '@/components/ui/ButtonNextPrev.vue';
import {UrlApi} from '@/api/index.js';
import { ref, computed } from 'vue'
import { useStore } from 'vuex'

export default {
  components: {
    ButtonNextPrev,
    UrlApi
  },

  setup() {
   
    const data = ref({})
    const router = useRouter()
    const store = useStore()

  
    const prev_page = async () => {
      router.push({name: 'second'})
      }

    
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

    





      // const requestOptions = {
      //       method: "POST",
      //       headers: { "Content-Type": "application/json" },
      //       body: JSON.stringify({
      //        "id": 0,
      //         "text": "string"
      //     })
      //     };
      // await fetch("http://127.0.0.1:8000/api/v2/resume", requestOptions)
      // .then(async (response) => {
      //   const data = await response.json()
      //   console.log("data", data);
      //   this.data = data
      // })
      // .catch((error) => {return error})



    return { 
      data,  
      prev_page,
      post_reqest,
      allLengthTexts: computed(() => store.getters.lengthTexts),
      lengthLoadingTexts: computed(() => store.getters.lengthTexts ? store.getters.getRequestTexts ? true : false : false),
      // lengthRequirements: computed(() => store.getters.lengthRequirements),
      getRequirements: computed(() => store.getters.getRequirements),
      getRequestTexts: computed(() => store.getters.getRequestTexts),


     };
  },
};
</script>

<template>
  <div>
   <h4>Отправьте запрос на сервер и получите ответ</h4>
    <div class="information">
      <p>Загруженно <span>{{ allLengthTexts }}</span> резюме</p>
      <p>Выбраны <span>{{ getRequirements }}</span> требования</p>

    </div>
    
    <div class="button_container">
      <ButtonNextPrev
    @clicks="prev_page"
      :active = true
      :right = false
    
    >Шаг №2</ButtonNextPrev>   
    <ButtonNextPrev
    @clicks="post_reqest"
      :active = lengthLoadingTexts
      :right = true
      :next_icon = true
    
    >Отправить</ButtonNextPrev>   


   

  </div>


  </div>
</template>

<style scoped>

.button_container, h4{
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.information span{
  -webkit-text-fill-color: red;
}


</style>
