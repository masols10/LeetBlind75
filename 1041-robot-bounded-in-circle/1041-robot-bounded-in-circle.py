class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''curr_dir = 'N'
        curr_pos = [0,0]
        directions = {'N':[0,1], 'E':[1,0], 'W':[-1,0], 'S':[0,-1]}
        change_dir = {
            'N':{'L':'W', 'R':'E'},
            'E':{'L':'N', 'R':'S'},
            'W':{'L':'S', 'R':'N'},
            'S':{'L':'E', 'R':'W'}
        }
        for instruction in instructions:
            if instruction == 'G':
                curr_pos[1] += directions[curr_dir][1]
                curr_pos[0] += directions[curr_dir][0]
            else:
                curr_dir=change_dir[curr_dir][instruction]
        if curr_dir != 'N' or curr_pos == [0,0]:
            return True
        else:
            return False
        '''
        #north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0
        
        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0
    
        '''
        We use simulation to simulate the path the robot goes in. We know if the robot will end up in a circle if it ends back where it is (x and y both are 0) or the robot isn't still facing the same direction (direction change is sitll 0, 1)

So, in the end we only need to check if x and y are the same or if di is still (0, 1) north.

We also don't need to store a whole array of directions: to swap the following directions:
left - set dx the opposite of dy and dy as dx.
right - set dy to the opposite of dx and dx as dy.
This is a bit tricky, but once you expand it you'll get it.

In-Depth Code Explanation
Define di as a tuple where di[0] is the change of x and di[1] is the change of y
Define x and y coordinates
Iterate through the list of instructions:
If the instruction is 'G': add di to x and y (make them move forward in same direction)
If the instruction is 'L': turn robot left (see above for detailed explanation for how)
If the instruction is 'R': turn robot right (see above for detailed explanation for how)
Check if x and y are still 0 or if di is not still (0, 1)
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        di = (0,1)
        x, y = 0, 0
        for instruction in instructions:
            if instruction == 'G':
                x, y = x + di[0], y + di[1]
            elif instruction == 'L':
                di = (-di[1], di[0])
            elif instruction == 'R':
                di = (di[1], -di[0])
            
        return (x == 0 and y == 0) or di != (0, 1)
        '''