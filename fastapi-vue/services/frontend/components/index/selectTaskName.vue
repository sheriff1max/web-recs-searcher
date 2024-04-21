<script setup lang="ts">
  // impot modules
  import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
  } from '@/components/ui/select'

  // requests
  const runtimeConfig = useRuntimeConfig()
  const loading = ref(1)

  const {data, pending} = await useFetch(`${runtimeConfig.public.API_URL}`, {})
</script>


<template>
    <Select :defaultValue='data?.task_names[0]'>
        <SelectTrigger>
          <SelectValue placeholder="Выбор задачи" />
        </SelectTrigger>
        <SelectContent>
          <SelectGroup>
            <SelectLabel>Название задач</SelectLabel>
            <SelectItem v-for="task_name in data?.task_names" :value="task_name" :key="task_name">
              {{ task_name }}
            </SelectItem>
          </SelectGroup>
        </SelectContent>
      </Select>
</template>
