<template>
<div>
    <div class="col-md-11 col-lg-25 col-xl-25 align-self-center">
        <div class="px-80 py-30 pr-2">
            <div class="form-group do-float">
                <label>Enter webiste url</label>
                <input type="text" class="form-control" name="weburl" v-model="weburl"/>
            </div>                
            <div class="form-group">
                <button class="btn btn-bold btn-block btn-primary" type="submit" @click="submitWebsite">Submit to Get Address</button>
                <div v-if="fetching">
                    <label> Fetching address... </label>    
                </div>
                <div v-if="fetched">
                    <table id="Address" class="table table-striped table-bordered dataTable display" cellspacing="0" cellpadding="0">
                        <thead>
                            <tr role="row">
                                <th class="th-1">Sr. No.</th>
                                <th><p class="p-0 m-0 sm">Address</p></th>
                            </tr>
                        </thead>
                        <tbody>
                        <tr role="row" class="odd" v-for="(addr,index) in address_list" :key="addr.index">
                            <td class="col-sm-1">{{index+1}}</td>
                            <td class="col-sm-9">{{addr}}</td>
                        </tr>
                        </tbody>
                    </table>    
                </div>
            </div>
        </div>
    </div>
    <div class="float-left pt-5 mt-5">
        <button type="submit" class="btn btn-bold btn-block btn-primary mt-5" @click="clearPage" >Clear</button>
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
    data() {
      return {
        weburl : '',
        address_list : [], 
        // ["\n\nValiance Solutions Pvt. Ltd, A-75, First Floor, Sector-58\nNoida-201301\n\n", "\n\n\nAddress:\n\n\n\n\n\nValiance Solutions Pvt. Ltd, A-75, First Floor, Sector-58\nNoida-201301\n\n\n", "\nValiance Solutions Pvt. Ltd, A-75, First Floor, Sector-58\nNoida-201301\n", "\n\n\nValiance Solutions Pvt. Ltd, A-75, First Floor, Sector-58\nNoida-201301\n\n\n", "Valiance Solutions Pvt. Ltd, A-75, First Floor, Sector-58\nNoida-201301"],
        fetching : false,
        fetched :false
      }
    },
    methods : {
        logout: function(e) {
            e.preventDefault();
            localStorage.removeItem('token');
            router.push({ name:"Login"});
        },
        submitWebsite:function(e) {
            if (this.weburl!=''){
                e.preventDefault();
                if (this.fetched){
                    this.address_list = []
                    this.fetched = false
                }
                this.fetching = true
                var token = localStorage.getItem('token');
                console.log("Submitting URL");

                var formData = new FormData();
                formData.append('url', this.weburl);
                // formData.append('dict', {heelo:"Helllo"});
                // formData.append('list', ["Heeyy","heyyy"]);
                
                this.$http.post(this.$hostname + 'getAddress/',formData,{headers: {Authorization: token}})
                .then(function (data) {
                    console.log(data.body);
                    if (data.body.success && !data.body.error){
                        this.fetching = false
                        this.address_list = data.body.address_list
                        this.fetched = true
                    }else{
                        alert(data.body.message)
                        this.clearPage()
                    }
                }.bind(this),function(data){
                    console.log("In bind")
                    console.log(data.body);
                })
            }
        },
        clearPage: function(e) {
            this.weburl = ''
            this.address_list = []
            this.fetching = false
            this.fetched = false
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