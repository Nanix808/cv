<script>
import { toRef } from 'vue'
export default {
  emits: ['clear_all', 'del_by_id', 'show_pdf'],
  props: {
    texts: {
      type: Array,
      required: false,
      default: []
    },
    show_del_buttons: {
      type: Boolean,
      required: false,
      default: false
    },
  },
  setup(props, { emit }) {
    const texts = toRef(() => props.texts)
    const show_del_buttons = toRef(() => props.show_del_buttons)
    const del_by_id = (id) => {
      emit('del_by_id', id)
    };

    const clear_all = () => {
      emit('clear_all')
    }

    const showPdf = (index) =>{
      emit('show_pdf', index)
    }

    return {
      texts,
      del_by_id,
      clear_all,
      show_del_buttons,
      showPdf
    };
  }
}
</script>

<template>
  <div class="right_menu">
    <table class="table">
      <thead>
        <tr>
          <th class="box-1">№</th>
          <th class="box-2">Название файла</th>
          <th class="box-3">Тип файла</th>
          <th class="box-4">Краткий текст</th>
          <th 
          v-if="show_del_buttons"
          class="box-5">Удалить</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(items, index) in texts" :key="index" :data-index="index">
          <td>{{ items.id }}</td>
          <td>{{ items.file_path.name }}</td>
          <td
          @click="showPdf(items.id)"
          
          >{{ items.file_path.type }}</td>
          <td>{{ items.text.substr(0, 300) }}</td>
          <td
          v-if="show_del_buttons"
          >
            <div class="delText">
              <span class="del" @click="del_by_id(index)"></span>
            </div>
          </td>
        </tr>
      </tbody>
      <tfoot
      v-if="show_del_buttons"
      >
        <tr class="clear_all" v-if="texts.length > 0" @click="clear_all">
          <td colspan="5"><span> Очистить все</span></td>
        </tr>
      </tfoot>
    </table>
  </div>
</template>        

<style lang="scss">
.right_menu {
  margin-top: 10px;
  border: 4px dotted #eee;
  border-radius: 15px;
  display: flex;
  width: 99%;
  flex-direction: column;
  flex-wrap: nowrap;
  padding-left: 5px;
  overflow-y: scroll;
  overflow-x: hidden;
  height: auto;
  max-height: 65vh;
}

.table {
  table-layout: fixed;
  width: 100%;
  margin-bottom: 20px;
}

.table th {
  font-weight: bold;
  padding: 5px;
  background: #efefef;
  position: sticky;
  top: 0;
  z-index: 2;
  -moz-user-select: none;
  -khtml-user-select: none;
  user-select: none;
}

.table td {
  padding: 5px 10px;
  border: 1px solid #eee;
  text-align: center;
  word-wrap: break-word;
}

.delText {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  position: relative;
}

.table .del {
  width: 25px;
  height: 25px;
  background-size: cover;
  display: block;
  background: url(../src/assets/images/minus.svg);
  cursor: pointer;
}

.table .del:hover {
  background: url(../src/assets/images/minus-hover.svg);
}

.table tbody tr:nth-child(odd) {
  background: #fff;
}

.table tbody tr:nth-child(even) {
  background: #F7F7F7;
}

.box-4 {
  max-width: 100%;
  width: 100%;
}

.box-1,
.box-3,
.box-5 {
  max-width: 65px;
  width: 65px;
}

.box-2 {
  max-width: 200px;
  width: 200px;
}
.clear_all {
  cursor: pointer;

  &:hover {
    color: red;
  }
}

.right_menu::-webkit-scrollbar {
  width: 14px;
}

.right_menu::-webkit-scrollbar-thumb {
  border: 4px solid rgba(0, 0, 0, 0);
  background-clip: padding-box;
  border-radius: 9999px;
  background-color: #AAAAAA;
}
</style>



