<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <VueFileAgent
      ref="profilePicRef"
      :multiple="true"
      v-model="profilePic"
      @select="onSelect($event)"
    ></VueFileAgent>
    <button @click="uploadChunks">Upload</button>
  </div>
</template>

<script>
import { toRaw } from 'vue';
import axios from "axios";
export default {
  name: "FileAgent",
  data() {
    return {
      fileChunks: [],
      uploadUrl: "http://localhost:8000/multipart",
      uploaded: false,
      uploadHeaders: {},
      profilePic: null,
      api: axios.create({ baseURL: "http://localhost:8000" }),
    };
  },
  props: {
    msg: String,
  },
  methods: {
    async uploadChunks() {
      const chunk = []
      for (let i = 0; i < this.fileChunks.length; i++) {
        chunk.push(toRaw(this.fileChunks[i])[0])
      }
      await this.uploadChunk(chunk);
       console.log('All chunks uploaded');
    },
    async uploadChunk(chunk) {
      let formData = new FormData();
      for (let i = 0; i < chunk.length; i++) {
        formData.append('files', chunk[i].file);
      }

      try {
        const response = await this.api.post('/multipart', formData );
        console.log("posted")
        const data = response.data;
        console.log('Chunk uploaded:', data);
      } catch (error) {
        console.error('Error uploading chunk:', error);
      }
    },
    onSelect(fileRecords){
      console.log('onSelect', fileRecords);
      this.uploaded = false;
      this.fileChunks.push(fileRecords)
    }
  },
  
};
</script>

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

