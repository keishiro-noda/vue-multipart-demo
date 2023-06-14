<template>
  <div>
    <VueFileAgent
      :uploadUrl="'http://localhost:8000/multipart'"
      :uploadHeaders="{}"
      :multiple="true"
      :deletable="true"
      :editable="true"
      :meta="true"
      :maxFiles="8"
      :helpText="'Select files'"
      :errorText="{
        type: 'Please select images, videos, pdf or zip files',
        size: 'You selected a larger file!',
      }"
      :thumbnailSize="120"
      :theme="'list'"
      v-model="fileRecords"
    ></VueFileAgent>
  </div>
</template>

<script>
export default {
  name: "FileAgent",
  data() {
    return {
      fileRecords: []
    };
  },
  
};
</script>

<style scoped>
#profile-pic-demo .drop-help-text {
  display: none;
}
#profile-pic-demo .is-drag-over .drop-help-text {
  display: block;
}
#profile-pic-demo .profile-pic-upload-block {
  border: 2px dashed transparent;
  padding: 20px;
  padding-top: 0;
}

#profile-pic-demo .is-drag-over.profile-pic-upload-block {
  border-color: #AAA;
}
#profile-pic-demo .vue-file-agent {
  width: 180px;
  float: left;
  margin: 0 15px 5px 0;
  border: 0;
  box-shadow: none;
}
</style>

