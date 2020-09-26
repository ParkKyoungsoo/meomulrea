<template>
  <span @click="onEmojiClick">{{ emoji.value }}</span>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: {
    emoji: {
      type: String,
      default: "",
    },
  },
  methods: {
    onEmojiClick() {
      this.$emit("click", this.emoji);
    },
  },
};
</script>
