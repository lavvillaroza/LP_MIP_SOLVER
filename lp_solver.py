from pulp import LpMaximize, LpProblem, LpVariable

def solve_lp():
    prob = LpProblem("Simple_LP", LpMaximize)
    x = LpVariable("x", lowBound=0)
    y = LpVariable("y", lowBound=0)
    prob += 3*x + 4*y
    prob += x + y <= 10
    prob += 2*x + y <= 15
    prob.solve()
    return {"x": x.varValue, "y": y.varValue, "objective": prob.objective.value()}


solve_lp()