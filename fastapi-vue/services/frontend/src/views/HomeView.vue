<template>
  <div class="home">
    <img alt="Logo" src="../assets/logo.png" width="200">
    <h2>RECS-SEARCHER</h2>

    <div class="box_inputer">

      <ListTaskNames msg="selecter"/>

      <div class="slider">
        <p>Количество выводимых результатов</p>
        <input name="k" id="rangeValue" type="range" min="1" max="10" value="1" oninput="textRangeValue.innerText = this.value">
        <p id="textRangeValue">1</p>
      </div> 
      
      <div class="inputer">
        <textarea name="text" id="text_inputer" required placeholder="Введите текст" rows="5" cols="50"></textarea>
      </div>

      <button id="button_inputer" @click="send">Поиск</button>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import ListTaskNames from '@/components/ListTaskNames.vue'

export default {
  name: 'HomeView',
  components: {
    ListTaskNames
  },
  methods: {
    send() {
      var task_names = document.getElementById("select_task_name");
      var task_name = task_names.options[task_names.selectedIndex].value;
      console.log(task_name);

      var k = document.getElementById('rangeValue').value;
      console.log(k);

      var text = document.getElementById('text_inputer').value;
      console.log(text);
      if (text.length == 0) {
        document.getElementById("text_inputer").style.backgroundColor = "#EC5353";
        return false;
      }

      document.getElementById("text_inputer").style.backgroundColor = "white";
      return axios.post("/",{
          task_name: task_name,
          k: k,
          text: text,
        }, {
          headers: {
            'Content-type': 'application/json',
          }
        }
      )
    },
  },
}
</script>

<style>
.box_inputer {
  background: aqua;
  padding-top: 50px;
  width: 600px;
  margin: 0 auto;
} 
</style>
