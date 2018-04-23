'''
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j+1]<arr[j]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr

if __name__=='__main__':

    row = input('请用空格为间隔输入数字')

    num=[int(n) for n in row.split()]
    print(bubbleSort(num))
'''
'''
def selectionSort(arr):
    # 选择排序
    count = len(arr)
    for i in range(0, count-1):
        minIndex = i
        for j in range(i+1, count):
            if arr[j]<arr[minIndex]:
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]
    return arr

if __name__=='__main__':

    row = input('请用空格为间隔输入数字')

    num=[int(n) for n in row.split()]
    print(selectionSort(num))
'''
'''
def insertionSort(arr):
    count=len(arr)
    for i in range(1,count):
        preIndex=i-1
        current=arr[i]
        while (arr[preIndex]>current) and (preIndex>=0):
            arr[preIndex+1]=arr[preIndex]
            preIndex-=1
        arr[preIndex+1]=current
    return arr

if __name__=='__main__':

    row = input('请用空格为间隔输入数字')

    num=[int(n) for n in row.split()]
    print(insertionSort(num))
'''
'''
def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = int(count//step)
    while group > 0:
        for i in range(0,int(group)):
            j = i + group
            while j < count:
                k = j - group
                key = lists[int(j)]
                while k >= 0:
                    if lists[int(k)] > key:
                        lists[int(k + group)] = lists[int(k)]
                        lists[int(k)] = key
                    k -= group
                j += group
        group //= step
    return lists
if __name__=='__main__':

    row = input('请用空格为间隔输入数字')

    num=[int(n) for n in row.split()]
    print(shell_sort(num))
'''

'''
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)
if __name__=='__main__':

    row = input('请用空格为间隔输入数字')

    num=[int(n) for n in row.split()]
    print(merge_sort(num))
'''
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

if __name__=='__main__':

    row = input('请用空格为间隔输入数字')

    num=[int(n) for n in row.split()]
    print(quick_sort(num,0,len(num)-1))