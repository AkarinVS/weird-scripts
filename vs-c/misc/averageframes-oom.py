import vapoursynth as vs
core = vs.core

c = core.std.BlankClip()
i = 0
while True:
    print('\r%d' % i, end='')
    i += 1
    d = core.misc.AverageFrames([c,c,c], [0.1,0.3,0.6])
