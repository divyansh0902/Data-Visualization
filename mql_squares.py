# import pyplot module #pyplot contains a number of functions that generate charts and plots
'''import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]  # data that we will plot
fig, ax = plt.subplots()  # a common matplotlib convention by calling plt.subplots() #variable fig represents entire figure or collection of plots that are generated
ax.plot(squares, linewidth = 3) #controls thickness of line

ax.set_title("Square Numbers", fontsize = 24) #set titile of chart. contols fonts size of title
ax.set_xlabel("Value", fontsize = 14) #title for x axis
ax.set_ylabel("Squares of Value", fontsize = 14) #title for y axis

ax.tick_params(axis='both', labelsize = 14) #styles the tick marks. Affects both axis
ax.plot(squares)  # variable ax represents a single plot in figure #use plot() method which will try to plot data it's given in a meaningful way
plt.show()  # opens matplotlib's viewer'''





import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn') #uses build in styles 
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)
#ax.plot(squares, linewidth = 3) 

ax.set_title("Square Numbers", fontsize = 24) #set titile of chart. contols fonts size of title
ax.set_xlabel("Value", fontsize = 14) #title for x axis
ax.set_ylabel("Squares of Value", fontsize = 14) #title for y axis

ax.tick_params(axis='both', labelsize = 14) 
#ax.plot(squares)  
plt.show()


























