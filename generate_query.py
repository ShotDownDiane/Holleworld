import sys
import struct
from collections import deque

if len(sys.argv) != 4:
    print "Usage: "
    print "python script nb_points window_size output_file"
    assert 0

nb_points, window_size = map(int, sys.argv[1:-1])

assert nb_points > 0 and window_size > 0

def front(q):
    x = q.popleft()
    q.appendleft(x)
    return x


with open(sys.argv[-1], 'w') as fwrite, open("./yfcc-all-data.txt") as fin:
    head = 0
    q = deque()
    for i in xrange(nb_points):
        line = fin.readline()
        t = int(line.split('\t')[0])
        assert t >= head
        head = t
        # print str(i)
        fwrite.write(struct.pack('I', i))
        q.append((t, i))
        while len(q) and head - front(q)[0] >= window_size:
            # print str(front(q)[1])
            fwrite.write(struct.pack('I', front(q)[1]))
            q.popleft()
        # if i % 111111 == 0:
        #     print i, len(q)
    while len(q) :
        # print str(front(q)[1])
        fwrite.write(struct.pack('I', front(q)[1]))
        q.popleft()


