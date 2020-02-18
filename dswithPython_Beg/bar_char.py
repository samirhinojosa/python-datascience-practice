from matplotlib import pyplot as plt


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West side story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(movies, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("Quantity of awards earned by movies")

plt.savefig("images/bar_char", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)