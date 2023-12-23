<template>
  <div class="home">
    <img alt="Logo" src="../assets/logo.png" width="200">
    <h2>RECS-SEARCHER</h2>

    <div class="center">
      <div class="box_inputer">

        <ListTaskNames msg="selecter"/>

        <div style="margin-top: 20px;">
          <p>Количество выводимых результатов:</p>
          <input id="rangeValue" type="range" min="1" max="10" value="1" oninput="textRangeValue.innerText = this.value">
          <p id="textRangeValue">1</p>
        </div> 
        
        <div class="inputer">
          <textarea id="text_inputer" required placeholder="Введите текст" rows="5" cols="50" @input="send"></textarea>
        </div>
      </div>

      <div class="box_outputer" v-if="check_is_result()">
        <table>
          <thead>
            <tr>
              <th colspan="2">Результат поиска</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="background: rgba(166, 113, 44, 1);"><b>Найденный текст</b></td>
              <td style="background: rgba(166, 113, 44, 1);"><b>Сходство</b></td>
            </tr>
            <tr v-for="result in dict.result" :key="result">
              <td>{{  result.text  }}</td>
              <td>{{ result.similarity }}</td>
            </tr>
          </tbody>
        </table>
      </div>
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
  data() {
    return {
      dict: {'result': []},
    };
  },
  methods: {
    send() {
      var task_names = document.getElementById("select_task_name");
      var task_name = task_names.options[task_names.selectedIndex].value;

      var k = document.getElementById('rangeValue').value;

      var text = document.getElementById('text_inputer').value;
      if (text.length == 0) {
        document.getElementById("text_inputer").style.backgroundColor = "#EC5353";
        return false;
      }

      document.getElementById("text_inputer").style.backgroundColor = "white";
      axios.post("/",{
          task_name: task_name,
          k: k,
          text: text,
        }, {
          headers: {
            'Content-type': 'application/json',
          }
        }
      ).then((res) => {
          this.dict = res.data;
          console.log(this.dict)
        })
        .catch((error) => {
          console.error(error);
        });
    },
    check_is_result() {
      if (this.dict.result.length != 0) return true;
      else return false;
    },
  },
}
</script>

<style>

.center {
  width: 600px;
  margin: 0 auto;
  margin-top: 40px;
  padding-bottom: 40px;
}

.box_inputer {
  background: #FFCA86;
  padding-top: 50px;
  padding-bottom: 30px;
  border-radius: 16px;
} 

.box_outputer {
  background: #FFF7EE;
  margin-top: 50px;
} 

table,
th,
td {
  border: 1px solid;
}

table {
  width: 100%;
}

tbody {
  white-space: nowrap;
}

th,
td {
  padding: 5px 10px;
  border-top-width: 0;
  border-left-width: 0;
}

th {
  position: sticky;
  top: 0;
  background: rgba(166, 113, 44, 1);
  vertical-align: bottom;
}

th:last-child,
td:last-child {
  border-right-width: 0;
}

#button_inputer {
  margin-bottom: 30px;
}
</style>
