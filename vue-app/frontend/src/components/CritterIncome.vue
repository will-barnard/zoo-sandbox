    <template>
      <div>
        <h1>Critter Income Generation</h1>
        <ul>
          <li v-for="critter in critters" :key="critter.id">
            {{ critter.name }}: ${{ critter.income }} per hour
          </li>
        </ul>
      </div>
    </template>

    <script>
    import axios from 'axios';

    export default {
      name: 'CritterIncome',
      data() {
        return {
          critters: []
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
          } catch (error) {
            console.error('Error fetching critter incomes:', error);
          }
        }
      }
    }
    </script>
    