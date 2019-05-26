temperatures = [10, -20, 100]

def cel_to_far(celcius):
	fahrenheit = (celcius*9/5)+32
	return fahrenheit

for hasil in temperatures:
	print(cel_to_far(hasil))

