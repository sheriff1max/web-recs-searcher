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
  import checkboxInterpret from '~/components/index/checkboxInterpret.vue'
  import sliderCountResults from '~/components/index/sliderCountResults.vue'

  // requests.
  const loading = ref(1)
</script>


<template>

  <div class="flex flex-wrap items-top justify-center w-screen gap-16 px-8 py-6">

    <div class="space-y-10">

      <selectTaskName name="task_name" />

      <checkboxInterpret name="flag_show_interpret" />

      <sliderCountResults />

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


        <p class="max-w-80 break-words">Разукрашенный исходный текст с его самыми важными элементами.</p>
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
      };
    },
    methods: {
      async send() {
        var task_name = document.getElementsByName('task_name')[0].getAttribute('default-value')
        var k = document.getElementsByName('k')[0].textContent
        var text = document.getElementsByName('text')[0].value
        var flag_show_interpret = document
          .getElementsByName('flag_show_interpret')[0]
          .getElementsByTagName('button')[0]
          .getAttribute('aria-checked')

        var body = {
          'task_name': task_name,
          'k': k,
          'text': text,
        }
        var query = {
          'flag_show_interpret': flag_show_interpret,
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
      },
      check_is_search() {
        if (this.search_result_array.length != 0) return true;
        else return false;
      },
      check_is_explain() {
        if (this.explain_result_array.length != 0) return true;
        else return false;
      },
    }
  }
</script>
