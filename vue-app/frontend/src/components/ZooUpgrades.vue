<template>
  <div>
    <h1>Zoo Upgrades</h1>
    <ul>
      <li v-for="upgrade in availableUpgrades" :key="upgrade.id">
        {{ upgrade.name }} - Cost: ${{ upgrade.cost }}
        <button @click="purchaseUpgrade(upgrade)">Buy</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ZooUpgrades',
  data() {
    return {
      availableUpgrades: [
        { id: 1, name: 'Enhanced Feeding', cost: 50 },
        { id: 2, name: 'Automatic Watering System', cost: 100 }
      ],
      purchasedUpgrades: []
    };
  },
  methods: {
    purchaseUpgrade(upgrade) {
      this.$emit('purchase-upgrade', upgrade);
    }
  }
};
</script>