<template>
    <div class="vfa-demo bg-light pt-3">
        <VueFileAgent
          ref="vfaDemoRef"
          :uploadHeaders="{}"
          :multiple="true"
          :deletable="true"
          :theme="'list'"
          v-model="fileRecords"
          @select="onSelect($event)"
        >
        </VueFileAgent>
        <v-list v-slot:file-preview="slotProps">
          <v-list-item :key="slotProps.index" >
            <v-btn icon class="close remove" aria-label="Remove" @click="removeFileRecord(slotProps.fileRecord)">
            </v-btn>
            <v-list-content :class="{'completed': slotProps.fileRecord.progress() == 100}">
              <div class="file-progress-bar" role="progressbar" :style="{width: slotProps.fileRecord.progress() + '%'}"></div>
            </v-list-content>
            <v-list-title>{{ slotProps.fileRecord.name() }}</v-list-title> <v-list-content>({{ slotProps.fileRecord.size() }})</v-list-content>
          </v-list-item>
      </v-list>
    </div>
</template>
  
<script>
import SvgIcon from '@jamescoyle/vue-icon';
import Resumable from 'resumablejs';
import * as tus from 'tus-js-client';
export default {
  name: "FileAgent",
  components: {
    SvgIcon
  },
  data(){
      return {
          fileRecords: [],
          uploadUrl:'http://localhost:8000/multipart',
          upload: null,
          uploadIsRunning: false
      }
  },
  methods: {
      removeFileRecord: function(fileRecord){
          return this.$refs.vfaDemoRef.removeFileRecord(fileRecord);
      },
      handleFileSelected(slotProps) {
        this.slots = slotProps; 
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
      onSelect: function(files) {
        let progressBar = '0%'
        const file = files[0]
        console.log(files)
        // Only continue if a file has actually been selected.
        // IE will trigger a change event even if we reset the input element
        // using reset() and we do not want to blow up later.
        if (!file) {
          return
        }

        const endpoint = this.uploadUrl
        let chunkSize = parseInt(1000, 10)

        let parallelUploads = 1

        const options = {
          endpoint,
          chunkSize,
          retryDelays: [0, 1000, 3000, 5000],
          parallelUploads,
          metadata: {
            name: file.name,
            type: file.type,
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
            progressBar = `${percentage}%`
            console.log(bytesUploaded, bytesTotal, `${percentage}%`)
          },
          onSuccess() {
            const anchor = document.createElement('a')
            anchor.textContent = `Download ${this.upload.file.name} (${this.upload.file.size} bytes)`
            anchor.href = upload.url
            anchor.className = 'btn btn-success'
            uploadList.appendChild(anchor)

            this.reset()
          },
        }

        console.log(options)

        this.upload = new tus.Upload(file, options)
        this.upload.findPreviousUploads().then((previousUploads) => {
          this.askToResumeUpload(previousUploads, this.upload)
    
          this.upload.start()
          this.uploadIsRunning = true
        })
      }
  }
};
</script>
  
<style>
.vfa-demo {
    position: relative;
}

.vfa-demo .file-preview-wrapper::before {
    background: transparent;
}

.vfa-demo .file-row {
    position: relative;
    z-index: 15;
    line-height: 24px;
    text-align: left;
    background: #EEE;
    margin-bottom: 5px;
    padding: 2px 5px;
}

.vfa-demo .remove {
    float: right;
    margin-top: -3px;
}

.vfa-demo .file-progress {
    position: static !important;
    float: right !important;
    width: 85px !important;
    height: 10px !important;
    margin-top: 7px !important;
    margin-right: 10px !important;
    border: 1px solid #AAA !important;
}

.vfa-demo .file-progress .file-progress-bar {
    background: #25acfa !important;
}

.vfa-demo .file-progress.completed {
    display: none; 
}

.vfa-demo .drop-help-text {
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    margin: 2px;
    background: rgba(255, 255, 255, 0.75);
    z-index: 1200;
    font-size: 32px;
    font-weight: bold;
    color: #888;
    align-items: center;
    justify-content: center;
    display: none;
}

.vfa-demo .is-drag-over .drop-help-text {
    display: flex;
}

.vfa-demo .upload-block  {
    border: 2px dashed transparent;
    padding: 20px;
    padding-top: 0;
}

.vfa-demo .is-drag-over.upload-block {
    border-color: #AAA;
}

.vfa-demo .vue-file-agent {
    border: 0 !important;
    box-shadow: none !important;
}
</style>
  