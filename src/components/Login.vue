<template>
  <div class="col-md-6 col-lg-5 col-xl-4 align-self-center">
    <div class="px-80 py-30">
      <h4>Login</h4>
      <br />
      <form>
        <div class="form-group do-float">
          <label>Username</label>
          <input type="text" class="form-control" name="email" v-model="email" />
        </div>
        <div class="form-group do-float">
          <label>Password</label>
          <input type="password" class="form-control" name="pwd" v-model="pwd" />
        </div>
        <div class="form-group">
          <button class="btn btn-bold btn-block btn-primary" type="submit" @click="loginMethod">Login</button>
        </div>
        <div class="form-group">
          <label>OR</label>
          <button class="btn btn-bold btn-block btn-primary" type="submit" @click="loginMethod">Register</button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<script>
  import router from '../router'

export default {
  name: 'LoginComponent',
  data() {
      return {
        email : '',
        pwd : ''
      }
    },
  methods: {
      loginMethod: function(e) {
        e.preventDefault();
        console.log("Logging Here");
        // console.log($http.get);
        // console.log($http.post);
        // var datatosend = {
        //   email : this.uname,
        //   pwd : this.pwd
        //   // dict : {heelo:"Helllo"},
        //   // list : ["Heeyy","heyyy"]
        // };

        // console.log(datatosend);

        var formData = new FormData();
        formData.append('email', this.email);
        formData.append('pwd', this.pwd);        
        // formData.append('dict', {heelo:"Helllo"});
        // formData.append('list', ["Heeyy","heyyy"]);
        
        // this.$http.post('http://localhost:8000/login',formData)
        // .then(function (data) {
        //   console.log(data.body);
          // localStorage.setItem('token',data.body.token);
          router.push({ name: "Dashboard"});
          // this.boardPersons.push(this.newPerson);
          // this.suggestions.push({item:this.newPerson,quantity:''});
        // }.bind(this),function(data){
        //   console.log("In bind")
        //   console.log(data.body);
        // })
      }
    },
  created () {
    if(localStorage.getItem('token')){
      console.log("Token Found");
      router.push({ name: "Dashboard"});      
    }else{
      router.push({ name: "Login"});
    }
  }
}
</script>

<style>
</style>