import seaborn as sns
import matplotlib.pyplot as plt

# Farm contains
# - season
# - money
# - field
# - field size 
# - tend (harvest, call plant, water)
# - plant (buy, plant in field)
# - change seasons
# - simulation methods
#   - run_step
#   - run_simulation
# - plot methods
#   - plot_crops
#   - plot_money
# - get valid crops (based on money and days left)

class Farm:
    def __init__(self, season):
        self.season = season
        self.money = 650
        self.field = []
        self.field_size = 135
        self.season_gains = []
        self.gains = [self.money]
        self.total_days = 0
        self.color = 0
        self.pallette = sns.color_palette("husl", 4)


    def tend(self):
        still_growing = []
        for crop in self.field:
            gains = crop.harvest()
            if gains:
                self.money += gains
                if crop.regrow_days:
                    still_growing.append(crop)
            else:
                still_growing.append(crop)
               
        self.field = still_growing
        
        if self.season.sell_day():
            self.plant()
        
        for crop in self.field:
            crop.water()
        

    def plant(self):
        crops = self.season.get_crops()
        
        valid_crops = self.get_valid_crops()
        while (self.money > 0 and len(valid_crops) > 0 and len(self.field) < self.field_size):
            valid_crops = self.get_valid_crops()
            if len(valid_crops) > 0:
                # OPTIONAL CHOICES
                # choice = get_most_profitable(valid_crops) # raw buy-sell
                # choice = get_cheapest(valid_crops)
                # choice = get_smallest_grow_time(valid_crops) 
                # choice = get_expensive(valid_crops)
                # choice = get_longest_grow_time(valid_crops)

                # best boi 
                choice = get_highest_seasonal_profit(valid_crops, self.season.days - self.season.current_day)

                # buy seed and plant in field
                self.money -= choice.buy_price
                self.field.append(choice)


    def run_step(self):
        print()
        print("DAY", self.season.current_day, "| MONEY: $", round(self.money, 2))
        print("# of CROPS: ", len(self.field))
        
        self.tend()
        # for crop in self.field:
        #     print(crop)
        
        # self.plot_money()
        
        self.total_days += 1
        self.gains.append(self.money)
        self.plot_crops() 
        self.season.next_day()
        

    def run_simulation(self):
        while self.season.current_day <= self.season.days:
            self.field_size += 3
            self.run_step()

        print()
        print("FINAL MONEY: $", round(self.money, 2))  


    def plot_crops(self):
        crop_names = [crop.name for crop in self.season.crops]
        field_crops = [crop.name for crop in self.field]
        crop_totals = [field_crops.count(crop) for crop in crop_names]
      
        sns.barplot(y=crop_names, x=crop_totals)
        plt.yticks(rotation=30, ha='right', fontsize=8)
        plt.xlabel('Total')
        plt.ylabel('Crop')
        plt.title(f'Total of Each Plant {self.season.name} Day {self.season.current_day}')
        plt.pause(0.3)
        plt.clf()
    

    def plot_money(self, update=True):
        sns.lineplot(x=range(self.total_days + 1), y=self.gains, label=self.season.name, color=self.pallette[self.color])
        for gains in self.season_gains:
            sns.lineplot(x=gains[0], y=gains[1], label=gains[2], color=gains[3])

        plt.xlabel('Days')
        plt.ylabel('Money')
        plt.title(f'Money Over Time')
        if update:
            plt.pause(0.3)
            plt.clf()
        else:
            plt.show()


    def change_seasons(self, season):
        print("SEASON CHANGE: ", season.name)
        start = self.total_days - self.season.days
        end = self.total_days + 1
        self.season_gains.append([range(start, end, 1), self.gains[start:end], self.season.name, self.pallette[self.color]])
        self.color += 1
        self.season = season

        # TODO: keep cross seasonal crops
        # keep = []
        # for crop in self.field:
        #     if crop in season.crops:
        #         keep.append(crop)
        
        self.field = []


    def get_valid_crops(self): 
        crops = self.season.get_crops()
        days = self.season.days - self.season.current_day

        valid_crops = []
        for crop in crops:
            if crop.buy_price <= self.money and crop.days_to_grow <= days:
                # new_plant = Crop(crop.name, crop.intro_day, crop.harvest_rate, crop.days_to_grow, crop.regrow_days, crop.buy_price, crop.sell_price)
                new_plant = crop.duplicate()
                valid_crops.append(new_plant)
        
        return valid_crops



# different ways to choose crops to plant
# utilized in plant() method
def get_most_profitable(crops):
    crops.sort(key=lambda x: x.initial_profit, reverse=True)
    return crops[0]

def get_smallest_grow_time(crops):
    crops.sort(key=lambda x: x.days_to_grow)
    return crops[0]

def get_longest_grow_time(crops):
    crops.sort(key=lambda x: x.days_to_grow, reverse=True)
    return crops[0]

def get_cheapest(crops):
    crops.sort(key=lambda x: x.buy_price)
    return crops[0]

def get_expensive(crops):
    crops.sort(key=lambda x: x.buy_price, reverse=True)
    return crops[0]

def get_highest_seasonal_profit(crops, days_left):
    crops.sort(key=lambda x: x.calculate_current_season_profit(days_left), reverse=True)
    return crops[0]
