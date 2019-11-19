from die import Die

die = Die()

results = [die.roll() for roll_number in range(1000)]
    
frequencies = {}
for key in range(1, die.number_sides+1):
    frequency = results.count(key)
    frequencies[key] = frequency
    
print(frequencies)