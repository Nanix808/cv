import {DefaultApiInstance} from './apiinstanse.js'


export const UrlApi = {

    postResume(body) {
        const url = '/resume';
        return DefaultApiInstance.post(url,body)
    },
}
