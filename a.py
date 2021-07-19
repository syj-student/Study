def  merge_sort(lst):
	lstlen = len(lst)
	if lstlen <= 1:
		return lst
	mid = lstlen // 2
	g1 = merge_sort(lst[:mid])
	g2 = merge_sort(lst[mid:])
	ret = list()
	while g1 and g2:
		if g1[0] < g2[0]:
			ret.append(g1.pop[0])
		else:
			ret.append(g2.pop[0])

	return ret