import csv
import optparse


def drange(start, stop, step=1.0):
    "generate between 2 numbers w/ optional step"
    r = start
    while r < stop:
        yield r
        r += step

def get_scale(series, is_y=False, steps=20):
    min_val = min(series)
    max_val = max(series)
    scaled_series = []
    for x in drange(min_val, max_val, (max_val-min_val)/steps):
        if x > 0 and scaled_series and max(scaled_series) < 0:
            scaled_series.append(0.0)
        scaled_series.append(x)
    
    if is_y:
        scaled_series.reverse()
    return scaled_series

def plot_scatter(f, xs, ys, size, pch):
    if f:
        data = [tuple(map(float, line)) for line in csv.reader(open(f))]
        xs = [i[0] for i in data]
        ys = [i[1] for i in data]
    else:
        xs = [float(row.strip()) for row in open(xs)]
        ys = [float(row.strip()) for row in open(ys)]
    
    plotted = set()

    print "-"*(2*len(get_scale(xs, False, size))+2)
    for y in get_scale(ys, True, size):
        print "|",
        for x in get_scale(xs, False, size):
            point = " "
            for (i, (xp, yp)) in enumerate(zip(xs, ys)):
                if xp <= x and yp >= y and (xp, yp) not in plotted:
                    point = pch
                    #point = str(i) 
                    plotted.add((xp, yp))
            if x==0 and y==0:
                point = "o"
            elif x==0:
                point = "|"
            elif y==0:
                point = "-"
            print point,
        print "|"
    print "-"*(2*len(get_scale(xs, False, size))+2)


if __name__=="__main__":

    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', help='a csv w/ x and y coordinates',
                      default=None, dest='f')
    parser.add_option('-x', help='x coordinates',
                      default=None, dest='x')
    parser.add_option('-y', help='y coordinates',
                      default=None, dest='y')
    parser.add_option('-s', '--size',help='y coordinates',
                      default=20, dest='size', type='int')
    parser.add_option('-p', '--pch',help='shape of point',
                      default="x", dest='pch') 


    (opts, args) = parser.parse_args()
    
    plot_scatter(opts.f, opts.x, opts.y, opts.size, opts.pch)

#plot_scatter("test.txt")
#plot_scatter("bigtest.txt")
#plot_scatter("texas.txt")



