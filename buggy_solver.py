from pulp import *

def solve_buggy_lp():
    prob = LpProblem("Buggy_LP", LpMaximize)
    x = LpVariable("x", lowBound=0)
    y = LpVariable("y", lowBound=0)
    prob += 3*x + 4*y
    prob += x + y <= 10
    prob += 2*x + y <= 5  # Incorrect constraint (too restrictive)
    prob.solve()
    return {"x": x.varValue, "y": y.varValue, "objective": prob.objective.value()}