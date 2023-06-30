<script >
import { computed } from 'vue';
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
      router.push({ name: 'second' })
    }

    const del_by_id = (id) => {


      store.dispatch('del_by_id', id)

    };

    return {
      lengthLoadingTexts: computed(() => store.getters.lengthTexts ? true : false),
      allTexts: computed(() => store.getters.getAllTexts),
      next_page,
      del_by_id


    };
  },
};
</script>

<template>
  <div>
    <AreaUploader>
    </AreaUploader>
    <TableWithStore
     @del_by_id="del_by_id"
     @clear_all="$store.dispatch('clear')" 
     :texts="allTexts"
     :show_del_buttons = true
     ></TableWithStore>
    <div class="button_container">
      <ButtonNextPrev @clicks="next_page" :active="lengthLoadingTexts" :right=true> Шаг №2
      </ButtonNextPrev>
    </div>
  </div>
</template>

<style scoped>
.button_container {
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
