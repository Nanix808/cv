import {DefaultApiInstance} from './apiinstanse.js'





export const UrlApi = {


    postResume(data) {
        const url = '/offer/all/';
        return DefaultApiInstance.post(url, data)
    },


    getResume(){
        const url = '/customer/all/';
        return DefaultApiInstance.get(url)

    },




}


