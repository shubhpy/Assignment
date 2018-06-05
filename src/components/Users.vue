<template>
<div class="main-content p-0">
  <div class="card h-fullscreen pt-5 mb-0">
    <div class="card-body pl-3 pr-3 pt-5">
      <table id="user" class="table table-striped table-bordered dataTable display" cellspacing="0" cellpadding="0">
        <thead>
          <tr role="row">
            <th class="th-1 sorting_asc" tabindex="0" aria-controls="DataTables_Table_0" rowspan="1" colspan="1" aria-sort="ascending">Sr. No.</th>
            <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0" rowspan="1" colspan="1">Name</th>
            <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0" rowspan="1" colspan="1">Email</th>
            <th class="sorting" tabindex="0" aria-controls="DataTables_Table_0" rowspan="1" colspan="1">Status</th>
            <th class="th-modify sorting" tabindex="0" aria-controls="DataTables_Table_0" rowspan="1" colspan="1">Modify</th>
          </tr>
        </thead>
        <tbody>
          <tr role="row" class="odd" ><!-- *ngFor="let d of data; let i = index;trackBy: trackByFn" {{d}} -->
            <td class="sorting_1">SNO</td>
            <td>name</td>
            <td>email</td>
            <td>Active</td>
            <td class="text-left">
              <!-- <a class="btn btn-w-md btn-info nav-action d-inline text-white" data-toggle="modal" data-target="#edit-user"><span class="ti-pencil"></span></a> -->
              <a class="btn btn-w-md btn-danger nav-action d-inline text-white" @click="remove(t.user_id)"><span class="ti-close"></span></a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Users',
  created () {
    this.$data.fetchList(this.$hostname + 'getnames', names).then(val => {})
    // fetch(this.$hostname + 'getnames')
    .then(val => {
        console.log(val)
        if (val.success){
          console.log("Data Received")   
        }else{
          alert("API is working")
        }
    })
      // .then(response => response.json())
    //   .then(json => {
        // console.log(json)
        // if (json.success){
        //   console.log("Data Received")   
        // }else{
        //   alert("API is working")
        // }
    // })
  }
}
</script>

<style>
</style>