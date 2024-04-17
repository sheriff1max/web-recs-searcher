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
  const runtimeConfig = useRuntimeConfig()
  const loading = ref(1)

  async function send() {
    const task_name = document.getElementsByName('task_name')[0].getAttribute('default-value')
    const k = document.getElementsByName('k')[0].textContent
    const flag_show_interpret = document
      .getElementsByName('flag_show_interpret')[0]
      .getElementsByTagName('button')[0]
      .getAttribute('aria-checked')

    console.log(k)
    // const tmp = await useFetch(()=>`${runtimeConfig.public.API_URL}`, {
    //   'method': 'post',
    //   'body': {
    //     'task_name': 'Города России.pkl',
    //     'k': 5,
    //     'text': 'Красноярс',
    //   },
    // })
  }
</script>


<template>

  <div class="flex flex-wrap items-top justify-center w-screen gap-16 px-16 py-6">

    <div class="space-y-10">

      <selectTaskName name="task_name" />

      <checkboxInterpret name="flag_show_interpret" />

      <sliderCountResults />

    </div>


    <div class="w-80">
      <Textarea required class="h-full" placeholder="Введите текст" name="text" @input="send" />
    </div>


    <div class="space-y-24">
      <Table>
        <TableCaption>Таблица с результатами поиска</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead>Найденный текст</TableHead>
            <TableHead>Сходство</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow>
            <TableCell class="max-w-40 break-words">*текст*</TableCell>
            <TableCell class="max-w-40 break-words">*число*</TableCell>
          </TableRow>
        </TableBody>
      </Table>


      <Table>
        <TableCaption>Таблица с важностью текстовых элементов</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead>Найденный элемент'</TableHead>
            <TableHead>Сходство</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow>
            <TableCell class="max-w-40 break-words">*текст* текст текст текст текст текст текст </TableCell>
            <TableCell class="max-w-40 break-words">*число* текст текст текст текст текст текст</TableCell>
          </TableRow>
        </TableBody>
      </Table>


      <p class="max-w-80 break-words">Разукрашенный исходный текст с его самыми важными элементами.</p>
    </div>


  </div>
</template>
