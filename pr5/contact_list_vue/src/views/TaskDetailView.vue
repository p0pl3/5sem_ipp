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
    async fetchListTask() {
      const response = await axios.get('http://localhost:8000/contact/' + this.$route.params.id);
      this.task = response.data;
      console.log(this.task)
    },

    async updateTask() {
      const response = await axios.put('http://localhost:8000/contact/' + this.$route.params.id + '/',
          {"name": this.task.name, "phone": this.task.phone},
          {headers: {Authorization: `Bearer ${this.$store.getters.getToken}`}});
    },

    async deleteTask() {
      const response = await axios.delete('http://localhost:8000/contact/' + this.$route.params.id);
    }
  },
  mounted() {
    this.fetchListTask();
  }
}
</script>
<style scoped>

</style>