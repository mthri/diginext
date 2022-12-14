import math

def repeat_then_count(data: str, n: int) -> int:
    # how many times we need to repeat?
    repeat_count = math.ceil(n/len(data))

    # repeat
    data = data * repeat_count

    # remove extra values
    data = data[:n]

    return data.count('a')

def fix_str(data: str) -> int:
    remove_count = 0

    current_char = data[0]
    for char in data[1:]:
        if char == current_char:
            remove_count += 1
        else:
            current_char = char

    return remove_count

def swap(array: list) -> int:
    #reference: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
    
    n = len(array)
	
    # create array pairs index and number [(index, value), ...]
    array_position = [*enumerate(array)]

	# sort array base on value.
    array_position.sort(key = lambda it : it[1])

    # create dict(hash map) for track visited elements
    visite = {k : False for k in range(n)}

    answer = 0
    for i in range(n):
        # already swapped or already present at correct position
        if visite[i] or array_position[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not visite[j]:
            # mark node as visited
            visite[j] = True
			
            # move to next node
            j = array_position[j][0]
            cycle_size += 1

        # update answer by adding current cycle
        if cycle_size > 0:
            answer += (cycle_size - 1)

    return answer