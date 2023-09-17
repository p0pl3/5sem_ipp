<template>
  <form @submit.prevent>
    <h2>Добавить контакт</h2>
    <my-input class="input__create" placeholder="Имя" v-model="task.name"/>
    <my-input class="input__create" placeholder="Номер" v-model="task.phone"/>
    <my-button class="btn__create" @click="createTask">Добавить</my-button>
  </form>
</template>

<script>
import MyInput from "@/components/MyInput";
import MyButton from "@/components/MyButton";
import MyTextarea from "@/components/MyTextarea";

export default {
  components: {MyTextarea, MyInput, MyButton},
  name: "TaskCreateForm",
  data() {
    return {
      task: {
        title: "",
        description: ""
      }
    }
  },
  methods: {
    createTask() {
      this.$emit("create", this.task);
    }
  }
}
</script>

<style scoped>
.btn__create{
  margin-top: 10px;
}

.input__create {
  background-color: #f8f8f8;
  border: 2px solid #ccc !important;
  height: 50px;
}
</style>