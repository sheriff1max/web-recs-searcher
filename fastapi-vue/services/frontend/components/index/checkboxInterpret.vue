<script setup lang="ts">
  // impot modules.
  import { Checkbox } from '@/components/ui/checkbox'
  const loading = ref(1)
</script>


<template>
    <div class="flex items-center">
        <Checkbox id="terms" />
        <label
          for="terms"
          class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 ml-3"
        >
          Вывод интерпретации результатов
        </label>
      </div>
</template>