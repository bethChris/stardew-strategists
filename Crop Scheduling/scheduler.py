from crop import Crop
from season import Season
from farm import Farm


# meta data for crops per season
spring_crops = {
    "blue jazz": {"buy_price": 30, "intro_day": 0, "sell_price": 50, "harvest_rate": 1, "days_to_grow": 7, "regrow_days": 0},
    "cauliflower": {"buy_price": 80, "intro_day": 0, "sell_price": 175, "harvest_rate": 1, "days_to_grow": 12, "regrow_days": 0},
    "green bean": {"buy_price": 60, "intro_day": 0, "sell_price": 40, "harvest_rate": 1, "days_to_grow": 10, "regrow_days": 3},
    "kale": {"buy_price": 70, "intro_day": 0, "sell_price": 110, "harvest_rate": 1, "days_to_grow": 6, "regrow_days": 0},
    "parsnip": {"buy_price": 20, "intro_day": 0, "sell_price": 35, "harvest_rate": 1, "days_to_grow": 4, "regrow_days": 0},
    "potato": {"buy_price": 50, "intro_day": 0, "sell_price": 80, "harvest_rate": 1.25, "days_to_grow": 6, "regrow_days": 0},
    "tulip": {"buy_price": 20, "intro_day": 0, "sell_price": 30, "harvest_rate": 1, "days_to_grow": 6, "regrow_days": 0},
    "unmilled rice": {"buy_price": 20, "intro_day": 0, "sell_price": 30, "harvest_rate": 1.11, "days_to_grow": 8, "regrow_days": 0},
}

summer_crops = {
    "blueberry": {"buy_price": 80, "intro_day": 0, "sell_price": 50, "harvest_rate": 3.02, "days_to_grow": 13, "regrow_days": 4},
    "corn": {"buy_price": 150, "intro_day": 0, "sell_price": 50, "harvest_rate": 1, "days_to_grow": 14, "regrow_days": 4},
    "hops": {"buy_price": 60, "intro_day": 0, "sell_price": 25, "harvest_rate": 1.03, "days_to_grow": 11, "regrow_days": 1},
    "hot pepper": {"buy_price": 40, "intro_day": 0, "sell_price": 40, "harvest_rate": 1, "days_to_grow": 5, "regrow_days": 3},
    "melon": {"buy_price": 80, "intro_day": 0, "sell_price": 250, "harvest_rate": 1, "days_to_grow": 12, "regrow_days": 0},
    "poppy": {"buy_price": 100, "intro_day": 0, "sell_price": 140, "harvest_rate": 1, "days_to_grow": 7, "regrow_days": 0},
    "radish": {"buy_price": 40, "intro_day": 0, "sell_price": 90, "harvest_rate": 1, "days_to_grow": 6, "regrow_days": 0},
    "summer spangle": {"buy_price": 50, "intro_day": 0, "sell_price": 90, "harvest_rate": 1, "days_to_grow": 8, "regrow_days": 0},
    "sunflower": {"buy_price": 200, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 8, "regrow_days": 0},
    "tomato": {"buy_price": 50, "intro_day": 0, "sell_price": 60, "harvest_rate": 1.05, "days_to_grow": 11, "regrow_days": 4},
    "wheat": {"buy_price": 10, "intro_day": 0, "sell_price": 25, "harvest_rate": 1, "days_to_grow": 4, "regrow_days": 0},
}

fall_crops = {
    "amaranth": {"buy_price": 70, "intro_day": 0, "sell_price": 150, "harvest_rate": 1, "days_to_grow": 7, "regrow_days": 0},
    "bok choy": {"buy_price": 50, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 4, "regrow_days": 0},
    "corn": {"buy_price": 150, "intro_day": 0, "sell_price": 50, "harvest_rate": 1, "days_to_grow": 14, "regrow_days": 4},
    "cranberries": {"buy_price": 240, "intro_day": 0, "sell_price": 75, "harvest_rate": 2.11, "days_to_grow": 7, "regrow_days": 5},
    "eggplant": {"buy_price": 20, "intro_day": 0, "sell_price": 60, "harvest_rate": 1.002, "days_to_grow": 5, "regrow_days": 5},
    "fairy rose": {"buy_price": 200, "intro_day": 0, "sell_price": 290, "harvest_rate": 1, "days_to_grow": 12, "regrow_days": 0},
    "grape": {"buy_price": 60, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 10, "regrow_days": 3},
    "pumpkin": {"buy_price": 100, "intro_day": 0, "sell_price": 320, "harvest_rate": 1, "days_to_grow": 13, "regrow_days": 0},
    "sunflower": {"buy_price": 200, "intro_day": 0, "sell_price": 80, "harvest_rate": 1, "days_to_grow": 8, "regrow_days": 0},
    "yam": {"buy_price": 60, "intro_day": 0, "sell_price": 160, "harvest_rate": 1, "days_to_grow": 10, "regrow_days": 0},
    "wheat": {"buy_price": 10, "intro_day": 0, "sell_price": 25, "harvest_rate": 1, "days_to_grow": 4, "regrow_days": 0},
}

# NOTES
# assumed available energy increases 6 per day translating to an additional 3 field slots per day. Starting at 135 
# max crops watered with basic level energy and watering can = 135 (270 max energy, 2 energy per water)
# all sell prices are for 1 crop and is assumed to be the base sell price (anything more is a plus)
# harvest rates are base rates with average of chance of getting more than 1 crop added
# starter seeds is 15 parsnips (sell those and gain gold, then make decision) + 150 g
# we only consider plants that can be be purchased and that are obtainable year 1
# all prices based on pierre's shop as we support small businesses round here
# giant crops are assumed to not be possible for simplicity
# starter gold is 500 + 150 g from selling parsnips
# all prices are for 1 seed
# all seasons have 28 Days
# assumed no speed grow
# assumed no fertilizer
# closed on wednesdays
# assumed no crows


# initial set up of seasons
s_crops = []
for crop in spring_crops:
    s_crops.append(Crop(crop, **spring_crops[crop]))

spring = Season("spring", s_crops, 100, [4,11,13,18,24,25])

sum_crops = []
for crop in summer_crops:
    sum_crops.append(Crop(crop, **summer_crops[crop]))

summer = Season("summer", sum_crops, 100, [4,11,18,25,28])

f_crops = []
for crop in fall_crops:
    f_crops.append(Crop(crop, **fall_crops[crop]))

fall = Season("fall", f_crops, 100, [4,11,16,18,25,27])

seasons = [spring, summer, fall]


# run simulation    
farm = Farm(spring)
farm.run_simulation()

farm.change_seasons(summer)
farm.run_simulation()

farm.change_seasons(fall)
farm.run_simulation()

farm.plot_money(update=False)
