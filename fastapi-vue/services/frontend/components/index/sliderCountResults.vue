<script setup lang="ts">
  // impot modules.
  import { Slider } from '@/components/ui/slider'
  import {
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
  } from '@/components/ui/form'

  const loading = ref(1)
</script>


<template>
  <FormField v-slot="{ componentField=[2], value=[1] }" name="_k">
    <FormItem>
      <FormLabel>Количество выводимых результатов</FormLabel>
      <FormControl name="k">
        <Slider
          v-bind="componentField"
          :default-value="[1]"
          :max="10"
          :min="1"
          :step="1"
        />
        <FormDescription class="flex justify-center">
          <span name="k">{{ value?.[0] }}</span>
        </FormDescription>
      </FormControl>
      <FormMessage />
    </FormItem>
  </FormField>
</template>