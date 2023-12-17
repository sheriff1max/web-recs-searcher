<template>
  <div>
    <table>
      <thead>
        <tr>
          <th colspan="2">The table header</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>The table body</td>
          <td>with two columns</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'predicted-results',
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