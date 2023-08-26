<template>
  <div class="file-uploader">
    <div class="loader" v-if="loader"></div>
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
 

  </div>
</template>

<script>
import {
  computed,
  ref,

} from 'vue';
import { useStore } from 'vuex'
import * as PDFJS from "pdfjs-dist";
import "pdfjs-dist/web/pdf_viewer.css";
// PDFJS.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${PDFJS.version}/pdf.worker.js`;
PDFJS.GlobalWorkerOptions.workerSrc =`https://cdn.jsdelivr.net/npm/pdfjs-dist@${PDFJS.version}/build/pdf.worker.min.js`;
// PDFJS.GlobalWorkerOptions.workerSrc ="https://cdn.jsdelivr.net/npm/pdfjs-dist@3.9.179/build/pdf.worker.min.js";


export default {
  components: {
  
  },
  emits: ['update:modelValue'],

  setup() {
  
    const store = useStore()
    const input = ref(null);
    const isDragStarted = ref(false);
    const loader = ref(false);

   const extractText = async (path) => {
        let pdf = await PDFJS.getDocument(path).promise
        let pages = pdf.numPages
        let pageText = []
        for(let i=1; i<=pages; i++)
        {   
            let page = await pdf.getPage(i)
            let texts = await page.getTextContent()
            let text = texts.items.map((s)=>s.str).join(" ")
            pageText.push(text)
        }
        let allText = pageText.join(" ")
        return allText
   }


   const filesReader = (path) =>{
      return new Promise((resolve) => {
      const fileReader = new window.FileReader()
      fileReader.readAsDataURL(path)
      fileReader.onload = async ()=>{
      let res = fileReader.result;
      const text = await extractText(res)
      resolve(text);  
    }

    });
  }



    const uploadFile = async (event) => {
      
      for(let i=0; i< event.target.files.length; i++){
        loader.value = true
        const file_path = event.target.files[i]
        let text = await filesReader(file_path)
        const fileText = Object.assign({}, {
            file_path : file_path,
            text : text
        })

          
        store.dispatch('addtext', fileText )
    } 
    loader.value = false
      
      if (input.value) {
        input.value.value = '';
      }

      isDragStarted.value = false;
    };


    const uploadText = computed(() => {
  
      if (store.getters.lengthTexts > 0) {
        return `Вы загрузили ${store.getters.lengthTexts} резюме`;
      }

      

      if (store.getters.lengthTexts === 0) {
        return 'Загрузите резюме';
      }
    
    });

    return {
      isDragStarted,
      uploadText,
      input,
      uploadFile,
      loader,
      count: computed(() => store.state.countId),
      increment: () => store.dispatch('increment'),
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
.loader {
  position: absolute;
  top: 0px;
  right: 0px;
  width: 100%;
  height: 100%;
  background-color: #eceaea;
  background-image: url('../src/assets/images/ajax-loader.gif');
  background-size: 50px;
  background-repeat: no-repeat;
  background-position: center;
  z-index: 10000000;
  opacity: 0.4;
  filter: alpha(opacity=40);
}
</style>