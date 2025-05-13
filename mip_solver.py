from pulp import *

def solve_knapsack():
    prob = LpProblem("Knapsack", LpMaximize)
    a = LpVariable("a", cat="Binary")
    b = LpVariable("b", cat="Binary")
    c = LpVariable("c", cat="Binary")
    prob += 5*a + 3*b + 2*c
    prob += 2*a + b + c <= 10
    prob.solve()
    return {"a": a.varValue, "b": b.varValue, "c": c.varValue, "objective": prob.objective.value()}