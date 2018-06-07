// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Resource from 'vue-resource';
import Element from "element-ui";
import en from "element-ui/lib/locale/lang/en";

Vue.use(Element, { locale: en });
Vue.use(Resource);
Vue.config.productionTip = false;
Vue.http.options.emulateJSON = true;

// Vue.prototype.$hostname = "http://localhost:8000/";
Vue.prototype.$hostname = "http://13.126.11.145:8088/";

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})