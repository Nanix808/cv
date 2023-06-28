import axios from "axios"
import  store  from '../store';


const baseURL = window.location.hostname === 'localhost' ? 'http://127.0.0.1:8000' : 'https://python.3s.by'
// console.log(baseURL, window.location.hostname)

const loginConfig = {
    baseURL: baseURL,
    headers: {
        'Content-Type': 'application/json'
    }
}
const LoginApiInstance = axios.create(loginConfig)

export {LoginApiInstance}


const defaultConfig = {
    baseURL: baseURL,
    headers: {
        'Content-Type': 'application/json'
    }
}
const DefaultApiInstance = axios.create(defaultConfig)

DefaultApiInstance.interceptors.response.use(undefined, (error) => {
                    if (error.response && error.response.status === 401) {
                        store.commit('showModal', "Зарегистрируйтесь")
                        store.commit('authModule/delToken');
                    }
                    return Promise.reject(error.response.data);
                });


export {DefaultApiInstance}



