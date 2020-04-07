import math
import random

scales = [2**2, 2**4, 2**6, 2**8, 2**10, 2**12, 2**14, 2**16]


l = 2**31

N = 100000

def get_one(L, delta):
    i = random.randint(0, L/delta)
    return 1.0*(i * delta)/L


for scale in scales:
    d_min = 1.0 * scale / l
    # d_max = math.sqrt(2)
    d_max = 2.0
    print "d_min= ", d_min, "d_max=", d_max
    file_name = "synthetic+{}+{}+{}.data".format(str(N), str(d_min), str(d_max))
    print "writing to: ", file_name
    with open(file_name, 'w') as f:
        for t in xrange(N):
            x, y = get_one(l, scale), get_one(l, scale)
            print >> f, "{}\t{} {}".format(str(t), str(x), str(y))
