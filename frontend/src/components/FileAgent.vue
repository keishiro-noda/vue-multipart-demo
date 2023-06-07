<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <VueFileAgent
      ref="profilePicRef"
      :multiple="false"
      @select="onSelect($event)"
      v-model="profilePic"
    ></VueFileAgent>
    <button @click="upload">Upload</button>
  </div>
</template>

<script>
export default {
  name: "FileAgent",
  data() {
    return {
      fileChunks: [],
      uploadUrl: "http://localhost:8000/multipart",
      uploaded: false,
    };
  },
  props: {
    msg: String,
  },
  methods: {
    handleFileChange(files) {
      this.fileChunks = files;
    },
    upload: function(){
      var self = this;
      this.$refs.profilePicRef.upload(this.uploadUrl, this.uploadHeaders, [this.profilePic]).then(function(){
        self.uploaded = true;
        setTimeout(function(){
          // self.profilePic.progress(0);          
        }, 500);
      });
    },
    onSelect: function(fileRecords){
      console.log('onSelect', fileRecords);
      this.uploaded = false;
    },
    async uploadChunks() {
      const totalChunks = this.fileChunks.length;
      console.log(this.fileChunks)
      await this.uploadChunk(this.fileChunks);
    //   for (let i = 0; i < totalChunks; i++) {
    //     const chunk = this.fileChunks[i];
    //     console.log(chunk)
    //     await this.uploadChunk(chunk);
    //   }
    //   console.log('All chunks uploaded');
    },
    async uploadChunk(chunk) {
      const formData = new FormData();
      formData.append('chunk', chunk.file);
      console.log(formData)
      
      try {
        const response = await fetch('http://localhost:8000/multipart', {
          method: 'POST',
          body: formData,
        });
        console.log("posted")
        const data = await response.json();
        console.log('Chunk uploaded:', data);
      } catch (error) {
        console.error('Error uploading chunk:', error);
      }
    },
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

