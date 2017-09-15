# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    print "let me settle it down!!!!!! \n\n DFS go!!!\n\n"
#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())
    nodeset=set()
    childcontainer = util.Stack()
    path=[]
   
    
    firstnode = problem.getStartState()

    childcontainer.push((firstnode,path))
#    numNodes = 1
    
    while not childcontainer.isEmpty():
        (curNode,path) = childcontainer.pop()
        if curNode in nodeset: 
            continue
        nodeset.add(curNode)
        if problem.isGoalState(curNode):
#            print path
#            print "number of nodes expanded",numNodes
            return path
            
        successors = problem.getSuccessors(curNode)
        
        for succ in successors:
#                numNodes += 1
            newPath = path + [succ[1]]
            childcontainer.push((succ[0],newPath))
    
    return none             
    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    nodeset=set()
    childcontainer = util.Queue()
    path=[]
    
    print "using bfs!!!!!\n\n\n"
    
    
    firstnode = problem.getStartState()

    childcontainer.push((firstnode,path))
#    numNodes = 1
    
    while not childcontainer.isEmpty():
        (curNode,path) = childcontainer.pop()
        if curNode in nodeset: 
            continue
        nodeset.add(curNode)
        if problem.isGoalState(curNode):
#            print path
#            print "number of nodes expanded",numNodes
            return path
            
        successors = problem.getSuccessors(curNode)
        
        for succ in successors:
#                numNodes += 1
            newPath = path + [succ[1]]
            childcontainer.push((succ[0],newPath))
    
    return none            

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    nodeset=set()
    childcontainer = util.PriorityQueue()
    path=[]
    
     
    firstnode = problem.getStartState()

     #watch out! the .pop() will not pop the cost!!!!
    childcontainer.push((firstnode,path,0) ,0) #(node,path[],cost),cost
    
#     numNodes = 1
    
    while not childcontainer.isEmpty():
        (curNode,path,cost) = childcontainer.pop()
        if curNode in nodeset: 
            continue
        nodeset.add(curNode)
        if problem.isGoalState(curNode):
#             print path
#             print "number of nodes expanded",numNodes
            return path       
        for succ in problem.getSuccessors(curNode):
#                 numNodes += 1
            newCost = cost+succ[2]               
            newPath = path + [succ[1]]
            childcontainer.push((succ[0],newPath,newCost),newCost)
    
    return none

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    nodeset=set()
    childcontainer = util.PriorityQueue()
    path=[]
    
     
    firstnode = problem.getStartState()

    #watch out! the .pop() will not pop the cost!!!!
    cost = heuristic(firstnode,problem)
#     cost = 0
    childcontainer.push((firstnode,path,cost) ,cost) #(node,path[],cost),cost
    
#     numNodes = 0
    
    while not childcontainer.isEmpty():
        (curNode,path,cost) = childcontainer.pop()
        if curNode in nodeset: 
            continue
        if problem.isGoalState(curNode):
#             print path
#             print "number of nodes expanded",numNodes
            return path
        nodeset.add(curNode)
#         numNodes += 1

         #succ: (node,path,cost)
        for succ in problem.getSuccessors(curNode):           
#             newCost = cost+succ[2]+heuristic(succ[0],problem)   
            newCost = cost+succ[2]          
            newPath = path + [succ[1]]
            childcontainer.push((succ[0],newPath,newCost),newCost+heuristic(succ[0],problem))


    
    return none

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
