# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)

# define the model
class Hanoi(ACTR):
    goal=Buffer()
    A = Buffer()
    B = Buffer()
    C = Buffer()
    A.set("[1,2,3]")
    B.set("[]")
    C.set("[]")
    print "Peg A has disks " + str(A.chunk) + ", peg B has disks " + str(B.chunk) + ", peg C has disks " + str(C.chunk) + "."


    def stepOne(goal='action:hanoi current:a123bc target:!a123bc'):
        A.set("[1,2]")
        C.set("[3]")
        print "Disk 3 was moved to peg C."
        goal.modify(current='a12bc3')        
    def stepTwo(goal='action:hanoi current:a12bc3 target:!a12bc3'):
        A.set("[1]")
        B.set("[2]")
        print "Disk 2 was moved to peg B."
        print "Peg A has disks " + str(A.chunk) + ", peg B has disks " + str(B.chunk) + ", peg C has disks " + str(C.chunk) + "."
        goal.modify(current='a1b2c3')        
    def stepThree(goal='action:hanoi current:a1b2c3 target:!a1b2c3'):
        C.set("[]")
        B.set("[2,3]")
        print "Disk 3 was moved to peg B."
        print "Peg A has disks " + str(A.chunk) + ", peg B has disks " + str(B.chunk) + ", peg C has disks " + str(C.chunk) + "."
        goal.modify(current='a1b23c')        
    def stepFour(goal='action:hanoi current:a1b23c target:!a1b23c'):
        C.set("[1]")
        A.set("[]")
        print "Disk 1 was moved to peg C."
        print "Peg A has disks " + str(A.chunk) + ", peg B has disks " + str(B.chunk) + ", peg C has disks " + str(C.chunk) + "."
        goal.modify(current='ab23c1')        
    def stepFive(goal='action:hanoi current:ab23c1 target:!ab23c1'):
        A.set("[3]")
        B.set("[2]")
        print "Disk 3 was moved to peg A."
        print "Peg A has disks " + str(A.chunk) + ", peg B has disks " + str(B.chunk) + ", peg C has disks " + str(C.chunk) + "."
        goal.modify(current='a3b2c1')        
    def stepSix(goal='action:hanoi current:a3b2c1 target:!a3b2c1'):
        C.set("[1,2]")
        B.set("[]")
        print "Disk 2 was moved to peg C."
        print "Peg A has disks " + str(A.chunk) + ", peg B has disks " + str(B.chunk) + ", peg C has disks " + str(C.chunk) + "."
        goal.modify(current='a3bc12')        
    def stepSeven(goal='action:hanoi current:a3bc12 target:!a3bc12'):
        C.set("[1,2,3]")
        A.set("[]")
        print "Disk 3 was moved to peg C."
        goal.modify(current='abc123')        


    def hanoiFinished(goal='action:hanoi current:?x target:?x'):
        print 'Finished Hanoi'
        goal.clear()
    
        
# run the model        
model=Hanoi()
ccm.log_everything(model)
model.goal.set('action:hanoi current:a123bc target:abc123')
model.run()


"""
[
    [#123##,,],
    [12,3,],
    [1,3,2],
    [,1,23],
    [3,1,2],
    [3,12,],
    [,123,],
    [12,,3],
    [13,,2],
    [,13,2],
    [,12,3],
    [1,2,3],
    [13,2,],
    [2,13,],
    [2,1,3],
    [1,23,],
    [23,1,],
    [,23,1],
    [,2,13],
    [2,,13],
    [23,,1],
    [3,2,1],
    [2,3,1],
    [3,,12],
    [,3,12],
    [,,123]
]
"""
