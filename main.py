"""
Author: David Moore
Assigment: 4
Course: Python 87B
Instructor: Professor Darwiche
Purpose: to take two sets of data, create two plots highlighting the max and min of both, then create other
data visualizations.  In this case I will create two boxplots on one graph to compare the average rainfall of
Decade 1 and Decade 2.

Citation:
{
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import numpy as np
import webbrowser


class Rainfall():

    def __init__(self, r1={}, r2={}):
        self.r1 = r1
        self.r2 = r2

    def fill_dictionaries(self):

        with open("rainfallSet1.txt") as rain1:
            for line in rain1:
                (key, val) = line.split()
                self.r1[str(key)] = round(float(val), 2)

        with open("rainfallSet2.txt") as rain2:
            for line in rain2:
                (key, val) = line.split()
                self.r2[str(key)] = round(float(val), 2)

    def plot_rain_together(self):

        x = self.r1.keys()
        y1 = self.r1.values()
        y2 = self.r2.values()
        plt.rcParams['figure.figsize'] = [8, 3.5]
        plt.rcParams['figure.autolayout'] = True
        plt.xticks(range(len(self.r1.keys())),self.r1.keys(), rotation='vertical')
        plt.margins(x=0, y=0)
        plt.xlabel('Cities')
        plt.ylabel('Rainfall (inches)')
        fig = plt.gca()
        fig.set_ylim([0, 100])
        plt.plot(x, y1, '-g', label='Decade 1')
        plt.plot(x, y2, '--r', label='Decade 2')
        plt.legend(loc='center right', frameon=False)
        plt.savefig('Rainfall Decade 1 & Decade 2 Line Comparison')
        plt.show()

    def plot_rain_separate(self):

        cities_y1 = list(self.r1.keys())
        values_y1 = list(self.r1.values())
        max_y1 = max(values_y1)
        colors = ['blue' if (bar == max(values_y1)) or (bar==min(values_y1)) else "grey" for bar in values_y1]
        plt.bar(range(len(self.r1)), values_y1, tick_label = cities_y1, color = colors)
        plt.xticks(rotation='vertical', fontsize=8)
        plt.xlabel('City')
        plt.ylabel('Rainfall in Inches')
        plt.title('Average Rainfall: Decade 1')
        plt.savefig('Average Rainfall Decade 1 Barchart')
        plt.show()


        cities_y2 = list(self.r2.keys())
        values_y2 = list(self.r2.values())
        plt.bar(range(len(self.r2)), values_y2, tick_label=cities_y2, color=colors)
        plt.xticks(rotation='vertical', fontsize=8)
        fig = plt.gca()
        fig.set_ylim([0,40])
        plt.xlabel('City')
        plt.ylabel('Rainfall in Inches')
        plt.title('Average Rainfall: Decade 2')
        plt.savefig('Average Rainfall Decade 2 Barchart')
        plt.show()

    def boxplot(self):
        # Please see citation
        webbrowser.open('citation.txt')

        dec1 = list(self.r1.values())
        dec2 = list(self.r2.values())
        data = [dec1, dec2]

        fig, ax1 = plt.subplots(figsize=(10,6))
        bp = ax1.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
        plt.setp(bp['boxes'], color='black')
        plt.setp(bp['whiskers'], color='black')
        plt.setp(bp['fliers'], color='red', marker='+')

        #setting grid for visibility
        ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=.5)

        ax1.set(
            axisbelow=True,
            title='Rainfall Boxplot Decade Comparison',
            ylabel='Rainfall (inches)'
        )

        colors = ['green', 'red']
        sets = len(data)
        medians = np.empty(sets)

        for set in range(sets):
            box = bp['boxes'][set]
            box_x = []
            box_y = []
            for j in range(5):
                box_x.append(box.get_xdata()[j])
                box_y.append(box.get_ydata()[j])
            box_coords = np.column_stack([box_x, box_y])
            # alternate between the two colors
            ax1.add_patch(patch.Polygon(box_coords, facecolor=colors[set%2]))
            med = bp['medians'][set]
            median_x = []
            median_y = []

            for n in range(2):
                median_x.append(med.get_xdata()[n])
                median_y.append(med.get_ydata()[n])
                ax1.plot(median_x,median_y)

            medians[set] = median_y[0]

            ax1.plot(np.average(med.get_xdata()), np.average(data[set]), color ='w', marker='*', markeredgecolor='k')

            ax1.set_ylim(0,100)
            ax1.set_xticklabels(['Decade 1', 'Decade 2'])
        plt.savefig('Boxplot Comparison')
        plt.show()


def main():
    rain = Rainfall()
    rain.fill_dictionaries()
    rain.plot_rain_together()
    rain.plot_rain_separate()
    rain.boxplot()


if __name__ == "__main__":
    main()


