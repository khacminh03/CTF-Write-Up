<template>
  <section class="nes-container with-title">
    <div class="header">
      <status-icon :connected="user.connected" />{{ user.username }}
    </div>
    <section class="nes-container is-dark">
      <section class="message-list">
        <div v-for="(message, index) in user.messages" :key="index">
          <section
            v-if="displaySender(message, index)"
            :class="{
              'message -right': message.fromSelf,
              'message -left': !message.fromSelf
            }"
          >
            <i v-if="!message.fromSelf" class="nes-bcrikko"></i>
            <!-- Balloon -->
            <div
              class="nes-balloon is-dark"
              :class="{
                'from-right': message.fromSelf,
                'from-left': !message.fromSelf
              }"
            >
              <p>{{ message.content }}</p>
            </div>
          </section>
        </div>
      </section>
    </section>

    <form @submit.prevent="onSubmit" class="form">
      <textarea v-model="input" placeholder="Your message..." class="nes-textarea input"></textarea>
      <button :disabled="!isValid" class="nes-btn is-primary send-button">Send</button>
    </form>
  </section>
</template>

<script>
import StatusIcon from "./StatusIcon";

export default {
  name: "MessagePanel",
  components: {
    StatusIcon,
  },
  props: {
    user: Object,
  },
  data() {
    return {
      input: "",
    };
  },
  methods: {
    onSubmit() {
      this.$emit("input", this.input);
      this.input = "";
    },
    displaySender(message, index) {
      return (
        index === 0 ||
        this.user.messages[index - 1].fromSelf !==
          this.user.messages[index].fromSelf
      );
    },
  },
  computed: {
    isValid() {
      return this.input.length > 0;
    },
  },
};
</script>

<style scoped>
 .header {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .header .nes-icon {
    margin-right: 8px;
  }

  .message {
    margin-bottom: 10px;
    display: flex;
  }

  .-right{
    justify-content: flex-end; /* Align messages to the right */
  }

  .sender {
    font-size: 0.8em;
    margin-bottom: 4px;
  }

  .form {
    margin-top: 20px;
  }

  .input {
    resize: none;
  }

  .send-button {
    margin-top: 10px;
  }

  .nes-bcrikko {
    margin-right: 10px;
  }

  .nes-balloon.is-dark {
    background-color: #212529;
    color: #f0f0f0;
    border-color: #212529;
  }

  .from-right .nes-balloon::before {
    border-right-color: #212529;
  }

  .from-right .nes-balloon::after {
    border-right-color: #212529;
  }

  .from-left .nes-balloon::before {
    border-left-color: #212529;
  }

  .from-left .nes-balloon::after {
    border-left-color: #212529;
  }
  
</style>
