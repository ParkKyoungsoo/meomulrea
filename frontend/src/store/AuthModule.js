import * as firebase from 'firebase'

const AuthModule = {
  state: {
    user: null
  },
  // mutations: {
  //   setUser (state, payload) {
  //     state.user = payload
  //     const userListRef = firebase.database().ref('presence')
  //     const myUserRef = userListRef.push()

  //     firebase.database().ref('.info/connected')
  //       .on(
  //         'value', function (snap) {
  //           if (snap.val()) {
  //             // if we lose network then remove this user from the list
  //             myUserRef.onDisconnect()
  //               .remove()
  //             // set user's online status
  //             let presenceObject = {user: payload, status: 'online'}
  //             myUserRef.set(presenceObject)
  //           } else {
  //             // client has lost network
  //             let presenceObject = {user: payload, status: 'offline'}
  //             myUserRef.set(presenceObject)
  //           }
  //         }
  //       )
  //   }
  // },
  actions: {
    // signUserUp ({commit}, payload) {
    //   commit('setLoading', true)
    //   commit('clearError')
    //   firebase.auth().createUserWithEmailAndPassword(payload.email, payload.password)
    //     .then(
    //       auth => {
    //         console.log("auth email : "+auth.user.email)
    //         console.log("auth password : "+payload.password)
    //         console.log("auth username : "+payload.username)
    //         firebase.database().ref('users').set({
    //           name: payload.username,
    //           email: auth.user.email,
    //           password: payload.password
    //         })  // 얘가 유저 테이블
    //           .then(
    //             () => {
    //               commit('setLoading', false)
    //       //         const newUser = {
    //       //           id: auth.user.uid,
    //       //           username: payload.username
    //       //         }
    //               // commit('setUser', newUser)
    //             }
    //           )
    //           .catch(
    //             // error => {
    //             //   commit('setLoading', false)
    //             //   commit('setError', error)
    //             //   console.log('AuthModule.js signUserUp 에러')
    //             // }
    //           )
    //       }
    //     )
    //     .catch(
    //       error => {
    //         commit('setLoading', false)
    //         commit('setError', error)
    //         console.log('여기 에러')
    //       }
    //     )
    // },
    signUserIn ({commit}, payload) {
      commit('setLoading', true)
      commit('clearError')
      firebase.auth().signInWithEmailAndPassword(payload.email, payload.password)
        .then(
          auth => {
            firebase.database().ref('users').child(auth.user.uid).once('value', function () {
              commit('setLoading', false)
              const newUser = {
                id: auth.user.uid,
                username: auth.user.email
              }
              commit('setUser', newUser)
            })
          }
        )
        .catch(
          error => {
            commit('setLoading', false)
            commit('setError', error)
            console.log('AuthModule.js signUserIn 에러')
          }
        )
    }
  },
  getters: {
    user (state) {
      return state.user
    }
  }
}

export default AuthModule