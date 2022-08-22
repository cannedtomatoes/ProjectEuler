#euler 109

import itertools

def labels(throws):

    return [throws[0][0], throws[1][0], throws[2][0]]

def nums(throws):

    return [throws[0][1], throws[1][1], throws[2][1]]

def points(throws):

    return [throws[0][2], throws[1][2], throws[2][2]]

def throws_with_label(throws, label):

    output = []

    for t in throws:

        if t[0] == label:

            output.append(t)

    return output

darts = []

darts.append(['S', 25, 25])
darts.append(['D', 25, 50])
darts.append(['Z', 0, 0])

for i in range(1, 21):

    darts.append(['S', i, i])
    darts.append(['D', i, 2*i])
    darts.append(['T', i, 3*i])

c = list(itertools.combinations_with_replacement(darts, 3))

total = 0
prev = 0

for throw in c:

    if sum(points(throw)) < 100:

        d_count = labels(throw).count('D')

        z_count = labels(throw).count('Z')

        if d_count == 1:

            total += 1

        elif d_count == 2:

            d_throws = throws_with_label(throw, 'D')

            throw1 = d_throws[0]
            throw2 = d_throws[1]

            if throw1[1] == throw2[1]:

                total +=1

            else:

                total += 2

        elif d_count == 3:

            unique_nums = len(set(nums(throw)))

            total += unique_nums

        #added = total - prev
        #if added > 0:

            #print(throw)
            #print("Added " + str(added))
            #input()
        #prev = total

print()        
print(total)
