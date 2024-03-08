lst = [3,17,15,8,11,2,19,5]

def merge_sort(s, e, lst):
    if s > e:
        return
    mid = (s+e) //2
    merge_sort(s, mid, lst)
    merge_sort(mid+1, e, lst)


merge_sort(0, len(lst), lst)
    