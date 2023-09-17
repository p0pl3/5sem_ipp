<template>
  <button>
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "MyButton"
}
</script>

<style scoped>
button{
  background-color: #7e2acc; /* Green */
  border: 3px solid;
  color: white;
  padding: 12px 26px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 15px;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
}


</style>