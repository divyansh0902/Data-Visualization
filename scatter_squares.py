# plotting and styling individual point with scatter
'''import matplotlib.pyplot as plt

plt.style.use('seaborn') #uses built in styles
fix, ax = plt.subplots()
ax.scatter(2,4, s = 100) #used to plot a single point or a series of points. Use s to set size of the dot

ax.set_title("Square Numbers", fontsize = 24) 
ax.set_xlabel("Value", fontsize = 14) 
ax.set_ylabel("Squares of Value", fontsize = 14)

ax.tick_params(axis='both', which ='major', labelsize = 14) 
plt.show()'''


# plotting a series of points with scatter()
'''import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.style.use('seaborn') #uses built in styles
fix, ax = plt.subplots()
ax.scatter(x_values,y_values, s = 100) #used to plot a single point or a series of points. Use s to set size of the dot

ax.set_title("Square Numbers", fontsize = 24) 
ax.set_xlabel("Value", fontsize = 14) 
ax.set_ylabel("Squares of Value", fontsize = 14)

ax.tick_params(axis='both', which ='major', labelsize = 14) 
plt.show()'''


# calculating data automatically
'''import matplotlib.pyplot as plt
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] #list comprehension generates y values
plt.style.use('seaborn')  # uses built in styles
fix, ax = plt.subplots()

#ax.scatter(x_values, y_values,c ='red', s=10)# used to plot a single point or a series of points. Use s to set size of the dot
ax.scatter(x_values, y_values,c =(0,0.8,0), s=10)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of Value", fontsize=14)

ax.axis([0, 1100, 0, 1100000])  # set range for each axis

ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()'''


#using colormap - is a series of color in a gradient that moves from a starting to an ending color
import matplotlib.pyplot as plt
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] 
plt.style.use('seaborn')  
fix, ax = plt.subplots()

ax.scatter(x_values, y_values,c = y_values, cmap=plt.cm.Greens, s=10) #we pass list of y_value to c, then tell pyplot which color to use using cmap argument
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of Value", fontsize=14)

ax.axis([0, 1100, 0, 1100000])  # set range for each axis

ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
#plt.savefig('square_plot.png', bbox_inches = 'tight') #saves the file. 1st argument is filename for plot image which will be saved in same directory.2nd argument trims extra spaces around plot




































