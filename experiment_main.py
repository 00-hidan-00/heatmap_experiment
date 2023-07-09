import matplotlib.pyplot as plt
import numpy as np

vegetables = ['5.00 M', '10.00 M', '15.00 M', '20.00 M', '25.00 M', ]

farmers = [
    2,
    4,
    6,
    8,
    10,
    12,
    14,
]

harvest = np.array([[8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 3],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 1],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0], ])


def main(cbar_kw=None, cbarlabel="", ):
    vegetables.reverse()

    fig, ax = plt.subplots()
    im = ax.imshow(harvest)

    if cbar_kw is None:
        cbar_kw = {}
    # cmap = "magma_r"
    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(farmers)), labels=farmers)
    ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Loop over data dimensions and create text annotations.
    ax.set_title("Harvest of local farmers (in tons/year)")
    fig.tight_layout()
    plt.show()

    return im, cbar


if __name__ == "__main__":
    main()
