/* eslint-disable import/namespace */
import Vuex from 'vuex'
import * as Tus from 'tus-js-client'


const store = new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {
    upload({ commit }, { file, params }) {
      return new Promise((resolve, reject) => {
        // Option setting
        const options = {
          endpoint: `http://localhost:8000/multipart`,
          fingerprint: file => file.name,
          chunkSize: 1024 * 1024 * 1,
          metadata: {
            filename: file.name
          },
          retryDelays: [0, 3000, 5000, 10000, 20000],
          resume: true,
          onError: function(error) {
            console.log('Failed because: ' + error)
            reject(error)
          },
          onProgress: function(bytesUploaded, bytesTotal) {
            const percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2)
            console.log(bytesUploaded, bytesTotal, percentage + '%')
          },
          onSuccess: function() {
            console.log('Download from %s complete', upload.url)
            resolve(upload.url)
          }
        }
        // Create a new tus upload
        const upload = new Tus.Upload(file, options)
        // Start the upload
        upload.start()
      })
    }
  }
})

export default store;
