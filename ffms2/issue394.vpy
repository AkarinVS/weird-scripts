import vapoursynth as vs
core = vs.core
import hashlib
import random

if 'a' not in globals():
    a = 'seek-test.mkv'

p = core.lsmas.LWLibavSource(a)
p.set_output(0)
q = core.ffms2.Source(a)
q.set_output(1)

def hash_frame(frame):
    md5 = hashlib.md5()
    for plane in range(frame.format.num_planes):
        for line in frame.get_read_array(plane):
            md5.update(line)
    return md5.hexdigest()

def test(n):
    assert hash_frame(p.get_frame(n)) == hash_frame(q.get_frame(n)), 'frame %d failed' % n

#test(1)
#test(100)
#test(1507)

N = 0
while True:
    print('%d\r' % N, end='')
    test(random.randint(0, p.num_frames-1))
    N += 1
