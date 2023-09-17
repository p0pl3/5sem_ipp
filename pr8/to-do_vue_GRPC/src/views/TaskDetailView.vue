<template>
  <div class="container">
    <dialog-window :show="true">
      <task-update-form @update="updateTask" @delete="deleteTask" v-model:task="task"/>
    </dialog-window>
  </div>
</template>

<script>
import DialogWindow from "@/components/DialogWindow";
import TaskUpdateForm from "@/components/TaskUpdateForm";
import axios from "axios";

export default {
  components: {TaskUpdateForm, DialogWindow},
  data() {
    return {
      task: {},
      isDialogVisible: true,
      token: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHBpcmVzIjoxNjU3MzM2MjU2LjAxODc3NX0.yXwNW7KeUpIR6KCwDRgHuvVP34CE3jgZUzSadU7CM14"
    }
  },
  methods: {
    async fetchListTasks() {
      const response = await axios.get('http://127.0.0.1:8000/' + this.$route.params.id);
      this.task = response.data["todo"];
      console.log(this.task)
    },

    async updateTask() {
      const response = await axios.patch(`http://127.0.0.1:8000/${this.task.id}?name=${this.task.name}&completed=true`);

    },

    async deleteTask() {
      const response = await axios.delete('http://127.0.0.1:8000/' + this.$route.params.id);
    }
  },
  mounted() {
    this.fetchListTasks();
  }
}
</script>
<style scoped>

</style>