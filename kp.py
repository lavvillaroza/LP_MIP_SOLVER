from pulp import *

def solve_kp():
    prob = LpProblem("KP", LpMaximize)
    a = LpVariable("a", cat="Binary")
    b = LpVariable("b", cat="Binary")
    c = LpVariable("c", cat="Binary")
    prob += 5*a + 3*b + 2*c
    prob += 2*a + b + c <= 10
    prob.solve()    
    print ("A=", a.varValue)
    print ("B=", b.varValue)
    print ("C=", c.varValue)
    print ("Objective=", prob.objective.value())
    return {"a": a.varValue, "b": b.varValue, "c": c.varValue, "objective": prob.objective.value()}    


solve_kp()

