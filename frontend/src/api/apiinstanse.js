import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api/v2/'

const defaultConfig = {
    baseURL: baseURL,
    headers: {
        'Content-Type': 'application/json'
    }
}
const DefaultApiInstance = axios.create(defaultConfig)
export {DefaultApiInstance}



