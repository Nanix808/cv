<template>
  <div v-if="isOpen" class="backdrop" @mousedown="close">
    <div class="popup" @mousedown.stop>
      <div class="popup_container">
        <div class="popup_header">
          <h3>{{ FileName  }}</h3>
          <div class="popup_close"
               @click="close"
          >
            <div></div>
          </div>
        </div>
        <div class="content">
          <vue-pdf-embed :source="FileOpen" 
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { toRef, onMounted, onUnmounted} from 'vue'
import VuePdfEmbed from 'vue-pdf-embed'

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
    FileName: String

  },

  emits: {
    close: null,
    ok: null
  },
  
  setup(props, {emit}) {
    const isOpen = toRef(() => props.isOpen)
    const FileOpen = toRef(() => props.FileOpen)
    const FileName  = toRef(() => props.FileName)

    const close = () => {
      emit("close");
    };

   const handleKeydown = (e)=> {
      if (isOpen.value && e.key === "Escape") {
        close();
      }
    }
    onMounted(() => {
      document.addEventListener("keydown", handleKeydown);
    })
    onUnmounted(() => {
      document.removeEventListener("keydown", handleKeydown)
    })
    return {
      isOpen,
      FileOpen,
      FileName,
      close
    }
  },
}
</script>
<style>


.popup {
  position: absolute;
  top: 50%;
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
  height: 90vh;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.popup_header {
  height: 40px;
  padding: 8px;
  background-color: rgb(245, 245, 245);
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgb(221, 221, 221);
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.popup h3 {
  padding: 5px; 
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
  /* margin-right: 15px; */
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
  overflow-y: auto;
  overflow-x: hidden;
  width: 100%; 
  position: relative;
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

.content::-webkit-scrollbar {
  width: 14px;
}

.content::-webkit-scrollbar-thumb {
  border: 4px solid rgba(0, 0, 0, 0);
  background-clip: padding-box;
  border-radius: 9999px;
  background-color: #AAAAAA;
}


</style>
