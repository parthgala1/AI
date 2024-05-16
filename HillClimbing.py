def objective(x, target):
    return (x*x) - target

def hill_climbing(target=25, currSol=0.0, epsilon=0.1):
    step_size = target
    while True:
        currObj = objective(currSol, target)
        
        if abs(currObj) < epsilon:
            return currSol
        if currObj > 0:
            currSol -= step_size
        if currObj < 0:
            currSol += step_size
            
        step_size /= 2

print(hill_climbing(target=100))