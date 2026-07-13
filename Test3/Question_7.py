'''7. Online Game Leaderboard
An online gaming platform stores players' scores.
Write a program to arrange the scores in descending order so that the
leaderboard can be displayed.'''


scores = [450, 980, 720, 600, 870]

def leaderboard(scores):
    n = len(scores)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if scores[j] > scores[index]:
                index = j
        scores[i], scores[index] = scores[index], scores[i]
    return scores

print(leaderboard(scores))