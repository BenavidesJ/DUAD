def bubble_sort(list_to_sort):
    for outer_idx in range(0, len(list_to_sort) - 1):
        already_swapped = False
        for idx in range(0, len(list_to_sort) - 1 - outer_idx):
            current_element = list_to_sort[idx]
            next_element = list_to_sort[idx + 1]
        
            if current_element > next_element:
                list_to_sort[idx] = next_element
                list_to_sort[idx + 1] = current_element
                already_swapped = True
                
        if not already_swapped:
            return

        
def inverted_bubble_sort(list_to_sort):
    for outer_idx in range(len(list_to_sort) - 1, -1, -1):
        already_swapped = False
        for idx in range(len(list_to_sort) - 1 - outer_idx, -1, -1):
            current_element = list_to_sort[idx]
            previous_element = list_to_sort[idx - 1]
            
            if current_element > previous_element:
                list_to_sort[idx] = previous_element
                list_to_sort[idx - 1] = current_element
                already_swapped = True
                
        if not already_swapped:
            return

        
test_list = [-1, 15, 8, 3, 21, 999, 3]
print('----------Normal-------------------')
bubble_sort(test_list)
print(test_list)
print('----------Invertido----------------')
inverted_bubble_sort(test_list)
print(test_list)