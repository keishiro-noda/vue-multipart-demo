<template>
    <div class="vfa-demo bg-light pt-3">
        <VueFileAgent
          class="upload-block"
          ref="vfaDemoRef"
          :uploadUrl="'http://localhost:8000/multipart'"
          :uploadHeaders="{}"
          :multiple="true"
          :deletable="true"
          :theme="'list'"
          v-model="fileRecords"
        >
          <template v-slot:file-preview="slotProps">
            <div :key="slotProps.index" class="grid-box-item file-row">
              <button type="button" class="close remove" aria-label="Remove" @click="removeFileRecord(slotProps.fileRecord)">
                <span aria-hidden="true">&times;</span>
              </button>
              <div class="file-progress" :class="{'completed': slotProps.fileRecord.progress() == 100}">
                <div class="file-progress-bar" role="progressbar" :style="{width: slotProps.fileRecord.progress() + '%'}"></div>
              </div>
              <strong>{{ slotProps.fileRecord.name() }}</strong> <span class="text-muted">({{ slotProps.fileRecord.size() }})</span>
            </div>
          </template >
          <template v-slot:file-preview-new>
            <div class="text-left my-3" key="new">
              <a href="#" class="">Select files</a> or drag & drop here
            </div>
          </template >
          <template v-slot:after-outer>
            <div title="after-outer">
              <div class="drop-help-text">
                <p>Drop here</p>
              </div>
            </div>
          </template >
        </VueFileAgent>
    </div>
</template>
  
<script>
  export default {
    name: "FileAgent",
    data(){
        return {
            fileRecords: []
        }
    },
    methods: {
        removeFileRecord: function(fileRecord){
            return this.$refs.vfaDemoRef.removeFileRecord(fileRecord);
        },
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
  