def bubble_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise TypeError("Esta funcion solo acepta listas como parametro")
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