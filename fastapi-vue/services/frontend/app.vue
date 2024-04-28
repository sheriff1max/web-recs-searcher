<template>
  <NuxtLayout class="overflow-x-hidden">
    <nav
      class="relative flex w-full flex-wrap items-center justify-between bg-stone-100 py-2 shadow-dark-mild dark:bg-neutral-700 lg:py-4">
      <div class="flex w-full flex-wrap items-center justify-between px-3">
        <div>
          <a class="mx-2 my-1 flex items-center lg:mb-0 lg:mt-0" href="/">
            <span class="text-black dark:text-white font-semibold">RECS-SEARCHER</span>
          </a>
        </div>
      </div>
    </nav>
    <NuxtLoadingIndicator />
    <NuxtPage />
  </NuxtLayout>
</template>
