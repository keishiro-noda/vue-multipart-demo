<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <VueFileAgent :uploadUrl="uploadUrl" v-model="fileRecords"></VueFileAgent>
  </div>
</template>

<script>
export default {
  name: "FileAgent",
  data() {
    return {
      fileRecords: [],
      uploadUrl: "http://localhost:8000/multipart",
    };
  },
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

