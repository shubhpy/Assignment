<template>
  <div class="col-md-6 col-lg-5 col-xl-4 align-self-center">
    <div class="px-80 py-30">
      <h4>Login</h4>
      <br />
      <form>
        <div class="form-group do-float">
          <label>Username</label>
          <input type="text" class="form-control" name="email" v-model="uname" />
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
          <button class="btn btn-bold btn-block btn-primary" type="submit" @click="registerMethod">Register</button>
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
        uname : '',
        pwd : ''
      }
    },
  methods: {
      loginMethod: function(e) {
        e.preventDefault();
        if (this.uname!='' && this.pwd!=''){        
          console.log("Logging Here");
          var formData = new FormData();
          formData.append('username', this.uname);
          formData.append('password', this.pwd);        
          // formData.append('dict', {heelo:"Helllo"});
          // formData.append('list', ["Heeyy","heyyy"]);
          
          this.$http.post(this.$hostname + 'login/',formData)
          .then(function (data) {
            console.log(data.body);
            if (data.body.success && !data.body.error){          
              localStorage.setItem('token',data.body.token);
              router.push({ name: "Dashboard"});
            }else{
              alert(data.body.message)            
            }
          }.bind(this),function(data){
            console.log("In bind")
            console.log(data.body);
          })
        }else{
            alert("Fill both fields")          
        }
      },

      registerMethod:function(e) {
        e.preventDefault();
        console.log("Routing to register");
        router.push({ name: "Register"});
      }

    },
  created () {
    if(localStorage.getItem('token')){
      console.log("Token Found");
      router.push({ name: "Dashboard"});
    }else{
      console.log("I m here")
      // router.push({ name: "Login"});
    }
  }
}
</script>

<style>
</style>