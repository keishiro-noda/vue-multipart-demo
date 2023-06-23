<template>
  <div id="app">
    <!-- <FileAgent /> -->
    <!-- <UploadComponent /> -->
    <Pond />
  </div>
</template>

<script>
// import FileAgent from "./components/FileAgentPreloading.vue";
import UploadComponent from "./components/UploadComponent.vue";
import FileAgent from "./components/FileAgentGmail.vue";
import Pond from "./components/FilePond.vue"
export default {
  name: "App",
  components: {
    FileAgent,
    UploadComponent,
    Pond
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