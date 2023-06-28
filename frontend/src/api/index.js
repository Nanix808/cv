import {LoginApiInstance, DefaultApiInstance} from './apiinstanse.js'





export const AuthApi = {

    login(email, password) {
        const url = '/auth/token/login/';
        const data = {email, password}
        return LoginApiInstance.post(url, data)
    },

    logout(){
        const url = '/auth/token/logout/';
        return DefaultApiInstance.post(url)

    },

    getOffer(params) {
        const url = '/offer/all/';
        return DefaultApiInstance.get(url, { params })
    },

    postOffer(data) {
        const url = '/offer/all/';
        return DefaultApiInstance.post(url, data)
    },


    getCustomer(){
        const url = '/customer/all/';
        return DefaultApiInstance.get(url)

    },




}


