<template>
  <Navbar />
  <router-view/>
</template>


<script>
  import Navbar from "./components/base/Navbar"
  import axios from "axios"

  export default {
    name: "App",
    components: {
      Navbar,
    },
    methods: {
    },
    data() {
      return {
      }
    }
  }
</script>

<style lang="scss">
  @import "../node_modules/tailwindcss";
  body, html {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
  }
</style>
