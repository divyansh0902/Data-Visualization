#rolling 1 die
'''from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()  # create instance of die with default 6 sides

results = []
# we roll die 100 times and store results of each rool in list results
for roll_number in range(1000):
    result = die.roll()
    results.append(result)

    frequencies = []  # create empty list to store numberof times each value is rolled
    for value in range(1, die.num_sides+1):  # loop through possible values
        # count how many times each number appears in results
        frequency = results.count(value)
        frequencies.append(frequency)  # then append this value tp list

# print(frequencies)
# print(results)

# visualize the results

# plotly doesn't accept results of range() func directly, so need to convert range to a list explicitly using list()func
x_values = list(range(1, die.num_sides+1))

# plotly class Bar() represent a data set that will be formatted as a bar chart
data = [Bar(x=x_values, y=frequencies)]

# giving title to each axis
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Freuency of Result'}

# layout class returns an object that specifies layout and configuration of graph as a whole
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

#to generate plot, we call offline.plot()func. This func need a directory containing data and layout objects and also accepts name of file where graph will be saved
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')'''




#rolling 2 dice
'''from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create 2 D6 dice
die_1 = Die()  
die_2 = Die()


results = []
for roll_number in range(1000):
    result = die_1.roll() + die_2.roll() #sum of 2 dice for each roll
    results.append(result)

    frequencies = [] 
    max_result = die_1.num_sides + die_2.num_sides #analyze result. 
    for value in range(2, max_result+1): #count number of results for each value between 2 and max_result 
       
        frequency = results.count(value)
        frequencies.append(frequency)  



x_values = list(range(2, max_result+1))

data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick' : 1} #when creating charts,we include dtick key. this setting controls spacing between tick marks on x axis
y_axis_config = {'title': 'Freuency of Result'}

my_layout = Layout(title='Results of rolling two D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')'''




#rolling dice of different sizes
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create D6 and D10 dice
die_1 = Die()  
die_2 = Die(10)


results = []
for roll_number in range(5000):
    result = die_1.roll() + die_2.roll() #sum of 2 dice for each roll
    results.append(result)

    frequencies = [] 
    max_result = die_1.num_sides + die_2.num_sides #analyze result. 
    for value in range(2, max_result+1): #count number of results for each value between 2 and max_result 
       
        frequency = results.count(value)
        frequencies.append(frequency)  


x_values = list(range(2, max_result+1))

data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick' : 1} #when creating charts,we include dtick key. this setting controls spacing between tick marks on x axis
y_axis_config = {'title': 'Freuency of Result'}

my_layout = Layout(title='Results of rolling D6 and D10 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')