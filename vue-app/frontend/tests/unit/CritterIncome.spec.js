    import { mount } from '@vue/test-utils';
    import CritterIncome from '@/components/CritterIncome.vue';

    describe('CritterIncome.vue', () => {
      let wrapper;
      const mockCritters = [
        { id: 1, name: 'Monkey', income: 10 },
        { id: 2, name: 'Giraffe', income: 15 }
      ];

      beforeEach(() => {
        jest.mock('axios');
        axios.get.mockResolvedValue({ data: mockCritters });

        wrapper = mount(CritterIncome);
      });

      it('should display critters and their incomes', async () => {
        await wrapper.vm.fetchCritterIncomes();
        const items = wrapper.findAll('li');
        expect(items.length).toBe(mockCritters.length);

        items.wrappers.forEach((item, index) => {
          expect(item.text()).toContain(mockCritters[index].name);
          expect(item.text()).toContain(`$${mockCritters[index].income} per hour`);
        });
      });

      it('should update funds based on critter incomes', async () => {
        await wrapper.vm.fetchCritterIncomes();
        const totalIncome = mockCritters.reduce((total, critter) => total + critter.income, 0);
        expect(wrapper.vm.funds).toBe(totalIncome);
      });

      it('should display error message on API failure', async () => {
        axios.get.mockRejectedValue(new Error('API error'));
        await wrapper.vm.fetchCritterIncomes();
        expect(console.error).toHaveBeenCalledWith(expect.stringContaining('Error fetching critter incomes:'));
      });
    });
    