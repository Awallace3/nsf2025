"""
Functions for measuring between points in 3D space
"""

import numpy as np


def calculate_distance(rA, rB):
    """
    Calculate the Euclidean distance between two points in 3D space.
    
    Parameters
    ----------
    rA : array_like
        Coordinates of the first point as a numpy array or array-like object.
        Shape should be (3,) for 3D coordinates.
    rB : array_like
        Coordinates of the second point as a numpy array or array-like object.
        Shape should be (3,) for 3D coordinates.
    
    Returns
    -------
    float
        The Euclidean distance between the two points.
    
    Examples
    --------
    >>> import numpy as np
    >>> point1 = np.array([0, 0, 0])
    >>> point2 = np.array([3, 4, 0])
    >>> distance = calculate_distance(point1, point2)
    >>> print(distance)
    5.0
    """
    # This function calculates the distance between two points given as numpy arrays.
    d = rA - rB
    dist = np.linalg.norm(d)
    return dist


def calculate_angle(rA, rB, rC, degrees=False):
    """
    Calculate the angle at point B formed by the line segments BA and BC.
    
    Parameters
    ----------
    rA : array_like
        Coordinates of the first point as a numpy array or array-like object.
        Shape should be (3,) for 3D coordinates.
    rB : array_like
        Coordinates of the vertex point (where the angle is measured) as a numpy 
        array or array-like object. Shape should be (3,) for 3D coordinates.
    rC : array_like
        Coordinates of the third point as a numpy array or array-like object.
        Shape should be (3,) for 3D coordinates.
    degrees : bool, optional
        If True, return angle in degrees. If False (default), return angle in radians.
    
    Returns
    -------
    float
        The angle at point B in radians (default) or degrees if specified.
        Range is [0, π] radians or [0, 180] degrees.
    
    Examples
    --------
    >>> import numpy as np
    >>> pointA = np.array([1, 0, 0])
    >>> pointB = np.array([0, 0, 0])  # vertex
    >>> pointC = np.array([0, 1, 0])
    >>> angle_rad = calculate_angle(pointA, pointB, pointC)
    >>> angle_deg = calculate_angle(pointA, pointB, pointC, degrees=True)
    >>> print(f"Angle: {angle_rad:.3f} radians, {angle_deg:.1f} degrees")
    Angle: 1.571 radians, 90.0 degrees
    """
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
