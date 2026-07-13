'''4. Rank Participants
A sports academy has recorded the timings (in seconds) of participants in
a race.
Write a program to arrange the timings from the fastest to the slowest so
that the winners can be announced'''

def Rank(timings):
    n = len(timings)
    for i in range(n):
        for j in range(n - i - 1):
            if timings[j] > timings[j + 1]:
                timings[j], timings[j + 1] = timings[j + 1], timings[j]

    return timings
timings = [11.5, 10.3, 13.8, 9.9, 13.4]
print("Fastest to Slowest: ",Rank(timings))
