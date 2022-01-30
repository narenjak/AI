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
        openls.pop(cur_index) 
        closels.append(cur)
        #goal test:
        if cur.position == end :
            Rpath_arr = []
            temp_node = cur
            while temp_node.parent != None :
                Rpath_arr.append(temp_node.position)
                temp_node=temp_node.parent
            Rpath_arr.append(temp_node.position)
            path_arr = Rpath_arr[: : -1]
            print ('expanded nodes = '+ str(nodes))
            return path_arr #goal achived
        
        #children:
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
        #for child_of_cur in children_of_cur:
        #    print (child_of_cur.position)     
        for child_of_cur in children_of_cur:

            child_of_cur.h=he(child_of_cur.position,end)
            child_of_cur.g=cur.g+1
            f_child_of_cur=child_of_cur.g+child_of_cur.h

            flag_notexist_childO = True
            flag_notexist_childC = True

            child_existO_f = Node()
            child_existC_f = Node()

            for o in openls:
                if child_of_cur == o:
                    flag_notexist_childO = False
                    child_existO_f.f = child_of_cur.f

            counter = 0
            index_child_of_cur = 0   
            for c in closels:
                if child_of_cur == c:
                    flag_notexist_childC = False
                    child_existC_f.f = child_of_cur.f
                    index_child_of_cur = counter


            if flag_notexist_childO and flag_notexist_childC :
                openls.append(child_of_cur) 
                nodes += 1
                child_of_cur.f = f_child_of_cur


            else:    
              if flag_notexist_childO : #child exit on the open list
                if child_of_cur.f > child_existO_f.f:
                    child_of_cur.f=child_existO_f.f

              if flag_notexist_childC:  #child exit on the close list          
                if child_of_cur.f > child_existC_f.f:
                    child_of_cur.f=child_existC_f.f
                    openls.append(child_of_cur)
                    nodes += 1
                    closels.pop(index_child_of_cur)

            #openls.append(child_of_cur)
    return None

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

    print('A:')
    start = (13, 2)
    goal  = (5, 23)
    path = astar(maze, start, goal)
    print(path)
    print('path cost: ' + str(len(path)-1))
    print('B:')
    start = (13, 2)
    goal  = (3,  2)
    path = astar(maze, start, goal)
    print(path)
    print('path cost: ' + str(len(path)-1))
    print('C:')
    start = (0 , 0)
    goal  = (24,24)
    path = astar(maze, start, goal)
    try:
        print(path)
        print('path cost: ' + str(len(path)-1))
    except:
        print('no solution')
        

if __name__ == '__main__':
    main()