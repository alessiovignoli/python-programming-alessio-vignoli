# SW

parameters = { 'match': 2, 'mismatch': -1, 'gap': -2 }
s1 = 'CTCGCGCTATGC'
s2 = 'TATGTAGCGAC'

#print(max_I, max_J)

def SW (parameters, s1, s2):

    max_I = 0
    max_J = 0
    row = len(s1) + 1
    col = len(s2) + 1
    M = []
    T = []

    for i in range(row):
        M.append([])
        T.append([])
        for j in range(col):
            M[i].append(0)
            T[i].append('0')

    #print ( M, T)

    highest_score = -1

    for i in range(1, row):
        for j in range(1, col):

            scores = [0]

            # diag

            if s1[i-1] == s2[j-1]:
                scores.append( M[i-1][j-1] + parameters['match'] )

            else:
                scores.append( M[i-1][j-1] + parameters['mismatch'] )

            # left

            scores.append( M[i][j-1] + parameters['gap'] )

            # up

            scores.append( M[i-1][j] + parameters['gap'] )

            # choose max

            if max(scores) == scores[0]:
                M[i][j] = 0

            elif max(scores) == scores[1]:
                M[i][j] = scores[1]
                T[i][j] = 'D'

            elif max(scores) == scores[2]:
                M[i][j] = scores[2]
                T[i][j] = 'L'

            else:
                M[i][j] = scores[3]
                T[i][j] = 'U'

            # check the highest

            if M[i][j] >= highest_score:
                max_I = i
                max_J = j
                highest_score = M[i][j]

    for i in range(row):
        print(M[i])

    for i in range(row):
        print(T[i])
            
    print('the highest value is: %d' %highest_score)
    print('the indexes of the highest value are: row = %d, column = %d'  %(max_I, max_J))

SW(parameters, s1, s2)                                                                    

#for i in range(6):
#    print(M[i])

#for i in range(5):
#    print(T[i])

#print( highest_score, max_I, max_J )
