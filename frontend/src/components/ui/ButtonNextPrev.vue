<script>
import { toRef } from 'vue'

export default {
  props: {
    active: {
      type: Boolean,
      required: false,
    },
    right: {
      type: Boolean,
      required: false,
      default: false
    },
    next_icon: {
      type: Boolean,
      required: false,
      default: false
    },
  },
  emits: ['clicks'],

  setup(props, { emit }) {
    const active = toRef(() => props.active)
    const right = toRef(() => props.right)
    const next_icon = toRef(() => props.next_icon)
    const click = () => {
      active.value ? emit("clicks") : ''
    }

    return {
      active,
      click,
      right,
      next_icon
    };
  }
}

</script>

<template>
  <button class="button"
    :class="[right ? 'button_right' : 'button_left', active ? 'active_button' : '', next_icon ? 'nojump' : '']"
    @click="click"><span>
      <slot></slot>
    </span></button>
</template>
<style scoped>
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

.button.active_button {
  background-color: green;
  cursor: pointer;
}

.button span {
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button_left.active_button span::before {
  content: '\00ab';
  position: absolute;
  opacity: 0;
  top: 0;
  left: -10px;
  transition: 0.5s;
}

.button_left.active_button:hover span {
  padding-left: 25px;
}

.button_left:hover span::before {
  opacity: 1;
  left: 0px;
}

.button_right.active_button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.button_right.active_button:hover span {
  padding-right: 25px;
}

.button_right:hover span:after {
  opacity: 1;
  right: 0;
}

.nojump.button_left:hover span::before,
.nojump.button_right:hover span::after {
  opacity: 0;
}

.nojump.button_left:hover span,
.nojump.button_right:hover span {
  padding: 0;
}

.nojump.button_left.active_button:hover span,
.nojump.button_right.active_button:hover span {
  transform: scale(1.2);
}</style>