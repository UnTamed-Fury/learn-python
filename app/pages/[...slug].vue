<template>
  <main>
    <ContentDoc>
      <template #not-found>
        <div class="text-center py-20">
          <h1 class="text-4xl font-bold mb-4">404</h1>
          <p class="text-xl text-gray-600 dark:text-gray-400">Page not found</p>
          <UButton to="/" class="mt-8">Go Home</UButton>
        </div>
      </template>
      <template #empty>
        <div class="text-center py-20">
           <h1 class="text-2xl font-bold mb-4">Document is empty</h1>
        </div>
      </template>
    </ContentDoc>
  </main>
</template>