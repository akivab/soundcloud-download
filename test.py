'''
Created on Jan 9, 2011

@author: akiva
'''
def exists(l, list):
    try:
        list.index(l)
        return True
    except Exception:
        return False
FILE = open("input.txt", "r")
for i in FILE.readlines():
    m = [j.strip() for j in sorted(i.split(' ')[1:])]
    if len(m)==0:
        continue
    r = range(0,len(''.join(m))+1)
    final = [None for i in r]
    final[0] = True
    final_arr = [None for i in r]
    final_arr[0] = m
    for i in r:
        for word in m:
            if i>=len(word) and final[i-len(word)] and exists(word, final_arr[i-len(word)]):
                if final[i]:
                    tmp = ("" if type(final[i-len(word)]) == bool else final[i-len(word)])+word
                    if tmp < final[i]:
                        final[i] = tmp
                        tmp = final_arr[i-len(word)]
                        final_arr[i-len(word)] = tmp[:]
                        b = tmp[:]
                        b.remove(word)
                        final_arr[i] = b
                else:
                    final[i] = ("" if type(final[i-len(word)]) == bool else final[i-len(word)])+word
                    tmp = final_arr[i-len(word)]
                    final_arr[i-len(word)] = tmp[:]
                    b = tmp[:]
                    b.remove(word)
                    final_arr[i] = b 
    print final[len(r)-1]