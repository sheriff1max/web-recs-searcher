<script setup lang="ts">
  // impot modules.
  import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from '@/components/ui/table'
  import { Textarea } from '@/components/ui/textarea'

  // import index ui-elements.
  import selectTaskName from '~/components/index/selectTaskName.vue'
  import sliderCountResults from '~/components/index/sliderCountResults.vue'
  import checkboxInterpret from '~/components/index/checkboxInterpret.vue'
  import selectAnalyzerExplain from '~/components/index/selectAnalyzerExplain.vue'

  // requests.
  const loading = ref(1)
</script>


<template>

  <div class="flex flex-wrap items-top justify-center w-screen gap-16 px-8 py-6">

    <div class="space-y-10">

      <selectTaskName name="task_name" />

      <sliderCountResults />

      <checkboxInterpret name="flag_show_interpret" @click="showSelectAnalyzer" />

      <!-- <p id="analyzer" class="hidden">Hello</p> -->
      <div id="analyzer_div" class="hidden">
        <selectAnalyzerExplain name="analyzer" />
      </div>
    </div>


    <div class="w-80">
      <Textarea required class="h-full" placeholder="Введите текст" id="text" name="text" v-on:input="send" />
    </div>


    <div class="space-y-24" v-if="check_is_search()">
      <Table>
        <TableCaption>Таблица с результатами поиска</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead>Найденный текст</TableHead>
            <TableHead>Сходство</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-for="result in search_result_array">
            <TableCell class="max-w-40 break-words">{{ result.text }}</TableCell>
            <TableCell class="max-w-40 break-words">{{ result.similarity }}</TableCell>
          </TableRow>
        </TableBody>
      </Table>


      <div v-if="check_is_explain()" class="space-y-24">
        <Table>
          <TableCaption>Таблица с важностью текстовых элементов</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead>Найденный элемент</TableHead>
              <TableHead>Сходство</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <TableRow v-for="result in explain_result_array">
              <TableCell class="max-w-40 break-words">{{ result.text }}</TableCell>
              <TableCell class="max-w-40 break-words">{{ result.similarity }}</TableCell>
            </TableRow>
          </TableBody>
        </Table>

        <p class="max-w-80 break-words" id="text_interpret_color"><b>Важные элементы текста при сравнении:</b><br>{{ text }}</p>
      </div>
    </div>


  </div>
</template>


<script lang="ts">
  export default {
    name: 'index',
    data() {
      return {
        search_result_array: [],
        explain_result_array: [],
        indeces_n_grams: [],
        text: '',
        colors_array: [
          '#f96d6d', '#f9a76d', '#f9c96d',
          '#f9f36d', '#d5f96d', '#8cf96d',
          '#6df9b0', '#6df9f6', '#6dbff9',
          '#d76df9', '#f96ddb', '#ad6df9',
        ],
      };
    },
    methods: {
      async send() {
        var task_name = document.getElementsByName('task_name')[0].getAttribute('default-value')
        var k = document.getElementsByName('k')[0].textContent
        var text = document.getElementsByName('text')[0].value
        this.text = text
        var flag_show_interpret = document
          .getElementsByName('flag_show_interpret')[0]
          .getElementsByTagName('button')[0]
          .getAttribute('aria-checked')
        var analyzer = null;
        if (flag_show_interpret) {
          analyzer = document.getElementsByName('analyzer')[0].getAttribute('default-value')
        }

        var body = {
          'task_name': task_name,
          'k': k,
          'text': text,
        }
        var query = {
          'flag_show_interpret': flag_show_interpret,
          'analyzer': analyzer,
        }

        const runtimeConfig = useRuntimeConfig()
        const response = await $fetch(`${runtimeConfig.public.API_URL}`, {
          'method': 'post',
          'body': JSON.stringify(body),
          'query': query,
          headers: {
            "Content-Type": "application/json",
            "Accept": 'application/json',
          },
        })
        this.search_result_array = response.search_result_array
        this.explain_result_array = response.explain_result_array
        this.indeces_n_grams = response.indeces_n_grams
        this.change_color_interpret_text()
      },
      check_is_search() {
        if (this.search_result_array.length != 0) return true;
        else return false;
      },
      check_is_explain() {
        if (this.explain_result_array.length != 0) return true;
        else return false;
      },
      showSelectAnalyzer() {
        const el = document.getElementById('analyzer_div')
        if (el.classList.contains('hidden')) {
          el.classList.remove("hidden")
        } else {
          el.classList.add("hidden")
        }
      },
      change_color_interpret_text() {
        var html_text_color = '<b>Важные элементы текста при сравнении:</b><br>'
        var cur_idx_color = 0

        // Итерируюсь по индексу введённого текста пользователя.
        for (var i = 0; i < this.text.length; i++) {

          // Находу tuple нужного элемента введённого текста, который
          // нужно разукрасить.
          var cur_idx_indeces_n_grams = null
          if (this.indeces_n_grams.length != 0) {
            cur_idx_indeces_n_grams = 0
            // Костыль, который вроде работает.
            var prev_end_idx = this.indeces_n_grams[cur_idx_indeces_n_grams][1]
            
            while ((i < this.indeces_n_grams[cur_idx_indeces_n_grams][0]) || (i > this.indeces_n_grams[cur_idx_indeces_n_grams][1])) {
              cur_idx_indeces_n_grams += 1
              if (cur_idx_indeces_n_grams >= this.indeces_n_grams.length) {
                cur_idx_indeces_n_grams = null
                break
              }
              // Костыль, который вроде работает.
              if (prev_end_idx == this.indeces_n_grams[cur_idx_indeces_n_grams][1]) {
                this.indeces_n_grams.splice(cur_idx_indeces_n_grams, 1)
                cur_idx_indeces_n_grams = null
                break
              }
            }
          }

          // Не крашу одну букву, так как в этом смысла нет.
          if ((cur_idx_indeces_n_grams != null) && (this.indeces_n_grams[cur_idx_indeces_n_grams][1] - i == 1)) {
            cur_idx_indeces_n_grams = null
          }

          // Нечего разукрашивать.
          if (cur_idx_indeces_n_grams == null) {
            html_text_color += this.text[i]
          } else {

            // Не входит в диапазон tuple.
            if (i < this.indeces_n_grams[cur_idx_indeces_n_grams][0]) {
              html_text_color += this.text[i]
            // Красим.
            } else {
              var tmp_start_idx = i
              var tmp_end_idx = this.indeces_n_grams[cur_idx_indeces_n_grams][1]

              html_text_color += '<span style="background-color:' + this.colors_array[cur_idx_color] + '">' + this.text.slice(tmp_start_idx, tmp_end_idx) + '</span>'

              this.indeces_n_grams.splice(cur_idx_indeces_n_grams, 1)
              i = tmp_end_idx - 1  // Для учтения пробелов делаем -1

              cur_idx_color += 1
              if (cur_idx_color >= this.colors_array.length) {
                cur_idx_color = 0
              }
            }
          }
        }
        document.getElementById("text_interpret_color").innerHTML = html_text_color
      },
    }
  }
</script>
