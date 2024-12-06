import numpy as np

def change_of_basis(*args):    

    """ 
    Description
    -----------
    
    This function calculates the coordinates of a vector with respect to the basis_a,
    provided that a basis a and b are given and that the coordinates of the vector with respect
    to the basis_b are also given. If only one basis is given, basis_a will be assumed to
    be the canonical basis for that particular vector space. KEEP IN MIND that this function
    does not check wether basis_a and basis_b are indeed basis of the vector space.
    
    Examples
    --------
    >>> x = change_of_basis([2, 2.5], [[np.sqrt(2)/2, np.sqrt(2)/2], [-np.sqrt(2)/2, np.sqrt(2)/2]], [[1, 0], [0, 1]])

    >>> x
    [[3.18198052 0.35355339]] # Coordinates of the vector [2, 2.5] written with respect to the canonical base rotated 90 degrees counterclockwise.

    >>> y = change_of_basis([1, 0, 1], [[2, 3, 1], [2, 2, 1], [-1, 0, -2]])

    >>> y
    [[ 1  3 -1]] # Coordinates of the vector [1, 3, -1] written with respect to the canonical base.

    >>> z = change_of_basis([1, -1, 2], [[1, 1, 1], [1, 0, 1], [0, 1, -1]], [[2, 3, 1], [2, 2, 1], [-1, 0, -2]])

    >>> z
    [[-1. -1.  2.]] # Coordinates of the vector [-2, 1, -4] written with respect to the basis_a = [[1, 1, 1], [1, 0, 1], [0, 1, -1]].

    """

    if len(args) == 2:
        
        """ If basis_a is not given it is assumed to be the canonical n-dimensional basis.
        Thus the matrix of change of basis has a simpler expression. """

        # Calculate the matrix of change of basis
        mat_cb = np.asmatrix(args[1]).transpose()
    
    else:

        """ This is the case where three arguments have been passed to the function. In such
        case, the second argument is most probably not the canonical base. With that, the matrix
        of change of basis is to be calculated. """

        # Calculate the matrix of change of basis
        basis_a = np.asmatrix(args[1])
    
        for i in range(len(args[0])):
            weigths_array = []
            for vector in args[2]:
                weigths_array.append(np.linalg.solve(basis_a.transpose(), vector))
        
        mat_cb = np.asmatrix(weigths_array).transpose()

    return mat_cb @ args[0]



def translation(point, vector):

    """ 
    Description
    -----------
    
    This function applies a translation to the given point based on the provided vector
    and is versatile enough to handle translations in n-dimensional vector spaces. KEEP IN MIND
    that both parameters must have the same size. 
    
    Example
    --------
    >>> x = translation([3, 4, -1], [1, 4, 0])

    >>> x
    [ 4  8 -1] # Translation applied to the point [3, 4, -1] according to the direction given by the vector [1, 4, 0].

    """

    for i in range(len(point)):
        vector[i] += point[i]

    return np.array(vector)



def homothety(center, point, ratio = 1.01):

    """ 
    Description
    -----------

    This function applies a homothety to the point parameter with respect to the center and ratio.

    Example
    --------
    >>> x = homothety([-2, 2], [-1, -1], 2)

    >>> x
    [ 0 -4] # Homothety to the point [-1, -1] with center [-2, 2] and ratio 2.

    """
    
    return ratio*np.array(point) + (1-ratio)*np.array(center)



def rotation(point, alpha, beta, gamma):

    """ 
     Description
    -----------
    
    This function rotates a point in 3D space based on the specified values of alpha, beta, and gamma. Each of these
    values represents the angle by which the point is rotated around the Z, Y, and X axes, respectively. In aviation
    lingo, this movements are also called yaw, pitch and roll.

    Example
    --------
    >>> x = rotation([1, 1, 1], np.pi/2, np.pi/2, -np.pi)

    >>> x
    [ 0. -1. -1.]

    """

    roll_matrix = np.array([[1,             0,              0], 
                            [0, np.cos(gamma), -np.sin(gamma)], 
                            [0, np.sin(gamma),  np.cos(gamma)]])
    yaw_matrix = np.array([[np.cos(alpha), -np.sin(alpha), 0],
                           [np.sin(alpha),  np.cos(alpha), 0],
                           [0            ,              0, 1]])
    pitch_matrix = np.array([[np.cos(beta), 0, np.sin(beta)],
                             [0            , 1,            0], 
                             [-np.sin(beta), 0, np.cos(beta)]])
    
    rotation_matrix = yaw_matrix @ pitch_matrix @ roll_matrix
    coords = rotation_matrix @ point
    for i in range(len(coords)):
        coords[i] = int(coords[i])

    return coords



def xy_projection(point):

    """ 
     Description
    -----------
    
    ************************************************************************
    ************************************************************************
    ************************************************************************
    ************************************************************************

    Example
    --------
    >>> x = rotation([1, 1, 1], np.pi/2, np.pi/2, -np.pi)

    >>> x
    [ 0. -1. -1.]

    """

    xy_projection_matrix = np.array([[1, 0, 0], 
                                     [0, 1, 0], 
                                     [0, 0, 0]])
    coords = xy_projection_matrix @ point
    coords = coords[:-1]
    
    return coords