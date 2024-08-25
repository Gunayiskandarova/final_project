a=[1,4,7,6,9]
def selection(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if a[j]< min_index:
                min_index =j
            temp=a[i]
            a[min_index ]= a[i]
            a[min_index]=temp
print(selection(a))