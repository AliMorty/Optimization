from cvxopt import matrix, solvers
P = 2*matrix([[2.0, 0.0], [0.0, 18.0] ])
q = matrix([1.0, 1.0])
G = matrix([[-2.0,-1.0, -1.0, 0.0],[-1.0,-3.0, 0.0, -1.0]])
h = matrix([-1.0, -1.0, 0.0,0.0])
A = matrix([1.0, 1.0], (1,2))
b = matrix(1.0)
sol=solvers.qp(P, q, G, h)