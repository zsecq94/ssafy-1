<template>
  <div>
    <div class="position-absolute top-50 start-50 translate-middle" style="margin-top:20px; width: fit-content;">
      <div style="background-color: skyblue; padding: 50px; width:500px; border-top-left-radius: 30px; border-top-right-radius: 30px;">
        <h1>보고싶은 영화 리스트</h1>
        <WatchListForm/>
      </div>
      <div style="background-color:gainsboro ">
        <WatchListItem
          v-for="(input, index) in inputData"
          :key="index"
          :input="input"        
        />
      </div>
    </div>
  </div>
</template>

<script>


import WatchListForm from '@/components/WatchListForm.vue';
import WatchListItem from '@/components/WatchListItem.vue';

export default {
  name: 'WatchListView',
  components:{
    WatchListItem,
    WatchListForm,
  },
  computed:{
    inputData(){
      return this.$store.state.inputData
    }
  }
}
</script>

<style>

</style>