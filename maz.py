#make a 2D list for board 
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
    def __init__(self,parent = None, position = None):
        self.par = parent 
        self.pos = position       #cell :(x,y)
        self.g=0
        self.h=0
        self.f=0
    # equalation operator 
    def __eq__(self, operand):
        return self.pos == operand.pos

    def __ne__(self, operand):
        return self.pos != operand.pos    
#make dictionery for each value on the board with N S E W value
#def initMAp():
#    board_map = {
#        (0,0) : {'N' : 0 ,'S' : 0 ,'E' : 0 ,'W' : 0  },
#    }

#heurestic -> manhatan distance:
def he(posOne,posTwo):
    x1,y1=posOne
    x2,y2=posTwo
    return abs(x1-x2)+abs(y1-y2)

#A* algorithm:    
def astar (board,start,end):
    st = node(None,start) #init start node
    st.g=0
    ed = node (None,end) #init dist node
    ed.g=ed.h=ed.f=0

    openls = [st]
    closels = []

    while len(openls) > 0:
        ################find a node:
        #init:
        cur = openls[0]
        cur_index = 0
        #find min:
        i=0
        for nd in openls:
            if nd.f<cur.f:
                cur = nd
                cur_index = i
            i =+ 1    
        #cur node is min    
        openls.pop(cur)
        closels.append(cur)
        #goal test:
        if cur == end :
            Rpath_arr = []
            temp_node = cur
            while temp_node.par != None :
                Rpath_arr.append(temp_node.pos)
                temp_node=temp_node.par
            path_arr = Rpath_arr[: : -1]
            return path_arr #goal achived
        
        #children:
        children_of_cur = []
        for add_node in [(1,0),(0,1),(-1,0),(0,-1)]:
            new_pos = (cur.pos(0)+add_node(0),cur.pos(1)+add_node(1))
            #validation of new pos:
            if new_pos[0] > 24 | new_pos[0] < 0 | new_pos[1] > 24 | new_pos[1] < 0 :
                continue
            if board(new_pos[0],new_pos[1]) == 0:
                continue
            #if valid:
            new_node = node(cur,new_pos)
            children_of_cur.append(new_node)

        for child_of_cur in children_of_cur:

            child_of_cur.h=he(child_of_cur.pos[0],child_of_cur.pos[1])
            child_of_cur.g=cur.g+1
            f=child_of_cur.g+child_of_cur.h

            flag_for_AddToOpn1 = False
            flag_for_AddToOpn2 = False

            child_existO = node
            child_existC = node
            for o in openls:
                if child_of_cur != o:
                    flag_for_AddToOpn1 = True
                    child_existO = child_of_cur
            for c in closels:
                if child_of_cur != c:
                    flag_for_AddToOpn2 = True
                    child_existC = child_of_cur

            if flag_for_AddToOpn2 and flag_for_AddToOpn1 :
                openls.append(child_of_cur) 
                child_of_cur.f = f
            else:    
              if flag_for_AddToOpn1 : #child exit on the open list
                if child_of_cur.f > child_existO.f:
                    child_of_cur.f=child_existO.f

              if flag_for_AddToOpn2:  #child exit on the close list          
                if child_of_cur.f > child_existC.f:
                    child_of_cur.f=child_existC.f
                    openls.append(child_of_cur)
                    closels.pop(child_of_cur)
            openls.append(child_of_cur)

def main():
    brd = initBoard 
    print(brd)
    sart_node=(2,13)
    goal_node=(2,3)
    #path = astar(brd,sart_node,goal_node)
    #a shape with 0 1 s(start) e1(goal1) e2(goal2) and *(path)


if __name__ == "__main__":
    main()