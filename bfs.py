def mean(l1,l2):
    n1 = len(l1)
    n2 = len(l2)

    l, r = 0, n1
    ans = 0
    while l <= r:
        p1 = int((l + r) / 2)
        p2 = int(((n1 + n2 +1) / 2)-p1)

        maxx = l1[p1 -1]
        may = l2[p2 -1]
        mix = l1[p1 ]
        miy = l2[p2 ]
        if maxx <= miy and may <=mix:
           if (n1+n2) % 2 == 0:
               return (max(maxx,may) + max(mix,miy))/2
           else:
               return max(maxx,may)
        elif maxx > may:
            print('ddd')
            r = p1-1
        else:
            print('llll')
            l = p1 +1
    # return  ans


print(mean([1,3,8,9,15],[7,11,18,19,21,25]))