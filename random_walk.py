from random import choice

class RandomWalk:
    def __init__(self, num_points = 5000): #initialize attribute of walks
        self.num_points = num_points

        #all walks start at (0,0)
        self.x_value =[0]
        self.y_value =[0]

    def fill_walk(self): #calculates all points in the walk
        while len(self.x_value) < self.num_points: #loop runs until walk is filled with correct number of points


            x_direction = choice([1,-1]) #1 for right, -1 for left direction
            x_distance = choice([0,1,3,4]) #how far to move in that direction by randomly selecting integer between 0 and 4
            x_step = x_direction * x_distance #determine length of each step

            y_direction = choice([1,-1])
            y_distance = choice([0,1,3,4])
            y_step = y_direction * y_distance

            #reject moves that go nowhere
            if x_step == 0 and y_step == 0: #if both x_step and y_step are 0, the walk doesn't go anywhere so we continue the loop to ignore this move
                continue
     
            #calculate new position
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)
