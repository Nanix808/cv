import{_ as l,ba as a,o as r,a as _,d,aV as u,n as f}from"./index-93060e0b.js";const v={props:{active:{type:Boolean,required:!1},right:{type:Boolean,required:!1,default:!1},next_icon:{type:Boolean,required:!1,default:!1}},emits:["clicks"],setup(t,{emit:n}){const o=a(()=>t.active),e=a(()=>t.right),c=a(()=>t.next_icon);return{active:o,click:()=>{o.value&&n("clicks")},right:e,next_icon:c}}};function p(t,n,o,e,c,s){return r(),_("button",{class:f(["button",[e.right?"button_right":"button_left",e.active?"active_button":"",e.next_icon?"nojump":""]]),onClick:n[0]||(n[0]=(...i)=>e.click&&e.click(...i))},[d("span",null,[u(t.$slots,"default",{},void 0,!0)])],2)}const x=l(v,[["render",p],["__scopeId","data-v-d4a7d398"]]);export{x as B};
