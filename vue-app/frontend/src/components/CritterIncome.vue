    <template>
      <div>
        <h1>Critter Income Generation</h1>
        <ul>
          <li v-for="critter in critters" :key="critter.id">
            {{ critter.name }}: ${{ critter.income }} per hour
          </li>
        </ul>
        <ZooUpgrades @purchase-upgrade="handlePurchase" />
      </div>
    </template>

    <script>
    import axios from 'axios';
    import ZooUpgrades from './ZooUpgrades.vue';

    export default {
      name: 'CritterIncome',
      components: {
        ZooUpgrades
      },
      data() {
        return {
          critters: [],
          funds: 0
        };
      },
      mounted() {
        this.fetchCritterIncomes();
      },
      methods: {
        async fetchCritterIncomes() {
          try {
            const response = await axios.get(`${process.env.VUE_APP_API_URL}/critters/income`);
            this.critters = response.data;
            this.updateFunds(); // Placeholder for updating funds based on critter incomes
          } catch (error) {
            console.error('Error fetching critter incomes:', error);
          }
        },
        updateFunds() {
          // Logic to update player funds based on critter income
          this.funds += this.critters.reduce((total, critter) => total + critter.income, 0);
        },
        handlePurchase(upgrade) {
          if (this.funds >= upgrade.cost) {
            this.funds -= upgrade.cost;
            // Logic to apply the upgrade effect on gameplay
            console.log(`Purchased ${upgrade.name}!`);
          } else {
            console.log('Insufficient funds!');
          }
        }
      },
      provide() {
        return {
          funds: this.funds,
          handlePurchase: this.handlePurchase
        };
      }
    }
    </script>