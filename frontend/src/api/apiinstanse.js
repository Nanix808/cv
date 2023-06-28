import axios, { AxiosInstance } from 'axios'
// import  store  from '../store';


const baseURL = window.location.hostname === 'localhost' ? 'http://127.0.0.1:8000' : 'https://python.3s.by'


// const apiClient = axios.create({
//     baseURL: 'https://api.openbrewerydb.org',
//     headers: {
//       'Content-type': 'application/json',
//     },
//   })
  
// export default apiClient

const defaultConfig = {
    baseURL: baseURL,
    headers: {
        'Content-Type': 'application/json'
    }
}
const DefaultApiInstance = axios.create(defaultConfig)

// DefaultApiInstance.interceptors.response.use(undefined, (error) => {
//                     if (error.response && error.response.status === 401) {
//                         store.commit('showModal', "Зарегистрируйтесь")
//                         store.commit('authModule/delToken');
//                     }
//                     return Promise.reject(error.response.data);
//                 });


export {DefaultApiInstance}



