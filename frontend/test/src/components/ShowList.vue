<template>
  <div>params: {{ $route.params }}</div>
</template>

<script>
export default {
  created() {
    console.log("Post has been created");
  },
  mounted() {
    console.log("Post has been mounted");
  },
};
</script>
