<template>
  <div id="app">
    <CritterMarket />
    <ZooDisplay />
  </div>
</template>

<script>
import CritterMarket from './components/CritterMarket.vue'
import ZooDisplay from './components/ZooDisplay.vue'

export default {
  name: 'App',
  components: {
    CritterMarket,
    ZooDisplay
  }
}
</script>