<template>
  <div v-if="isOpen" class="backdrop" @mousedown="close">
    <div class="popup" @mousedown.stop>
      <div class="popup_container">
        <div class="popup_header">
          <h3>Корзина</h3>
          <div class="popup_close"
               @click="close"
          >
            <div></div>
          </div>
        </div>
        <div class="content">

          <vue-pdf-embed :source=" FileOpen" />
       
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { toRef} from 'vue'
import VuePdfEmbed from 'vue-pdf-embed'
// import axios from 'axios'
// import 'vue-select/dist/vue-select.css';
// import {AuthApi} from '@/_api';

export default {
  components: {
    VuePdfEmbed,
  },

  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
    FileOpen: {
     
    },

  emits: {
    close: null,
    ok: null
  },
  setup() {
    const isOpen = toRef(() => props.isOpen)
    const FileOpen = toRef(() => props.FileOpen)
   

    return {
      isOpen,
      FileOpen

    }

  },
  // mounted() {
  //   document.addEventListener("keydown", this.handleKeydown);
  // },
  // beforeUnmount() {
  //   document.removeEventListener("keydown", this.handleKeydown);
  // },


  // methods: {
   
   
  //   handleKeydown(e) {
  //     if (this.isOpen && e.key === "Escape") {
  //       this.close();
  //     }
  //   },
  //   close() {
  //     this.$emit("close");
  //   },
  //   ok() {
  //     this.$emit("ok");
  //     this.$emit("close");
  //   },
 


  //   },
  },
}
</script>
<style>


.popup {
  /* position: absolute;
  top: 40%;
  left: 50%;
  max-width: 480px;
  padding: 40px;
  transform: translate(-50%, -50%);
  background: white;
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, .1);
  display: flex;
  flex-direction: column;
  width: 90%;
  cursor: default;
  margin-right: 76px; */
  position: absolute;
  top: 5%;
  left: 50%;
  width: 90%;
  transform: translate(-50%, -50%);
  background: white;
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, .1);
  display: flex;
  flex-direction: column;
  cursor: default;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.popup_container {
  position: relative;
  display: flex;
  flex-direction: column;
  height: 10vh;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.popup_header {
  height: 40px;
  padding: 8px;
  /* width: 100%; */
  background-color: rgb(245, 245, 245);
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgb(221, 221, 221);
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.popup h3 {
  margin: 0 0 30px;
  padding: 0;
  color: #000000;
  text-align: center;
}

.popup_close {
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;

}

.popup_close div {
  width: 20px;
  height: 20px;
  border-radius: 512px;
  background-size: cover;
  background: url(../src/assets/images/close.svg);
}

.popup_close:hover {
  background-color: rgb(221, 221, 221);
  border-radius: 512px;
}

.popup_close div:hover {
  background: url(../src/assets/images/close-hover.svg);
}

.content {
  background-color: white;
}

.backdrop {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 100;
}


</style>
