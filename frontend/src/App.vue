<template>
  <div id="app">
    <!-- <FileAgent /> -->
    <!-- <UploadComponent /> -->
    <Pond />
    <!-- <Tus /> -->
  </div>
</template>

<script>
// import FileAgent from "./components/FileAgentPreloading.vue";
// import FileAgent from "./components/FileAgentGmail.vue";
import FileAgent from "./components/FileAgentTus.vue";
import UploadComponent from "./components/UploadComponent.vue";
import Pond from "./components/FilePond.vue";
import Tus from "./components/Tus.vue";
export default {
  name: "App",
  components: {
    FileAgent,
    UploadComponent,
    Pond,
    Tus
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>