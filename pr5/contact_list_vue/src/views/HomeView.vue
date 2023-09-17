<template>
  <div class="container">
    <div class="to_do__wrapper">
      <h1>Контакты</h1>
      <div class="action__btns" style="">
        <my-button @click="isDialogVisible = true;">Добавить</my-button>
      </div>
      <task-list v-model:tasks="searchedTasks"/>
      <dialog-window v-model:show="isDialogVisible">
        <task-create-form @create="createTask"/>
      </dialog-window>
    </div>
  </div>
</template>

<script>
import TaskList from "@/components/TaskList";
import MyButton from "@/components/MyButton";
import MyInput from "@/components/MyInput";
import DialogWindow from "@/components/DialogWindow";
import MyTextarea from "@/components/MyTextarea";
import TaskCreateForm from "@/components/TaskCreateForm";
import axios from "axios";

export default {
  components: {TaskCreateForm, MyTextarea, DialogWindow, MyInput, TaskList, MyButton},
  data() {
    return {
      isDialogVisible: false,
      tasks: [],
      searchQuery: "",
    }
  },
  methods: {
    async fetchListTasks() {
      const response = await axios.get('http://localhost:8000/contact/');
      this.tasks = response.data;
    },
    async createTask(task){
      this.isDialogVisible = false;
      if (!task.title.isEmpty && !task.description.isEmpty){
        await axios.post('http://localhost:8000/contact/', {"name": task.name, "phone": task.phone});
        await this.fetchListTasks();
      }
    },
    logout() {
      this.$store.dispatch("onLogout");
      this.$router.push("/login")
    }
  },
  computed: {
    searchedTasks() {
      return this.tasks.filter(task => task.name.toLowerCase().includes(this.searchQuery.toLowerCase()));
    }
  },
  created() {
    this.fetchListTasks();
  },
  mounted() {
    this.fetchListTasks();
  },
  watch: {
    '$store.state.token': function() {
      this.fetchListTasks();
    }
  }
}
</script>

<style>

h1{
  font-size: 60px;
}

h2{
  text-align: center;
  font-size: 40px;
}

my-input{
  width: 400px;
}

.action__btns {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
}
</style>