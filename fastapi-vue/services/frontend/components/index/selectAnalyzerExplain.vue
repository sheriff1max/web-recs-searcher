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
  const loading = ref(1)
</script>


<template>
    <Select defaultValue='word'>
        <SelectTrigger>
          <SelectValue placeholder="Алгоритм для интерпретации" />
        </SelectTrigger>
        <SelectContent>
          <SelectGroup>
            <SelectLabel>Алгоритм для интерпретации</SelectLabel>
            <SelectItem value="word">
              Анализ слов
            </SelectItem>
            <SelectItem value="char">
              Анализ символов
            </SelectItem>
          </SelectGroup>
        </SelectContent>
      </Select>
</template>
