## Movement function
import copy
import sys 

def empty_tile(parent):
    for i in range(len(parent.puzzle)):
        for j in range(len(parent.puzzle[i])):
            if parent.puzzle[i][j]==0:
                return i,j
    return -1,-1

def generate_children(parent):
    l=[]
    i,j=empty_tile(parent)


    ## move up:
    if i>0:
        temp=copy.deepcopy(parent.puzzle)
        temp[i][j],temp[i-1][j]=temp[i-1][j],temp[i][j]
        l.append(temp)


    ## move down:
    if i<2:
        temp=copy.deepcopy(parent.puzzle)
        temp[i][j],temp[i+1][j]=temp[i+1][j],temp[i][j]
        l.append(temp)

    ## move left:
    if j>0:
        temp=copy.deepcopy(parent.puzzle)
        temp[i][j],temp[i][j-1]=temp[i][j-1],temp[i][j]
        l.append(temp)

    ## move up:
    if j<2:
        temp=copy.deepcopy(parent.puzzle)
        temp[i][j],temp[i][j+1]=temp[i][j+1],temp[i][j]
        l.append(temp)        
    
    
    return(l)


def sequencer(child,l):
    l.insert(0,child)

    if child.parent!=None:
        if child.cost-1!=child.parent.cost:
            print("cost verification failed")
            return
    
        else:
            print("cost verification successful")

        
    if child.parent==None:
        return
    else:
        sequencer(child.parent,l)


class state:
    def __init__(self,puzz, parent, cost):
        self.puzzle = puzz
        self.parent = parent
        self.cost = cost

    def data(self):
        print('object:\t ',)
        printarr(self.puzzle)
        print('Parent:\n\t',self.parent)
        print('cost=',self.cost)
        print()

def printarr(arr):
    for i in range(len(arr)):
        print('\t', end='')
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()

initial=[[1,2,3],
         [8,0,4],
         [7,6,5]]
# final=[[2,8,1],
#        [0,4,3],
#        [7,6,5]]
final=[[1,5,3],
       [7,4,6],
       [2,8,0]]

root=state(initial,None,0)
# root.data()
open=[]
open.append(root)
closed=[]
iter=0

while len(open)>0:

    iter=iter+1
    if iter%100==0:
        print('iter=',iter)
    parent=open.pop(0)
    
    # print('parent=')
    # printarr(parent.puzzle)
    # print()

    cost=parent.cost+1
    l=generate_children(parent)
    for i in range(len(l)):
        puzzle=l[i]
        # printarr(puzzle)
        if puzzle==final:
            last=state(puzzle, parent, cost)
            sequence=[]
            sequencer(last,sequence)
            print("end sequence=")
            for k in range(len(sequence)):
                printarr(sequence[k].puzzle)
                print()


            sys.exit()
            print("quit executed")

            

        if puzzle not in [j.puzzle for j in open] and puzzle not in [j.puzzle for j in closed]:
            open.append(state(puzzle,parent,cost))
            # print('unique puzzle=')    
            # print("open:")
            # for i in range(len(open)):
            #     printarr(open[i].puzzle)
            #     print()


        elif puzzle in [j.puzzle for j in open]:
            for j in open:
                if puzzle==j.puzzle:
                 index=open.index(j)

            index=open.index(j)
            if open[index].cost>cost:
                open.pop(index)
                open.append(state(puzzle,parent,cost))


        elif puzzle in [j.puzzle for j in closed]:
            for j in closed:
                if puzzle==j.puzzle:
                 index=closed.index(j)

            if closed[index].cost>cost:
                closed[index].cost=cost


        closed.append(parent)

