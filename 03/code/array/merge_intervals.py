class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i
    return out

def print_inter(intervals):
    res = []
    for i in intervals:
        res.append('['+str(i.start)+','+str(i.end)+']')
    print("".join(res))

    