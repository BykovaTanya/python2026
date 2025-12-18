def push_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores
print(push_score(1))
print(push_score(2))

def push_score(score, scores=[]):
    scores.append(score)
    return scores
push_score(3)

print(push_score)
 
def top_scores(scores, n=3):
    scores.sorted
    return scores[:n]
top_scores(4)
print(top_scores)
