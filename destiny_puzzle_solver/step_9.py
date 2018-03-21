# Edit these two values.  Enter data by columns, top to bottom, left to right
INFLUX = 590
arr = [[650,460,590,-520,-640], 
       [360,400,420,-340,-420], 
       [270,310,180,-260,-330], 
       [130,60,210,-70,-130], 
       [40,30,30,-40,-10]]
# ^ represents an influx of 590 and this
#   array of capacitance/resistance: 650  360  270  130  40
#                                    460  400  310   60  30
#                                    590  420  180  210  30
#                                   -520 -340 -260  -70 -40
#                                   -640 -420 -330 -130 -10
# You most likely don't need to edit anything under this line.

# If you can't find a solution, you may need to change the target total, which
# was 730 for most people.  The overall goal is for you and your fireteam to have
# the same sum after selecting your nodes, so try different values here.
TARGET_TOTAL = 730

def f1(lIn=[[]]):
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        result = INFLUX + lIn[0][a] + lIn[1][b] + lIn[2][c] + lIn[3][d] + lIn[4][e]
                        if result == TARGET_TOTAL:
                            print("{} = {} + {} + {} + {} + {} + {} ".format(result, INFLUX, lIn[0][a], lIn[1][b], lIn[2][c], lIn[3][d], lIn[4][e]))
                            return [a, b, c, d, e]

match = f1(arr)

print("Winner {}".format(match))
