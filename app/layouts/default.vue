<script setup lang="ts">
const { data: navigation } = await useAsyncData('navigation', () => fetchContentNavigation())
</script>

<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 font-sans">
    
    <!-- Header -->
    <header class="sticky top-0 z-50 w-full border-b border-gray-200 dark:border-gray-800 bg-white/75 dark:bg-gray-900/75 backdrop-blur">
      <div class="container mx-auto px-4 h-16 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="text-xl font-bold flex items-center gap-2">
            <UIcon name="i-heroicons-book-open" class="w-8 h-8 text-primary-500" />
            Python Mastery
          </NuxtLink>
        </div>
        <div class="flex items-center gap-4">
          <UButton
            to="https://github.com/UnTamed-Fury/learn-python"
            target="_blank"
            color="gray"
            variant="ghost"
            icon="i-heroicons-command-line"
            label="GitHub"
          />
           <ColorModeButton />
        </div>
      </div>
    </header>

    <div class="container mx-auto px-4 flex">
      <!-- Sidebar -->
      <aside class="hidden lg:block w-64 h-[calc(100vh-4rem)] sticky top-16 overflow-y-auto py-8 pr-4 border-r border-gray-200 dark:border-gray-800">
        <nav class="space-y-4">
          <div v-for="level in navigation" :key="level._path">
             <!-- Top Level Categories -->
            <NuxtLink 
              v-if="level.children"
              :to="level._path" 
              class="block font-semibold text-gray-900 dark:text-gray-100 mb-2 hover:text-primary-500"
            >
              {{ level.title }}
            </NuxtLink>
            
            <!-- Sub Links (Limit depth for cleaner sidebar) -->
             <div v-if="level.children" class="pl-3 border-l border-gray-200 dark:border-gray-800 space-y-2">
                <NuxtLink
                  v-for="child in level.children"
                  :key="child._path"
                  :to="child._path"
                  class="block text-sm text-gray-600 dark:text-gray-400 hover:text-primary-500 truncate"
                  active-class="text-primary-500 font-medium"
                >
                  {{ child.title }}
                </NuxtLink>
             </div>
          </div>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 py-8 lg:px-8 max-w-none">
        <article class="prose prose-primary dark:prose-invert max-w-4xl mx-auto">
          <slot />
        </article>
      </main>
    </div>
  </div>
</template>

<style>
/* Custom scrollbar for sidebar */
aside::-webkit-scrollbar {
  width: 4px;
}
aside::-webkit-scrollbar-thumb {
  background-color: #e5e7eb;
  border-radius: 4px;
}
.dark aside::-webkit-scrollbar-thumb {
  background-color: #374151;
}
</style>
