def merge_sort(data_list, key_index=0, reverse=False):
    if len(data_list) > 1:
        mid = len(data_list) // 2
        left_half = data_list[:mid]
        right_half = data_list[mid:]

        # Recursión en ambas mitades
        merge_sort(left_half, key_index, reverse)
        merge_sort(right_half, key_index, reverse)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            # Comparar en base al key_index (0 = Velocidad, 1 = Orientación, 2 = Triage)
            if (left_half[i][key_index] > right_half[j][key_index] and reverse) or (left_half[i][key_index] < right_half[j][key_index] and not reverse):
                data_list[k] = left_half[i]
                i += 1
            else:
                data_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data_list[k] = right_half[j]
            j += 1
            k += 1

    return data_list