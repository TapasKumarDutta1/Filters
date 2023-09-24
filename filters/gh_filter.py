# -*- coding: utf-8 -*-
"""GH-filter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zZ469JdSLS9CWrXmm-z5J153qJb9e99
"""

def g_h_filter(data, g, h, dx, dt):
    """
    Apply a 1D Generalized Holt-Winters filter to the input data.

    Parameters:
        data (list): List of data points to be filtered.
        g (float): Smoothing factor for the trend component.
        h (float): Smoothing factor for the noise component.
        dx (float): Initial estimate of the data point.
        dt (float): Time interval between data points.

    Returns:
        list: A list of filtered data points.

    The Generalized Holt-Winters filter is used to smooth time-series data and make
    short-term predictions. It consists of two components: the level (dx) and the trend (dx).
    The filter iterates through the data, updating the level and trend estimates based on the
    input smoothing factors (g and h) and the observed residuals. The filtered results are
    returned as a list.
    """
    initial = dx
    results = []

    for i in data:
        # Update the level estimate based on the current trend estimate
        initial = initial + dx * dt

        # Calculate the residual between the observed data point and the current level estimate
        residual = i - initial

        # Update the trend estimate based on the residual and the trend smoothing factor
        dx = dx + h * residual / dt

        # Calculate the final filtered value based on the current level estimate and the trend smoothing factor
        final = initial + (g * dx / dt)

        # Append the filtered value to the results list
        results.append(final)

    return results