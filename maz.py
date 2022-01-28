#make a 2D list for board 
from importlib.resources import path


def initBoard():
    board = [
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1],
    [1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1],
    [0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1],
    [0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
    [1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    return board
#make a structure for each node:
class node():
    #Constructor
    def __init__(self,parent = None, pos = None):
        self.parent = parent #self is a cell :(x,y)
        self.pos = pos 
        self.g=0
        self.h=0
        self.f=0
    # equalation operator 
    def __eq__(self, operand):
        return self.pos == operand.pos
#make dictionery for each value on the board with N S E W value
#def initMAp():
#    board_map = {
#        (0,0) : {'N' : 0 ,'S' : 0 ,'E' : 0 ,'W' : 0  },
#    }

#heurestic -> manhatan distance:
def he(celOne,celTwo):
    x1,y1=celOne
    x2,y2=celTwo
    return abs(x1-x2)+abs(y1-y2)

#A* algorithm:    
def astar (board,start,end):
    st = node(None,start) #init start node
    st.g=0
    ed = node (None,end) #init dist node
    ed.g=ed.h=ed.f=0

    openls = [st]
    closels = []
    while len(openls) >0:
        ################find a node:
        #init:
        cur = openls[0]
        cur_index = 0
        #find min:
        ######################################enumerate?!

        openls.pop(cur)
        closels.append(cur)
        #goal test:

        #children:
        children_of_cur = []
        for add_node in [(1,0),(0,1),(-1,0),(0,-1)]:
            new_pos = (cur.pos(0)+add_node(0),cur.pos(1)+add_node(1))
            #validation of new pos:


            #if valid:
            new_node = node(cur,new_pos)
            children_of_cur.append(new_node)
        for child_of_cur in children_of_cur:

            child_of_cur.h=he(child_of_cur.pos[0],child_of_cur.pos[1])
            child_of_cur.g=cur.g+1
            child_of_cur.f=child_of_cur.g+child_of_cur.h

            openls.append(child_of_cur)


    #return path

        

        


def main():
    brd = initBoard 
    print(brd)
    sart_node=(2,13)
    goal_node=(2,3)
    #path = astar(brd,sart_node,goal_node)
    #a shape with 0 1 s(start) e1(goal1) e2(goal2) and *(path)


if __name__ == "__main__":
    main()