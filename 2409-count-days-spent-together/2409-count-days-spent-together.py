class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s = 0
        for i in d:
            s += i
        def convert(s):
            a = s.split("-")
            x = [int(i) for i in a]
            return x
        aa = convert(arriveAlice)
        print(aa)
        la = convert(leaveAlice)
        print(la)
        ab = convert(arriveBob)
        lb = convert(leaveBob)
        alicear = aa[1]
        for i in range(aa[0]-1):
            alicear += d[i]
        alicedr = la[1]
        for j in range(la[0]-1):
            alicedr += d[j]
        bobar = ab[1]
        for l in range(ab[0]-1):
            bobar += d[l]
        bobdr = lb[1]
        for k in range(lb[0]-1):
            bobdr += d[k]

        print(alicear)
        print(alicedr)
        print(bobar)
        print(bobdr)
        start = max(alicear, bobar)
        end = min(alicedr, bobdr)

        return max(0, end - start + 1)