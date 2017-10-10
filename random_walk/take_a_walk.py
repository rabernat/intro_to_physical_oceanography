from pylab import *
import walkers

N = 200
mypoints = [walkers.RandomWalker() for n in range(N)]

# define points for drawing a circle
x_circ = cos(linspace(0,2*pi,100))
y_circ = sin(linspace(0,2*pi,100))

Nt = 100
close('all')
figure(figsize=(8,4))
clf()
for n in range(Nt):
    subplot(121)
    cla()
    xlim([-20,20]); ylim([-20,20])
    # moments
    x,y = 0.,0.
    x2,y2 = 0.,0.
    D = 0.
    for w in mypoints:
        p=plot(w.x_hist, w.y_hist, '-')
        plot(w.x,w.y, '.', color=p[0].get_color())
        x += w.x
        y += w.y
        x2 += w.x**2
        y2 += w.y**2
        D += w.dist_from_origin()
        w.step_forward()
    x,y = x/N, y/N
    x2,y2 = x2/N, y2/N
    D = D/N
    r = sqrt(x2+y2)
    plot(r*x_circ, r*y_circ, 'k')
    title('n = %g' % n)
    subplot(122)
    plot(n, r, 'k.');
    #plot(n, D, 'r.');
    xlim((0,Nt)); ylim((0,12))
    xlabel('time')
    title('RMS distance from origin')
    tight_layout()
    savefig('frames/random_walk_%04d.png' % n)
    #show()
    #pause(0.001)
