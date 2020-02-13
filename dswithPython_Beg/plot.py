from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#create a line chart, years on x-axis and gdp on y-axis
plt.plot(years, gdp, color="green", marker="o", linestyle="solid")

#add a lable to the y-axis
plt.ylabel("Bilions of $")

plt.savefig("dswithPython_Beg/new", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)


