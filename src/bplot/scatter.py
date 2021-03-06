from bplot.check_data import check_data


def scatter(
    x, y, color="tab:blue", label="", style="o", size=1.0, alpha=1.0, ax=None, **kws
):
    """Draw scatter plot.

    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of x-axis data for which points are drawn.

    y : {numpy.array, pandas.core.series.Series}
        The vector of y-axis data for which points are drawn.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    style : string, 'o' by default
        The shape of the points to draw.

    size : int, 1 by default
        The size of the points to draw.  In matplotlib terms, this is equivalent to mpl.rcParam['lines.markersize'] = 6**(size + 1).

    alpha : float, 1.0 by default
        The transparency of the color.  Values between 0 (transparent) and 1 (opague) are allowed.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    x, y, ax = check_data(x, y, ax)

    out = ax.scatter(
        x, y, c=color, label=label, marker=style, s=6 ** (size + 1), alpha=alpha, **kws
    )
    return out
