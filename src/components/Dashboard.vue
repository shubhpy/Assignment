<template>
<div>
    <div class="col-md-10 col-lg-20 col-xl-20 align-self-center">
        <div class="px-80 py-30">
            <div class="form-group do-float">
                <label>Enter webiste url</label>
                <input type="text" class="form-control" name="website" v-model="website"/>
            </div>

            <div class="form-group">
                <button class="btn btn-bold btn-block btn-primary" type="submit" @click="submitWebsite">Submit to Get Address</button>
            </div>
        </div>
    </div>
    <header class="topbar">
    <div class="topbar-right">
        <a class="topbar-btn text-white" data-toggle="quickview" @click="logout">Logout<i class="ti-power-off"></i></a>
    </div>
    </header>
    <main class="main-container">
        <router-view></router-view>
    </main>
</div>
</template>
<script>
    import router from '../router'
    export default {
    name: 'Dashboard',
    methods : {
        logout: function(e) {
        e.preventDefault();
        localStorage.removeItem('token');
        router.push({ name:"Login"});
        }
    }
}
</script>

<style>
    .menu-category::after
    {
        top: 60%;
    }
    .dataTables_wrapper .dataTables_paginate .paginate_button:hover{
        background-color:transparent;
        background:transparent;
    }
</style>