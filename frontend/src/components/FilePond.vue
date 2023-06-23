<template>
    <FilePond
    ref="pond"
    label-idle="Drop files here..."
    allow-multiple="true"
    server="http://localhost:8000/multipart"
    v-on:init="handleFilePondInit"
    v-on:processfile="handleFilePondProcessFile"

    />
</template>
  
<script>
  // Import Vue FilePond
  import vueFilePond from "vue-filepond";
  
  // Import FilePond styles
  import "filepond/dist/filepond.min.css";
  
  // Import FilePond plugins
  // Please note that you need to install these plugins separately
  import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type'
  
  
  // Create component
  const FilePond = vueFilePond(
  );
  
  export default {
    name: "Pond",
    data: function () {
      return ;
    },
    methods: {
      handleFilePondInit: function () {
        console.log("FilePond has initialized");
  
        // FilePond instance methods are available on `this.$refs.pond`
      },
      handleFilePondProcessFile(file) {
      console.log(file)
    }
      
    },
    components: {
      FilePond,
    },
  };
</script>