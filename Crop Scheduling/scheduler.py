import math
import matplotlib.pyplot as plt
import seaborn as sns

spring_crops = {
    "blue jazz": {"buy_price": 30, "intro_day": 0, "sell_price": 50, "harvest_rate": 1, "days_to_grow": 7, "regrow_days": 0},
    "cauliflower": {"buy_price": 80, "intro_day": 0, "sell_price": 175, "harvest_rate": 1, "days_to_grow": 12, "regrow_days": 0},
    "garlic": {"buy_price": 40, "intro_day": 0, "sell_price": 60, "harvest_rate": 1, "days_to_grow": 4, "regrow_days": 0},
    "green bean": {"buy_price": 60, "intro_day": 0, "sell_price": 40, "harvest_rate": 1, "days_to_grow": 10, "regrow_days": 3},
    "kale": {"buy_price": 70, "intro_day": 0, "sell_price": 110, "harvest_rate": 1, "days_to_grow": 6, "regrow_days": 0},
    "parsnip": {"buy_price": 20, "intro_day": 0, "sell_price": 35, "harvest_rate": 1, "days_to_grow": 4, "regrow_days": 0},
    "potato": {"buy_price": 50, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 6, "regrow_days": 0},
    "tulip": {"buy_price": 20, "intro_day": 0, "sell_price": 30, "harvest_rate": 1, "days_to_grow": 6, "regrow_days": 0},
    "unmilled rice": {"buy_price": 20, "intro_day": 0, "sell_price": 30, "harvest_rate": 1, "days_to_grow": 8, "regrow_days": 0},
}

summer_crops = {
    "blueberry": {"buy_price": 80, "intro_day": 0, "sell_price": 50, "harvest_rate": 3, "days_to_grow": 13, "regrow_days": 4},
    "corn": {"buy_price": 150, "intro_day": 0, "sell_price": 50, "harvest_rate": 1, "days_to_grow": 14, "regrow_days": 4},
    "hops": {"buy_price": 60, "intro_day": 0, "sell_price": 25, "harvest_rate": 1, "days_to_grow": 11, "regrow_days": 1},
    "hot pepper": {"buy_price": 40, "intro_day": 0, "sell_price": 40, "harvest_rate": 1, "days_to_grow": 5, "regrow_days": 3},
    "melon": {"buy_price": 80, "intro_day": 0, "sell_price": 250, "harvest_rate": 1, "days_to_grow": 12, "regrow_days": 0},
    "poppy": {"buy_price": 100, "intro_day": 0, "sell_price": 140, "harvest_rate": 1, "days_to_grow": 7, "regrow_days": 0},
    "radish": {"buy_price": 40, "intro_day": 0, "sell_price": 90, "harvest_rate": 1, "days_to_grow": 6, "regrow_days": 0},
    "summer spangle": {"buy_price": 50, "intro_day": 0, "sell_price": 90, "harvest_rate": 1, "days_to_grow": 8, "regrow_days": 0},
    "sunflower": {"buy_price": 200, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 8, "regrow_days": 0},
    "tomato": {"buy_price": 50, "intro_day": 0, "sell_price": 60, "harvest_rate": 1, "days_to_grow": 11, "regrow_days": 4},
    "wheat": {"buy_price": 10, "intro_day": 0, "sell_price": 25, "harvest_rate": 1, "days_to_grow": 4, "regrow_days": 0},
}

fall_crops = {
    "amaranth": {"buy_price": 70, "intro_day": 0, "sell_price": 150, "harvest_rate": 1, "days_to_grow": 7, "regrow_days": 0},
    "bok choy": {"buy_price": 50, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 4, "regrow_days": 0},
    "corn": {"buy_price": 150, "intro_day": 0, "sell_price": 50, "harvest_rate": 1, "days_to_grow": 14, "regrow_days": 4},
    "cranberries": {"buy_price": 240, "intro_day": 0, "sell_price": 75, "harvest_rate": 2, "days_to_grow": 7, "regrow_days": 5},
    "eggplant": {"buy_price": 20, "intro_day": 0, "sell_price": 60, "harvest_rate": 1, "days_to_grow": 5, "regrow_days": 5},
    "fairy rose": {"buy_price": 200, "intro_day": 0, "sell_price": 290, "harvest_rate": 1, "days_to_grow": 12, "regrow_days": 0},
    "grape": {"buy_price": 60, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 10, "regrow_days": 3},
    "pumpkin": {"buy_price": 100, "intro_day": 0, "sell_price": 320, "harvest_rate": 1, "days_to_grow": 13, "regrow_days": 0},
    "sunflower": {"buy_price": 200, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 8, "regrow_days": 0},
    "yam": {"buy_price": 60, "intro_day": 0, "sell_price": 160, "harvest_rate": 1, "days_to_grow": 10, "regrow_days": 0},
}


# Season contains
# - crops
# - days
# - sell days

# Crop contains
# - name
# - pricing info
# - tending methods
#   - water
#   - harvest


# Farm contains
# - crops planted
# - season info
# - money
# - field size 
# - tending methods
# - transfer seasons


# max crops watered with basic level energy and watering can = 135 (270 max energy, 2 energy per water)
# starter gold is 500
# starter seeds is 15 parsnips (sell those and gain gold, then make decision) + 150 g
# closed on wednesdays
# all prices based on pierre's shop as we support small businesses round here
# all prices are for 1 seed
# all sell prices are for 1 crop and is assumed to be the base sell price (anything more is a plus)
# harvest rates are the base rate, no simulating chance of more for simplicity
# we only consider plants that can be be purchased and that are obtainable year 1
# giant crops are assumed to not be possible for simplicity
# assumed no fertilizer
# assumed no speed grow
# assumed no crows
# all seasons have 28 days

class Crop:
    def __init__(self, name, intro_day, harvest_rate, days_to_grow, regrow_days, buy_price, sell_price):
        self.name = name
        self.intro_day = intro_day
        self.harvest_rate = harvest_rate
        self.days_to_grow = days_to_grow
        self.regrow_days = regrow_days
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.days_grown = 0

        self.total_sold_for = (harvest_rate * sell_price)
        self.initial_profit = self.total_sold_for - buy_price
        
        self.profit_per_grow_day = (self.initial_profit) / days_to_grow  
        self.profit_per_regrow_day = ((self.total_sold_for) / regrow_days) if regrow_days else 0

        self.regrow_periods_to_break_even = max(math.ceil((buy_price - (harvest_rate * sell_price))  / (harvest_rate * sell_price)), 0)
        self.total_regrow_days_to_break_even = self.regrow_days * self.regrow_periods_to_break_even

        self.seasonal_profit = self.calculate_season_profit()


    def calculate_season_profit(self, days=28):
        if self.regrow_days:
            period = days - self.days_to_grow
            regrow_profit = (((period // self.regrow_days) * self.harvest_rate) * self.sell_price)
            return (regrow_profit + self.total_sold_for) - self.buy_price
        else:
            # calculate how many grow times we can have.abs
            times_grown = days // self.days_to_grow
            return self.initial_profit * times_grown
    
    def water(self):
        self.days_grown += 1
        

    def harvest(self):
        if self.days_grown >= self.days_to_grow:
            if self.regrow_days:
                if (self.days_grown - self.days_to_grow) % self.regrow_days == 0:
                    return self.total_sold_for
            else:
                self.days_grown = 0
                return self.total_sold_for
        return 0
        

    def __str__(self):
        if self.regrow_days:
            regrown_days = (self.days_grown) % self.days_to_grow if self.days_grown > self.days_to_grow else 0
            return f"{self.name}({self.days_grown}/{self.days_to_grow}) regrow: ({regrown_days}/{self.regrow_days})"
        return f"{self.name}({self.days_grown}/{self.days_to_grow})"


class Season:
    def __init__(self, name, crops, field_size, no_sell_days=[4,11,18,25]):
        self.name = name
        self.crops = crops
        self.days = 28
        self.sell_days = [True for _ in range(28)]
        self.field_size = field_size
        self.field = []
        for day in no_sell_days:
            self.sell_days[day-1] = False
        
        self.current_day = 1

    def get_crops(self):
        return self.crops

    def sell_day(self):
        return self.sell_days[self.current_day-1]
    
    def next_day(self):
        self.current_day += 1


class Farm:
    def __init__(self, season):
        self.season = season
        self.money = 650
        self.field = []
        self.field_size = 100
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

        self.season.next_day()

    def plant(self):
        crops = self.season.get_crops()
        
        valid_crops = get_valid_crops(crops, self.season.days - self.season.current_day, self.money)
        while (self.money > 0 and len(valid_crops) > 0 and len(self.field) < self.field_size):
            valid_crops = get_valid_crops(crops, self.season.days - self.season.current_day, self.money)
            if len(valid_crops) > 0:
                # define here what selection process to use
                # choice = get_most_profitable(valid_crops)
                choice = get_cheapest(valid_crops)
                # choice = get_most_profitable_per_day(valid_crops)
                # choice = get_smallest_grow_time(valid_crops) 
                # choice = get_expensive(valid_crops)
                # choice = get_highest_seasonal_profit(valid_crops)
                # choice = get_longest_grow_time(valid_crops)

                # buy seed and plant in field
                self.money -= choice.buy_price
                self.field.append(choice)

    def run_step(self):
        print()
        print("DAY", self.season.current_day, "| MONEY: $", self.money)
        print("# of CROPS: ", len(self.field))
        self.tend()
        
        # self.plot_money()
        self.plot_crops()
        self.total_days += 1
        self.gains.append(self.money)
        
        # for crop in self.field:
        #     print(crop)


    def run_simulation(self):
        while self.season.current_day <= self.season.days:
            self.run_step()

        print()
        print("FINAL MONEY: $", self.money)  


    def plot_crops(self):
        crop_names = [crop.name for crop in self.season.crops]
        field_crops = [crop.name for crop in self.field]
        crop_totals = [field_crops.count(crop) for crop in crop_names]
      
        sns.barplot(y=crop_names, x=crop_totals)
        plt.yticks(rotation=30, ha='right', fontsize=8)
        plt.xlabel('Total')
        plt.ylabel('Crop')
        plt.title(f'Total of Each Plant {self.season.name} Day {self.season.current_day}')
        plt.pause(0.08)
        plt.clf()
    

    def plot_money(self, update=True):
        sns.lineplot(x=range(self.total_days + 1), y=self.gains, label=self.season.name, color=self.pallette[self.color])
        for gains in self.season_gains:
            sns.lineplot(x=gains[0], y=gains[1], label=gains[2], color=gains[3])

        plt.xlabel('Days')
        plt.ylabel('Money')
        plt.title(f'Money Over Time')
        if update:
            plt.pause(0.08)
            plt.clf()
        else:
            plt.show()

    def change_seasons(self, season):
        print("SEASON CHANGE: ", season.name)
        start = self.total_days - self.season.days
        end = self.total_days + 1
        self.season_gains.append([range(start, end, 1), self.gains[start:end], self.season.name, self.pallette[self.color]])
        print(range(start, end, 1))
        self.color += 1
        self.season = season
        keep = []
        for crop in self.field:
            if crop in season.crops:
                keep.append(crop)
        
        self.field = keep


def get_valid_crops(crops, days, money): 
    valid_crops = []
    for crop in crops:
        if crop.buy_price <= money and crop.days_to_grow <= days:
            new_plant = Crop(crop.name, crop.intro_day, crop.harvest_rate, crop.days_to_grow, crop.regrow_days, crop.buy_price, crop.sell_price)
            valid_crops.append(new_plant)
    
    return valid_crops


def get_most_profitable(crops):
    crops.sort(key=lambda x: x.initial_profit, reverse=True)
    return crops[0]

def get_smallest_grow_time(crops):
    crops.sort(key=lambda x: x.days_to_grow)
    return crops[0]

def get_longest_grow_time(crops):
    crops.sort(key=lambda x: x.days_to_grow, reverse=True)
    return crops[0]

def get_most_profitable_per_day(crops):
    crops.sort(key=lambda x: x.profit_per_grow_day, reverse=True)
    return crops[0]

def get_cheapest(crops):
    crops.sort(key=lambda x: x.buy_price)
    return crops[0]

def get_expensive(crops):
    crops.sort(key=lambda x: x.buy_price, reverse=True)
    return crops[0]

def get_highest_seasonal_profit(crops):
    crops.sort(key=lambda x: x.seasonal_profit, reverse=True)
    return crops[0]

    

f_crops = []
for crop in fall_crops:
    f_crops.append(Crop(crop, **fall_crops[crop]))

fall = Season("fall", f_crops, 100, [4,11,16,18,25,27])

s_crops = []
for crop in spring_crops:
    s_crops.append(Crop(crop, **spring_crops[crop]))

spring = Season("spring", s_crops, 100, [4,11,13,18,24,25])

sum_crops = []
for crop in summer_crops:
    sum_crops.append(Crop(crop, **summer_crops[crop]))

summer = Season("summer", sum_crops, 100, [4,11,18,25,28])

farm = Farm(spring)
farm.run_simulation()

farm.change_seasons(summer)
farm.run_simulation()

farm.change_seasons(fall)
farm.run_simulation()

farm.plot_money(update=False)
