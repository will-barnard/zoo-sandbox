<template>
  <div class="critter">
    <h2>{{ critter.name }}</h2>
    <p>Price: ${{ critter.price }}</p>
    <button @click="buyCritter" :disabled="!canBuy">Buy</button>
    <button @click="placeInZoo" :disabled="!isOwned || isInZoo">Place in Zoo</button>
    <p>Income: ${{ critter.income }} per second</p>
  </div>
</template>

<script>
export default {
  props: {
    critter: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      ownedCritters: []
    };
  },
  computed: {
    canBuy() {
      return this.$root.balance >= this.critter.price;
    },
    isOwned() {
      return this.ownedCritters.includes(this.critter.id);
    },
    isInZoo() {
      return this.$root.zoo.includes(this.critter.id);
    }
  },
  methods: {
    buyCritter() {
      if (this.canBuy) {
        this.$root.balance -= this.critter.price;
        this.ownedCritters.push(this.critter.id);
      }
    },
    placeInZoo() {
      if (!this.isInZoo && this.isOwned) {
        this.$root.zoo.push(this.critter.id);
        setInterval(() => {
          this.$root.balance += this.critter.income;
        }, 1000);
      }
    }
  }
};
</script>

<style scoped>
.critter {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}
</style>
