#make a structure for each node:
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position #(x,y)
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other

#heurestic -> manhatan distance:
def he(posOne,posTwo):
    x1,y1=posOne
    x2,y2=posTwo
    return abs(x1-x2)+abs(y1-y2)

#A* algorithm:    
def astar (board,start,end):
    nodes =1 #number of expanded nodes
    
    st = Node(None,start) #init start node
    st.g=0
    st.h=he(start,end)
    st.f=st.g+st.h
    
    openls = [st]  #list of unexpanded nodes
    closels = []   #list of explored nodes

    while len(openls) > 0:
        #find next node:
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
        openls.pop(cur_index) #remove cur from openls at which f is minimum
        closels.append(cur)   #place cur on closels at which f is minimum
        #goal test:
        if cur.position == end :  #if node is goal node
            Rpath_arr = []
            temp_node = cur
            while temp_node.parent != None :
                Rpath_arr.append(temp_node.position)
                temp_node=temp_node.parent
            Rpath_arr.append(temp_node.position)
            path_arr = Rpath_arr[: : -1]      #solution
            print ('expanded nodes = '+ str(nodes))  
            return path_arr #goal achived
        
        #children_expand node cur,generating all its successors with pointers back to cur_:
        children_of_cur = []
        for child_node in [(1,0),(0,1),(-1,0),(0,-1)]:
            child_pos = (cur.position[0]+child_node[0],cur.position[1]+child_node[1])
            #validation of new pos:
            if child_pos[0] > 24 or child_pos[0] < 0 or child_pos[1] > 24 or child_pos[1] < 0 :
                continue
            if board[child_pos[0]][child_pos[1]] != 1:
                continue
            #if valid:
            new_node = Node(cur,child_pos)
            children_of_cur.append(new_node)
       
        for child_of_cur in children_of_cur:    #for all child_of_cur of cur do...

            child_of_cur.h=he(child_of_cur.position,end)  #calculate f_child_of_cur
            child_of_cur.g=cur.g+1
            f_child_of_cur=child_of_cur.g+child_of_cur.h

            flag_notexist_childO = True  #missing child in openls
            flag_notexist_childC = True  #missing child in closels

            child_existO_f = Node()
            child_existC_f = Node()

            for o in openls:
                if child_of_cur == o:
                    flag_notexist_childO = False
                    child_existO_f.f = child_of_cur.f #make a copy from f of child_of_cur 

            counter = 0 
            index_child_of_cur = 0   #becuse we should pop from closls
            for c in closels:
                if child_of_cur == c:
                    flag_notexist_childC = False
                    child_existC_f.f = child_of_cur.f
                    index_child_of_cur = counter
                counter += 1


            if flag_notexist_childO and flag_notexist_childC :  #if child_of_cur dosnt exist in openls and closels
                openls.append(child_of_cur)      #add child_of_cur to openls
                child_of_cur.f = f_child_of_cur  #assign the newly computed f to child_of_cur
                nodes += 1                       #each assign for node.f means : a node expanded


            else:    
              if flag_notexist_childO :                #child exit on the open list
                if child_of_cur.f > child_existO_f.f:  #if f value is smaller than the previous value
                    child_of_cur.f=child_existO_f.f    #update f with new value
                    nodes += 1

              if flag_notexist_childC:                 #child exit on the close list          
                if child_of_cur.f > child_existC_f.f:  #if f value is smaller than the previous value
                    child_of_cur.f=child_existC_f.f    #update f with new value
                    nodes += 1    
                    openls.append(child_of_cur)         #move child_of_cur back to openls
                    closels.pop(index_child_of_cur)

            #openls.append(child_of_cur)
    return None

def show(maze,start,end,path):
    for i in range (25):
        temp = ''
        for j in range (25):
            if (maze[i][j] == 1):
                if ((i,j) == start):
                    temp += 'S  '
                elif ((i,j) == end):
                    temp += 'E  '
                elif ((i,j) in path):
                    temp += '*  '
                else:
                    temp += '1  '
            elif (maze[i][j] == 0):
                temp += '0  '
        print (temp)

def main():
    maze = [
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


    print('A:')  #outputcalculate the output of part A question 4
    start = (13, 2)
    goal  = (5, 23)
    path = astar(maze, start, goal)
    print(path)
    show(maze,start,goal,path)
    print('path cost: ' + str(len(path)-1))
    
    print('B:')  #outputcalculate the output of part B question 4
    start = (13, 2)
    goal  = (3,  2)
    path = astar(maze, start, goal)
    print(path)
    show(maze,start,goal,path)
    print('path cost: ' + str(len(path)-1))

    print('C:')  #outputcalculate the output of part C question 4
    start = (0 , 0)
    goal  = (24,24)
    path = astar(maze, start, goal)
    try:  #error management
        print(path)
        show(maze,start,goal,path)
        print('path cost: ' + str(len(path)-1))
    except:
        print('no solution')

if __name__ == '__main__':
    main()