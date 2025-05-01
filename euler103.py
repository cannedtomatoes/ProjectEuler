#euler 103

import itertools

def the_rest(lstt, original):

    output = []

    for element in original:

        if element not in lstt:

            output.append(element)

    return output
    

def test(lst):

    

    length = len(lst)

    for i in range(1, length):

        j = length - i

        for c in itertools.combinations(lst, i):

            ch = the_rest(c, lst)

            if sum(c) == sum(ch):
                return False

            elif len(c) > len(ch):

                if sum(c) < sum(ch):

                    return False
            elif len(ch) > len(c):

                if sum(ch) < sum(c):

                    return False

    return True
           

s1 = (19, 30, 37, 38, 39, 41, 44)

checked = []

current_best_sum = sum(s1)
current_best_list = s1

max_gap = 4



while True:

    print("max_gap =", max_gap)

    all_choices = []

    for n in s1:

        choices = []

        for m in range((n-max_gap), (n+max_gap+1)):
            choices.append(m)

        all_choices.append(choices)

    #print(all_choices)


    for num0 in all_choices[0]:

        for num1 in all_choices[1]:

            for num2 in all_choices[2]:

                for num3 in all_choices[3]:

                    for num4 in all_choices[4]:

                        for num5 in all_choices[5]:

                            for num6 in all_choices[6]:

                                s = [num0, num1, num2, num3, num4, num5, num6]

                                if sum(s) > current_best_sum:
                                    continue

                                if s in checked:

                                    continue
                                else:

                                    checked.append(s)

                                    if sum(s) < current_best_sum:

                                        #print("Checking", s)

                                        if test(s):
                                            print("Winner:", s, sum(s))
                                            current_best_sum = sum(s)
                                            current_best_list = s
                                            

    max_gap += 1
