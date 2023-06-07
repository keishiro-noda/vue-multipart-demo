<template>
    <div id="app" class="example-full">
      <div class="example-simple">
        <div class="upload">
          <ul>
            <li v-for="(file, index) in files" :key="file.id">
              <span><img class="thumb" v-bind:src="file.blob"></span>
              <span>ファイル名：{{file.name}}</span> 
              <span>ファイルサイズ：{{file.size | formatSize}}バイト</span> -
              <span v-if="file.error">{{file.error}}</span>
              <span v-else-if="file.success">success</span>
              <span v-else-if="file.active">active</span>
              <span v-else-if="file.active">active</span>
              <span v-else></span>
            </li>
          </ul>
          <div class="example-btn">
            <VueUploadComponent
              class="btn btn-primary"
              :multiple="true"
              v-model="files"
              @input-filter="inputFilter"
              @input-file="inputFile"
              ref="upload"
            >
              <i class="fa fa-plus"></i>
                    Select files
            </VueUploadComponent>
            <button type="button" class="btn btn-success" v-if="!$refs.upload || !$refs.upload.active" @click.prevent="$refs.upload.active = true">
              <i class="fa fa-arrow-up" aria-hidden="true"></i>
              Start Upload
            </button>
            <button type="button" class="btn btn-danger"  v-else @click.prevent="$refs.upload.active = false">
              <i class="fa fa-stop" aria-hidden="true"></i>
              Stop Upload
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { VueUploadComponent } from 'vue-upload-component';
  
  export default {
    components: {
      VueUploadComponent
    },
    data() {
      return{
        files: []
      }
    },
    methods: {
      inputFile: function (newFile, oldFile) {
        if (newFile && oldFile && !newFile.active && oldFile.active) {
          console.log('response', newFile.response)
          if (newFile.xhr) {
            console.log('status', newFile.xhr.status)
          }
        }
      },
      inputFilter: function (newFile, oldFile, prevent) {
        if (newFile && !oldFile) {
          if (!/\.(jpeg|jpe|jpg|gif|png|webp)$/i.test(newFile.name)) {
            return prevent()
          }
        }
        newFile.blob = ''
        let URL = window.URL || window.webkitURL
        if (URL && URL.createObjectURL) {
          newFile.blob = URL.createObjectURL(newFile.file)
        }
      }
    }
  };
  </script>
  
  <style>
  .file-uploads {
    overflow: hidden;
    position: relative;
    text-align: center;
    display: inline-block;
  }
  .btn {
    display: inline-block;
    font-weight: 400;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    border: 1px solid transparent;
    padding: .5rem .75rem;
    font-size: 1rem;
    line-height: 1.25;
    border-radius: .25rem;
    transition: all .15s ease-in-out;
  }
  .btn-primary {
    color: #fff;
    background-color: #007bff;
    border-color: #007bff;
  }
  ul {
    padding: 15px;
  }
  .thumb {
    width: 50px;
  }
  </style>
  