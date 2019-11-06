export default {
    setApiList(state, payload) {
        state.ApiLists = payload.map(m => m)
    },
    setNewApi(state, payload) {
        state.ApiLists.push(payload)
        state.postData = true
    },
    setAddApi(state, payload) {
        state.addApi.push(payload)
    },
    resetAddApi(state, payload) {
        state.addApi = []
    },
    reApi(state, payload) {
        state.reApiList = state.ApiLists.concat(state.addApi)
        state.postData = true
    }
}
