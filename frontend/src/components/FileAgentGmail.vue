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
          uploadUrl:'http://localhost:8000/multipart'
      }
  },
  methods: {
      removeFileRecord: function(fileRecord){
          return this.$refs.vfaDemoRef.removeFileRecord(fileRecord);
      },
      handleFileSelected(slotProps) {
        this.slots = slotProps; 
      },
      onSelect: function(fileRecords){
        var file = fileRecords[0]

        // Create a new tus upload
        var upload = new tus.Upload(file, {
          // Endpoint is the upload creation URL from your tus server
          endpoint: this.uploadUrl,
          // Retry delays will enable tus-js-client to automatically retry on errors
          retryDelays: [0, 3000, 5000, 10000, 20000],
          // Attach additional meta data about the file for the server
          metadata: {
            filename: file.name,
            filetype: file.type,
          },
          // Callback for errors which cannot be fixed using retries
          onError: function (error) {
            console.log('Failed because: ' + error)
          },
          // Callback for reporting upload progress
          onProgress: function (bytesUploaded, bytesTotal) {
            var percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2)
            console.log(bytesUploaded, bytesTotal, percentage + '%')
          },
          // Callback for once the upload is completed
          onSuccess: function () {
            console.log('Download %s from %s', upload.file.name, upload.url)
          },
        })

        // Check if there are any previous uploads to continue.
        upload.findPreviousUploads().then(function (previousUploads) {
          // Found previous uploads so we select the first one.
          if (previousUploads.length) {
            upload.resumeFromPreviousUpload(previousUploads[0])
          }

          // Start the upload
          upload.start()
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
  