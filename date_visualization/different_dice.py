from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = [die_1.roll() + die_2.roll() for roll_number in range(50000)]

max_result = die_1.number_sides + die_2.number_sides    
frequencies = [results.count(value) for value in range(1, max_result+1)]
    
hist = pygal.Bar()

hist.title = "Result of rolling a D6 and a D10 50000 times"
hist.x_labels = [x_label for x_label in range(1, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')