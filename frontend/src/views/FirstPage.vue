<script >
import { ref, computed } from 'vue';
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import AreaUploader from '@/components/Area.vue';
import TableWithStore from '@/components/Table_with_store.vue';
import ButtonNextPrev from '@/components/ui/ButtonNextPrev.vue';
import VuePdfEmbed from 'vue-pdf-embed'

export default {
  components: {
    AreaUploader,
    TableWithStore,
    ButtonNextPrev,
    VuePdfEmbed,
  },

  setup() {
    const pdfSource = 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/examples/learning/helloworld.pdf'
    const store = useStore()
    const router = useRouter()

    const next_page = () => {
      router.push({ name: 'second' })
    }

    const del_by_id = (id) => {
      store.dispatch('del_by_id', id)
    };

    const closePopup = () => {

      console.log('close')

      PopupOpen.value = false

    };

    return {
      lengthLoadingTexts: computed(() => store.getters.lengthTexts ? true : false),
      allTexts: computed(() => store.getters.getAllTexts),
      file1: computed(() => allTexts[0].file_path.type),
      next_page,
      del_by_id,
      pdfSource,
    };
  },
};
</script>

<template>
  <div>
    <AreaUploader>
    </AreaUploader>
    <TableWithStore @del_by_id="del_by_id" @clear_all="$store.dispatch('clear')"  :texts="allTexts"
      :show_del_buttons=true></TableWithStore>
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
