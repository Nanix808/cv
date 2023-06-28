<script >
import { useRouter} from 'vue-router'
import ButtonNextPrev from '@/components/ui/ButtonNextPrev.vue';
import { ref } from 'vue'
export default {
  components: {
    ButtonNextPrev
  },

  setup() {
   
    const data = ref({})
    const router = useRouter()

  


    const prev_page = async () => {
        
      const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
             "id": 0,
              "text": "string"
          })
          };
      await fetch("http://127.0.0.1:8000/api/v2/resume", requestOptions)
      .then(async (response) => {
        const data = await response.json()
        console.log("data", data);
        this.data = data
      })
      .catch((error) => {return error})






    }


 

    return { 
      data,  
      prev_page,
    


     };
  },
};
</script>

<template>
  <div>
   <h4>Отправьте запрос на сервер</h4>
 
    <div class="button_container">
    <ButtonNextPrev
    @clicks="prev_page"
      :active = true
      :right = false
    
    >Запрос</ButtonNextPrev>   
   

  </div>

{{ data }}
  </div>
</template>

<style scoped>

.button_container, h4{
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}


</style>
