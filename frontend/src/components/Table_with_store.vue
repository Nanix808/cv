<script>
import { computed } from 'vue';
import { useStore } from 'vuex'
export default {
    setup() {

      const store = useStore()

      
      const delText= (id) => {
        store.dispatch('del_by_id', id )



      }



      return {
      count: computed(() => store.state.count),
      lengthLoadingTexts: computed(() => store.getters.lengthTexts),
      allTexts: computed(() => store.getters.getAllTexts),
      delText,
      clear_all: () => store.dispatch('clear'),
    //   increment: () => store.dispatch('increment'),
    //   decrement: () => store.dispatch('decrement'),
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
            <th class="box-5">Удалить</th>
          </tr>
          </thead>
                   <tbody>

           <tr v-for="(items, index) in allTexts" :key="index"
                :data-index="index"
            >
              <td>{{ items.id }}</td>
              <td>{{ items.file_path.name }}</td>
              <td>{{ items.file_path.type}}</td>
              <td>{{ items.text.substr(0, 300) }}</td>
              <td>
                <div class="delText">

                      <span
                          class="del"
                          @click="delText(index)"></span>
                </div>
              </td>
            </tr> 

  
      
           </tbody>
           <tfoot >
              <tr class="clear_all"
                  v-if="$store.getters.lengthTexts > 0"
                  @click="clear_all"
              >
           
              <td colspan="5"><span> Очистить все</span></td>
    
              </tr>
              </tfoot>
        </table>
      </div>


</template>        

<style lang="scss">

.right_menu {
    // padding-top: 1px;
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
// position: relative;
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
// border: 1px solid #dddddd;
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

.box-1, .box-3, .box-5{
max-width: 65px;
width: 65px;
}
.box-2{
max-width: 200px;
width: 200px;
}



.clear_all{
    cursor: pointer;

    &:hover{
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



