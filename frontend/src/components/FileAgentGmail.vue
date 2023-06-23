<template>
    <div class="vfa-demo bg-light pt-3">
        <VueFileAgent
          ref="vfaDemoRef"
          :uploadUrl="'http://localhost:8000/multipart'"
          :uploadHeaders="{}"
          :multiple="true"
          :deletable="true"
          :theme="'list'"
          v-model="fileRecords"
        >
        <!-- <template v-slot:file-preview="slotProps">
          <v-list-item
            v-for="(item, index) in slotProps"
            :key="index"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </template> -->
        <template v-slot:file-preview-new>
          <div  class="d-flex justify-space-around" key="new">
            <!-- <a href="#" class="">Select files</a> or drag & drop here -->
            <svg-icon type="mdi" href="#" class="" :path="path"></svg-icon>
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


        <v-menu light max-width="1000">
            <template v-slot:activator="{ props }">
              <v-btn
                rounded="pill"
                class="transparent"
                icon=""
                size="x-small"
                dark
                elevation="0"
                v-bind="props"
              >
  
                <i class="tio- text-primary text-20">fileupload</i>
              </v-btn>
            </template>
            <div class="fileupload-menu">
              <h4 class="ma-3 text-subtitle-2 font-weight-bold">File Uploads</h4>
              <v-divider></v-divider>
              <v-list >
                <v-list-item-group>
                <v-list-item>
                  <VueFileAgent
                    class="upload-block"
                    ref="vfaDemoRef"
                    :uploadUrl="'http://localhost:8000/multipart'"
                    :uploadHeaders="{}"
                    :multiple="true"
                    :deletable="true"
                    :theme="'list'"
                    v-model="fileRecords"
                    @selected="handleFileSelected"
                  >
                  <template v-slot:file-preview-new>
                    <div  class="d-flex justify-space-around" key="new">
                      <!-- <a href="#" class="">Select files</a> or drag & drop here -->
                      <svg-icon type="mdi" href="#" class="" :path="path"></svg-icon>
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
                </v-list-item>
                    <!-- <template v-slot:file-preview="slotProps">
                      <v-list-item :key="slotProps.index" class="grid-box-item file-row">
                        <v-btn icon class="close remove" aria-label="Remove" @click="removeFileRecord(slotProps.fileRecord)">
                          <span aria-hidden="true">&times;</span>
                        </v-btn>
                        <div class="file-progress" :class="{'completed': slotProps.fileRecord.progress() == 100}">
                          <div class="file-progress-bar" role="progressbar" :style="{width: slotProps.fileRecord.progress() + '%'}"></div>
                        </div>
                        <strong>{{ slotProps.fileRecord.name() }}</strong> <span class="text-muted">({{ slotProps.fileRecord.size() }})</span>
                      </v-list-item>
                    </template > -->
                    <v-list-item v-slot:file-preview="slotProps">
                    <div :key="slotProps.index" >
                      <v-list-title>{{ slotProps.fileRecord.name() }}</v-list-title> <v-list-content>({{ slotProps.fileRecord.size() }})</v-list-content>
                    </div>
                </v-list-item>
              </v-list-item-group>
                </v-list>
            </div>
          </v-menu>
    </div>
</template>
  
<script>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiFileUpload } from '@mdi/js';
export default {
  name: "FileAgent",
  components: {
    SvgIcon
  },
  data(){
      return {
          path: mdiFileUpload,
          fileRecords: [],
          fileAgentProps: null,
          files: [],
          items: [
            { title: 'Click Me1' },
            { title: 'Click Me2' },
            { title: 'Click Me3' },
            { title: 'Click Me4' },
          ],
          slots: []
      }
  },
  methods: {
      removeFileRecord: function(fileRecord){
          return this.$refs.vfaDemoRef.removeFileRecord(fileRecord);
      },
      handleFileSelected(slotProps) {
        this.slots = slotProps; 
      },
      handleFileAgentProps(slotProps) {
        console.log(slotProps)
        this.fileAgentProps = slotProps;
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
  