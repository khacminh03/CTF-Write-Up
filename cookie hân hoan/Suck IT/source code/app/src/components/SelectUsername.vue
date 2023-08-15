<template>
  <div class="select-username nes-field nes-container is-centered">
    <form @submit.prevent="onSubmit">
      <label for="name_field">Your name</label>
      <div>
        <input v-model="username" type="text" id="name_field" class="is-centered nes-input">
      </div>
      <button :disabled="!isValid" class="nes-btn ">Send</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SelectUsername",
  data() {
    return {
      username: "",
    };
  },
  computed: {
    isValid() {
      return this.username.length > 2;
    },
  },
  methods: {
    onSubmit() {
      this.$emit("input", this.username);
    },
  },
};
</script>

<style scoped>
.select-username {
  width: 300px;
  margin: 100px auto 0;
}

.nes-btn{
  margin-top: 10px;
}

</style>
