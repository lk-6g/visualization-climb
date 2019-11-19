from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []
for roll_number in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
frequencies = []
max_result = die_1.number_sides + die_2.number_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
hist = pygal.Bar()

hist.title = "Result of rolling two D6 dice 1000 times"
hist.x_labels = []
for x_label in range(1, 13):
    hist.x_labels.append(x_label)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('Two D6', frequencies)
hist.render_to_file('dice_visual.svg')