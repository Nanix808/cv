<script >
import { ref, computed } from 'vue';
import { useStore } from 'vuex'
import { useRouter, useRoute } from 'vue-router'
import AreaUploader from '@/components/Area.vue';
import TableWithStore from '@/components/Table_with_store.vue';
import ButtonNextPrev from '@/components/ui/ButtonNextPrev.vue';

export default {
  components: {
    AreaUploader,
    TableWithStore,
    ButtonNextPrev
  },

  setup() {

    const store = useStore()
    const router = useRouter()

    const next_page = () => {
        router.push({name: 'second'})
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
    <AreaUploader>
    </AreaUploader> 
    <TableWithStore></TableWithStore>


    <div class="button_container">
    <ButtonNextPrev 
      @clicks="next_page"
      :active = "lengthLoadingTexts"
      :right = true
    > Шаг №2

    </ButtonNextPrev>
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
