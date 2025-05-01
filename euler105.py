#euler 103

import itertools

def file_to_list_of_integer_lists(filepath):
  """Reads a file with comma-separated numbers per line and
  returns a list of lists, where each inner list contains integers.

  Args:
    filepath: The path to the text file.

  Returns:
    A list of lists of integers.
    Returns an empty list if the file cannot be opened.
  """
  all_numbers = []
  try:
    with open(filepath, 'r') as file:
      for line in file:
        # Remove leading/trailing whitespace and split the line by comma
        string_numbers = line.strip().split(',')
        # Convert each string number to an integer
        integer_list = [int(num) for num in string_numbers]
        all_numbers.append(integer_list)
    return all_numbers
  except FileNotFoundError:
    print(f"Error: File not found at '{filepath}'")
    return []

def disjoint(l1, l2):

    for e in l1:

        if e in l2:
            return False

    return True
    

def the_rest(lstt, original):

    output = []

    for element in original:

        if element not in lstt:

            output.append(element)

    return output
    

def test_valid(ch1, ch2):

    if sum(ch1) == sum(ch2):
        return False

    elif len(ch1) > len(ch2):

        if sum(ch1) < sum(ch2):

            return False
    elif len(ch2) > len(ch1):

        if sum(ch2) < sum(ch1):

            return False

    return True

def big_test(dic, test_list):
    
    for config in d[len(test_list)]:

        first_candidates = list(itertools.combinations(test_list, config[0]))
        second_candidates = list(itertools.combinations(test_list, config[1]))

        for c1 in first_candidates:

            for c2 in second_candidates:

                if disjoint(c1, c2):

                    if not test_valid(c1, c2):
                        return False

    return True

                    
           
d = {}

list_of_integer_lists = file_to_list_of_integer_lists("0105_sets.txt")



for s in range(7, 13):

    all_pairs = []

    digs = range(1, s+1)

    for comb in itertools.combinations_with_replacement(digs, 2):

        if (comb[0] + comb[1]) <= s:

            all_pairs.append(comb)

    d[s] = all_pairs


output = 0
    
for this_test_list in list_of_integer_lists:

    if big_test(d, this_test_list):

        output += sum(this_test_list)

        print(this_test_list)

print(output)
