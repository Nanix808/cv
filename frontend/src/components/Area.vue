<template>
  <div class="file-uploader">
    <div
      class="file-uploader__wrapper"
      :class="{ 'file-uploader__wrapper--drag': isDragStarted }"
    >
      <input
        accept="application/pdf"
        ref="input"
        class="file-uploader__input"
        type="file"
        multiple
        title=""
        @change="uploadFile"
        @dragenter="isDragStarted = true"
        @dragleave="isDragStarted = false"

      >
      
      {{ isDragStarted ? '' : uploadText }}
      <img
        v-show="isDragStarted"
        src="@/assets/images/upload.svg"
        class="file-uploader__icon"
        alt="Загрузите фото"
      >
    </div>
    <div class="file-uploader__files">
      <div
      
        class="file-uploader__file"
      >
        <button
          class="file-uploader__remove"
        
        > </button>
        <img>
      </div>
    </div>
    
  </div>
</template>

<script>
import {
  computed,
  ref,
  // PropType,
  toRefs,
} from 'vue';



export default {
  components: {
  
  },
  props: {
    modelValue: {
      type: Array,
      required: false,
    },
  },

  emits: ['update:modelValue'],

  setup(props, { emit }) {
    const { modelValue } = toRefs(props);

    const input = ref(null);
    const isDragStarted = ref(false);

   
   

    const uploadFile = async (event) => {
      console.log(event)
      if (event.target.files) {
        emit('update:modelValue', [...modelValue.value, ...Array.from(event.target.files)]);
      }

  
     
    
      if (input.value) {
        input.value.value = '';
      }

      isDragStarted.value = false;
    };

    // const removefile = (index: number) => {
    //   emit('update:modelValue', modelValue.value.filter((p, i) => i !== index));
    // };

    // const getSrc = (file: File) => URL.createObjectURL(file);

    const needToUpload = computed(() => modelValue.value.length);

    const uploadText = computed(() => {
      if (needToUpload.value > 0) {
        return `Вы загрузили ${needToUpload.value} 'резюме'`;
      }

      if (needToUpload.value === 0) {
        return 'Загрузите резюме';
      }
    
    });

    return {
      isDragStarted,
      uploadText,
      input,
      uploadFile,
    };
  },
};
</script>

<style lang="scss">
.file-uploader {
  &__wrapper {
    position: relative;
    text-align: center;
    height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 4px dotted #eee;
    border-radius: 15px;
    color: rgba(#000, 0.5);

    &--drag {
      color: rgba(#fff, 0);
      border-color: #777;
    }
  }

  &__input {
    cursor: pointer;
    position: absolute;
    z-index: 2;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    opacity: 0;
  }

  &__files {
    display: flex;
    margin-top: 20px;
  }

  &__file {
    position: relative;
    width: 200px;
    margin-right: 60px;

    img {
      border-radius: 10px;
    }
  }

  &__remove {
    cursor: pointer;
    position: absolute;
    outline: none;
    top: 0;
    left: calc(100% + 10px);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background-color: rgba(#000, 0.05);
    border: 0;

    &::before {
      content: "";
      position: absolute;
      z-index: 1;
      top: calc(50% - 1px);
      left: calc(50% - 5px);
      width: 10px;
      height: 2px;
      background-color: #000;
    }
  }

  &__icon {
    opacity: 0.3;
    width: 50px;
  }
}
</style>