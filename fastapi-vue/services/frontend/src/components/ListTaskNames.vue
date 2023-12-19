<template>
  <div>
    <p>Выбор задачи:</p>
    <select id="select_task_name">
      <option :value="task_name" v-for="task_name in dict.list_task_names" :key="task_name">
        {{ task_name }}
      </option>
    </select>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'task-names',
  data() {
    return {
      dict: {'list_task_names': []},
    };
  },
  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          this.dict = res.data;
          console.log(this.dict)
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>