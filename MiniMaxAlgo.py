import math

def minimax(currentDepth, indexNode, max_min, scores, leafNode, path=[]):
    if currentDepth == leafNode:
        print("Path:", path)
        return scores[indexNode], path    
    if max_min:
        left_score, left_path = minimax(currentDepth + 1,indexNode * 2,False, scores, leafNode, path + [indexNode * 2])
        right_score, right_path = minimax(currentDepth + 1, indexNode * 2 + 1, False, scores, leafNode, path + [indexNode * 2 + 1])
        if left_score > right_score:
            return left_score, left_path
        else:
            return right_score, right_path
    else:
        left_score, left_path = minimax(currentDepth + 1, indexNode * 2,True, scores, leafNode, path + [indexNode * 2])
        right_score, right_path = minimax(currentDepth + 1,indexNode * 2 + 1,True, scores, leafNode, path + [indexNode * 2 + 1])
        if left_score < right_score:
            return left_score, left_path
        else:
            return right_score, right_path

scores = []
                
length = int(input("Enter the Length of the List: "))
for i in range(length):
    num = int(input(f"Enter number {i+1}: "))
    scores.append(num)

lengthNode = int(math.log(len(scores), 2))
max_min = True if (int(math.log(len(scores), 2)) == math.log(len(scores), 2)) else False
print("Minimax Algorithm:")
result, path = minimax(0,0,max_min, scores, lengthNode)
print("Numbers selected on the path:", [scores[node] for node in path])
print("Result:", result)
