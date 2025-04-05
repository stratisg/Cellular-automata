"""Visualization module."""
import os
import matplotlib.pyplot as plt


class PlotTool:
    """"
    Class that contains all the necessary attributes and methods for
    making plots.
    """
    def __init__(self, xlabel, ylabel, pics_dir, dpi):
        """Initialize the class."""
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.pics_dir = pics_dir
        if not os.path.isdir(pics_dir):
            os.mkdir(pics_dir)
        self.dpi = dpi
    
    def plot_figure(self, data, plot_type, label, figname):
        """Plot the figure corresponding to the data provided."""
        if plot_type == "plot":
            fig = plt.plot(data[0], data[1], label=label)
        elif plot_type == "scatter":
            fig = plt.scatter(data[0], data[1], label=label)
        elif plot_type == "image":
            fig = plt.imshow(data, cmap=plt.cm.binary)
        if label != None:
            plt.legend(frameon=False)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.tight_layout()
        self.save_fig(figname)
        
    def animate_evolution(self):
        """
        Animate evolution of automaton over time.
        """
        pass

    def save_fig(self, figname):
        """Save figure in the corresponding directory."""
        plt.savefig(f"{self.pics_dir}/{figname}.png", dpi=self.dpi)
        plt.close()

