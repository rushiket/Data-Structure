def hashTable(arr):
	dic = {}
	for i in arr:
		if i not in dic:
			dic[i] = i
	print(dic)

a = [1,2,3,4,5,6,1,2,3,4,5,6,7,8,9,1,2,3,4]
arr = ["b","a","e","c","i","h","e","a","d","c","b","a"]
hashTable(arr)
