<template>
  <div id="app">
    <FileAgent msg="vue-file-agent-next example"/>
    <UploadComponent />
  </div>
</template>

<script>
import FileAgent from "./components/FileAgent.vue";
// import UploadComponent from "./components/UploadComponent.vue";

export default {
  name: "App",
  components: {
    FileAgent,
    // UploadComponent
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