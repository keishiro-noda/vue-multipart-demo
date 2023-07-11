<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
    <template v-slot:activator="{ props }">
      <v-btn color="primary" v-bind="props" >
       Open Dialog
      </v-btn>
     </template>

      <v-card>
        <FilePond
        ref="pond"
        label-idle="Drop files here..."
        allow-multiple="true"
        v-bind:server="myServer"
        >
        </FilePond>
      </v-card>
    </v-dialog>
  </div>

  <br />
  
  <div class="text-center">
    <v-menu
      open-on-hover
    >
      <template v-slot:activator="{ props }">
        <v-btn
          color="primary"
          v-bind="props"
        >
          Dropdown
        </v-btn>
      </template>

      <v-card>
        <FilePond
        ref="pond"
        label-idle="Drop files here..."
        allow-multiple="true"
        v-bind:server="myServer"
        >
        </FilePond>
      </v-card>
    </v-menu>
  </div>
    <!-- <v-btn :disabled="upload === null" @click="pauseUpload">
      {{ button }}
    </v-btn> -->
</template>
  
<script>
  import vueFilePond from "vue-filepond";
  import * as tus from 'tus-js-client';
  import "filepond/dist/filepond.min.css";
  import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type'
  

  const FilePond = vueFilePond(
    FilePondPluginFileValidateType,
  );
  
  export default {
    name: "Pond",
    data() {
      return{
        uploadUrl:'http://localhost:8000/files',
        upload: null,
        uploadIsRunning: false,
        progressBar: 0,
        button: "pause",
        isError: false,
        dialog: false,
        myServer: {
          process: (fieldName, file, metadata, load, progress, error) => {

            if (this.isError && this.upload && !this.uploadIsRunning){
              this.upload.start()
              this.uploadIsRunning = true
              this.isError = false
              return
            }
            let filetype = ""
            let data = this
            if (!file) {
              return
            }

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
              onError(onerror) {
                error()
                data.isError = true
                if (onerror.originalRequest) {
                  if (data.upload) {
                    data.upload.abort()
                    data.uploadIsRunning = false
                  }
                } else {
                  window.alert(`Failed because: ${onerror}`)
                }
              },
              onProgress(bytesUploaded, bytesTotal) {
                const percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2)
                data.progressBar = percentage
                console.log(bytesUploaded, bytesTotal, `${percentage}%`)
                // progress(true, bytesUploaded, bytesTotal);
                // progress(true, percentage, 100);
              },
              onSuccess() {
                load()
                data.reset()
              },
            }

            this.upload = new tus.Upload(file, options)
            this.upload.findPreviousUploads().then((previousUploads) => {
              this.askToResumeUpload(previousUploads, this.upload)
        
              this.upload.start()
              this.uploadIsRunning = true
            })
          },
        },
      }
    },
    methods: {
      handleButtonClick() {
        // ボタンのクリックイベントの処理
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
        this.upload = null
        this.uploadIsRunning = false
      },
      startUpload: function(file) {
        if (this.isError && this.upload && !this.uploadIsRunning){
          this.upload.start()
          this.uploadIsRunning = true
          this.isError = false
          return
        }

        let filetype = ""
        let data = this
        if (!file) {
          return
        }

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
            data.isError = true
            if (error.originalRequest) {
              if (data.upload) {
                data.upload.abort()
                data.uploadIsRunning = false
              }
            } else {
              window.alert(`Failed because: ${error}`)
            }
          },
          onProgress(bytesUploaded, bytesTotal) {
            const percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2)
            data.progressBar = percentage
            console.log(bytesUploaded, bytesTotal, `${percentage}%`)
          },
          onSuccess() {
            data.reset()
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
      
    },
    components: {
      FilePond,
    },
  };
</script>

<style>
.custom-progress-bar {
  width: 100%;
  height: 20px;
  background-color: #f0f0f0;
}

.progress-bar {
  height: 100%;
  background-color: blue;
}

.filepond--item-panel {
  background-color: #555;
}
</style>