<script >
import { ref, watchEffect } from 'vue';
import AreaUploader from '@/components/Area.vue';
import TableWithStore from '@/components/Table_with_store.vue';

export default {
  components: {
    AreaUploader,
    TableWithStore
  },

  setup() {
    const files = ref([]);


    const getData = async () => {
      await fetch("https://api.chucknorris.io/jokes/random", {
        method: 'GET' //optional
    })
      .then(async (response) => {
        const data = await response.json()
        console.log("data", data);
        // this.data = data
      })
      .catch((error) => {return error})
 
    };

    watchEffect(() => console.log(files))

    return { files };
  },
};
</script>

<template>
  <div>
    <AreaUploader v-model="files">
    </AreaUploader>
    <TableWithStore></TableWithStore>
    {{files }}
  </div>
</template>

<style scoped>

</style>
