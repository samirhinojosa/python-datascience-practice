from matplotlib import pyplot as seg


mentions = [500, 505]
years = [2013, 2014]

seg.bar([2012.6, 2013.6], mentions, 0.8)
seg.xticks(years)
seg.ylabel("# algo")
seg.axis([2012.5, 2014.5, 499, 506])
seg.title("Loog at the huge")
seg.savefig("images/bar_char2", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)