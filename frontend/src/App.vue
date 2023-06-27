<script >
import { ref, computed } from 'vue';
import { useStore } from 'vuex'
import { useRouter, useRoute } from 'vue-router'
import AreaUploader from '@/components/Area.vue';
import TableWithStore from '@/components/Table_with_store.vue';
import ButtonNext from '@/components/ui/button_next.vue';

export default {
  components: {
    AreaUploader,
    TableWithStore,
    ButtonNext
  },

  setup() {

    const store = useStore()
    const router = useRouter()
    const route = useRoute()
    function pushWithQuery() {
    
      // router.push({
      //   name: 'search',
  
      // })
    }

    const next_page = () => {
      console.log("dddd")
      // pushWithQuery()
    }

   

    // const getData = async () => {
    //   await fetch("https://api.chucknorris.io/jokes/random", {
    //     method: 'GET' //optional
    // })
    //   .then(async (response) => {
    //     const data = await response.json()
    //     console.log("data", data);
    //     // this.data = data
    //   })
    //   .catch((error) => {return error})
 
    // };

 

    return { 
      lengthLoadingTexts: computed(() => store.getters.lengthTexts ? true : false),
      next_page


     };
  },
};
</script>

<template>
  <div>
    <AreaUploader>
    </AreaUploader>
    <TableWithStore></TableWithStore>


    <div class="button_container">
    <ButtonNext 
      @clicks="next_page"
      :active = "lengthLoadingTexts"
    >

    </ButtonNext>
  </div>


  </div>
</template>

<style scoped>

.button_container{
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}


</style>
