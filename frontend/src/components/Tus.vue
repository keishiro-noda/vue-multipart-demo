<template>
    <section class="container">
      <div>
        <h1 class="title">tus-client</h1>
        <h2 class="subtitle">Tus.io File Upload Sample</h2>
        <v-file-input
          @onchange="handleChange"
          @onremove="handleRemove"
          multiple="true"
          v-model="fileList"
        >
        </v-file-input>
        <v-progress-linear v-model="progressBar" color="cyan"></v-progress-linear>
          <v-btn :disabled="upload === null" @click="pauseUpload">
            {{ button }}
          </v-btn>
          <v-btn @click="startUpload">
            Upload
          </v-btn>
          <p> {{ progressBar}}%</p>
      </div>
    </section>
  </template>
  
  <script>
  import * as tus from 'tus-js-client';
  
  export default {
    name: "Tus",
    data() {
      return {
        fileList: [],
        params: {
          message: 'this is debug message.'
        },
        uploadUrl:'http://localhost:8000/files',
        upload: null,
        uploadIsRunning: false,
        progressBar: 0,
        button: "pause"
      }
    },
    methods: {
      handleChange: function(file, fileList) {
        this.fileList = fileList
      },
      handleRemove: function(file, fileList) {
        this.fileList = fileList
      },
      askToResumeUpload: function(previousUploads, currentUpload) {
        if (previousUploads.length === 0) return

        let text = 'You tried to upload this file previously at these times:\n\n'
        previousUploads.forEach((previousUpload, index) => {
          text += `[${index}] ${previousUpload.creationTime}\n`
        })
        text +=
          '\nEnter the corresponding number to resume an upload or press Cancel to start a new upload'

        const answer = prompt(text)
        const index = parseInt(answer, 10)

        if (!Number.isNaN(index) && previousUploads[index]) {
          currentUpload.resumeFromPreviousUpload(previousUploads[index])
        }
      },
      reset: function() {
        input.value = ''
        toggleBtn.textContent = 'start upload'
        this.upload = null
        this.uploadIsRunning = false
      },
      startUpload: function() {
        let filetype = ""
        let data = this
        const file = this.fileList[0]
        // Only continue if a file has actually been selected.
        // IE will trigger a change event even if we reset the input element
        // using reset() and we do not want to blow up later.
        if (!file) {
          return
        }

        console.log(file.name)

        if (!file.type){
          if (file.name.split('.').pop() == "bag"){
            filetype = 'application/octet-stream'
          }
        }else{
          filetype = file.type
        }

        const endpoint = this.uploadUrl
        let chunkSize = 100000

        let parallelUploads = 1

        const options = {
          endpoint,
          chunkSize,
          retryDelays: [0, 1000, 3000, 5000],
          parallelUploads,
          metadata: {
            name: file.name,
            type: filetype,
          },
          onError(error) {
            if (error.originalRequest) {
              if (window.confirm(`Failed because: ${error}\nDo you want to retry?`)) {
                this.upload.start()
                this.uploadIsRunning = true
                return
              }
            } else {
              window.alert(`Failed because: ${error}`)
            }

            this.reset()
          },
          onProgress(bytesUploaded, bytesTotal) {
            const percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2)
            data.progressBar = percentage
            console.log(bytesUploaded, bytesTotal, `${percentage}%`)
          },
          onSuccess() {
            const anchor = document.createElement('a')
            anchor.textContent = `Download ${this.upload.file.name} (${this.upload.file.size} bytes)`
            anchor.href = this.upload.url
            anchor.className = 'btn btn-success'
            uploadList.appendChild(anchor)

            this.reset()
          },
        }

        this.upload = new tus.Upload(file, options)
        this.upload.findPreviousUploads().then((previousUploads) => {
          this.askToResumeUpload(previousUploads, this.upload)
    
          this.upload.start()
          this.uploadIsRunning = true
        })
      },
      pauseUpload: function() {
        if (this.upload) {
          if (this.uploadIsRunning) {
            this.upload.abort()
            this.uploadIsRunning = false
            this.button = "resume"
          } else {
            this.upload.start()
            this.uploadIsRunning = true
            this.button = "pause"
          }
        }
      }

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

  .progress {
    height: 32px;
  }
  </style>
  