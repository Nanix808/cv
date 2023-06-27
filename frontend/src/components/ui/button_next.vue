<script>
import {toRef } from 'vue'

export default {

    
    props: {
    active: {
      type: Boolean,
      required: false,
    },
    emits: ['clicks'],
  },
    setup(props, {emit}) {
      const active = toRef(() => props.active)
      const click = () =>{
        // console.log(active)
        active.value ? emit("clicks") : ''
      }

      return {
        active,
        click
    };
    }
    }



</script>

<template>
<button class="button"
        :class="{ 'active_button': active }"
        @click="click"
><span>Шаг №2</span></button>

</template>
<style>
.button {
  border-radius: 4px;
  background-color: #f4511e;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 28px;
  padding: 12px;
  width: 200px;
  transition: all 0.5s;
 
  margin: 5px;
}
.button.active_button{
    background-color: green;
    cursor: pointer;
}

.button span {

  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button.active_button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.button.active_button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}

</style>