<template>
    <section class="container">
      <div>
        <h1 class="title">tus-client</h1>
        <h2 class="subtitle">Tus.io File Upload Sample</h2>
        <v-file-input
          action
          :auto-upload="false"
          @onchange="handleChange"
          @onremove="handleRemove"
          multiple="true"
          v-model="fileList"
        >
        </v-file-input>
        <v-button slot="trigger" class="button--green">
            Select Files
          </v-button>
          <v-button class="button--grey" @click="upload">
            Upload
          </v-button>
      </div>
    </section>
  </template>
  
  <script>
  
  export default {
    name: "Tus",
    data() {
      return {
        fileList: [],
        params: {
          message: 'this is debug message.'
        }
      }
    },
    methods: {
      handleChange: function(file, fileList) {
        this.fileList = fileList
      },
      handleRemove: function(file, fileList) {
        this.fileList = fileList
      },
      upload: async function() {
        if (this.fileList.length === 0) {
            console.log(this.fileList)
          return
        }
        await Promise.all(
          this.fileList.map(file => {
            return this.$store.dispatch('upload', {
              file: file,
              params: this.params
            })
          })
        )
        this.fileList = []
      },
    }
  }
  </script>
  
  <style>
  .container {
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  
  .title {
    font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
      'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    display: block;
    font-weight: 300;
    font-size: 60px;
    color: #35495e;
    letter-spacing: 1px;
  }
  
  .subtitle {
    font-weight: 300;
    font-size: 30px;
    color: #526488;
    word-spacing: 5px;
    padding-bottom: 15px;
  }
  </style>
  