list1=[1,2,3];
list2=['a','b','c',''];
n = len(list1);
l=[ ];
for i in range(n):
	l.append(list1[i]);
	l.append(list2[i]);
print l;
