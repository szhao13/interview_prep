
def merge_lists(array_0, array_1):
	curr_id_0 = 0
	curr_id_1 = 0
	merged_array = []
	len_0 = len(array_0)
	len_1 = len(array_1)
	total = len_0 + len_1

	for index in range(total):
		if curr_id_0 < len_0:
			if curr_id_1 == len_1 or array_0[curr_id_0] <= array_1[curr_id_1]:
				merged_array.append(array_0[curr_id_0])

				curr_id_0 += 1
				continue
			# print "curr_id_0 is %d" %curr_id_0

		if curr_id_1 < len_1:
			if curr_id_0 == len_0 or array_1[curr_id_1] <= array_0[curr_id_0]:
				merged_array.append(array_1[curr_id_1])

				curr_id_1 += 1
		# print merged_array
	return merged_array


my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]


print merge_lists(my_list, alices_list)