from __future__ import division
from component import *
from mpi4py import MPI
import numpy


class Var_x0(SimpleComponent):

    def _declare(self):
        return 'x0', 1

    def _initializeArguments(self):
        self.localSize = 1


class Var_xi(SimpleComponent):

    def _declare(self):
        return 'x', 1

    def _initializeArguments(self):
        self.localSize = 1


class Var_yi(SimpleComponent):

    def _declare(self):
        return 'y', 1

    def _initializeArguments(self):
        self.localSize = 1
        self._addArgument('x0', [0])
        self._addArgument('xi', [0])


class Var_yi(SimpleComponent):

    def _declare(self):
        return 'y', 1

    def _initializeArguments(self):
        self.localSize = 1


#setting up multiple copies for multi-point
s_comps = []
for i in xrange(2):
    var_list = [Var_xi(i),Var_yi(i)] #a Component is defined as a collection of specific variables!
    s_comp = SerialComponent('pt', var_list ,i) 
    s_comps.append(s_comp)

#explicit parallelization for multi-point
p_comp = ParallelComponent('pts', s_comps)

#top of level execution
main = SerialComponent('main',[ Var_x0(), p_comp,])
    
print main.variables
main.initialize()
if MPI.COMM_WORLD.rank is 0 or True:
    print 'vVec', main.vVec
    print 'cVec', main.cVec
