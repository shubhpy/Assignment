<template>
  <div class="col-md-6 col-lg-5 col-xl-4 align-self-center">
    <div class="px-80 py-30">
      <h4>Register Here</h4>
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
          <button class="btn btn-bold btn-block btn-primary" type="submit" @click="registerNewUser">Register</button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<script>
  import router from '../router'

export default {
  name: 'Register',
  data() {
      return {
        uname : '',
        pwd : ''
      }
    },
  methods: {
      registerNewUser: function(e) {
        e.preventDefault();
        console.log("Registering Here");
        var formData = new FormData();
        formData.append('username', this.uname);
        formData.append('password', this.pwd);        
        // formData.append('dict', {heelo:"Helllo"});
        // formData.append('list', ["Heeyy","heyyy"]);
        
        this.$http.post(this.$hostname + 'register/',formData)
        .then(function (data) {
          console.log(data.body);
          if (data.body.success && !data.body.error){
            console.log("Registered")
            alert("Registered, Login to enter")
            router.push({ name: "Login"});
          }else{
            alert(data.body.message)
          }
        }.bind(this),function(data){
          console.log("In bind")
          console.log(data.body);
        })
      }
    }
}
</script>

<style>
</style>