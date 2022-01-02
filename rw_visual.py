import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True: #make multiple walks without having to run program
    rw = RandomWalk(50_000) #create a random walk and store it in rw
    rw.fill_walk() #we call fill_walk() func
    
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points) #renge () func to generate list of numbers equal to number of points in walk than store them in point_numbers
    ax.scatter(rw.x_value,rw.y_value, c= point_numbers, cmap=plt.cm.Blues, edgecolors='none',s = 1) #use edgecolors to get rid of black outline around dots

    #emphasize first and last points
    ax.scatter(0,0, c='green', edgecolors='none',s=100) #starting point
    ax.scatter(rw.x_value[-1],rw.y_value[-1],c= 'red', edgecolors='none',s=100) #last point


    #remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make anothet walk? (y/n): ")
    if keep_running == 'n':
        break