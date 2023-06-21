<script >
import { ref } from 'vue';
import AreaUploader from '@/components/Area.vue';

export default {
  components: {
    AreaUploader,
  },

  setup() {
    const files = ref([]);

    return { files };
  },
};
</script>

<template>
  <div>
    <AreaUploader v-model="files">
    </AreaUploader>
    {{files }}
  </div>
</template>

<style scoped>

</style>
