<script >
import {computed } from 'vue';
import { useStore } from 'vuex'
import { useRouter, useRoute } from 'vue-router'
import ButtonNext from '@/components/ui/button_next.vue';

export default {
  components: {
    ButtonNext
  },

  setup() {

    const store = useStore()
    const router = useRouter()
    const route = useRoute()
  

    const next_page = () => {
      console.log("dddd")
      // pushWithQuery()
    }


 

    return { 
      lengthLoadingTexts: computed(() => store.getters.lengthTexts ? true : false),
      next_page


     };
  },
};
</script>

<template>
  <div>
   

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
