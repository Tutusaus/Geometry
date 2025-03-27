import numpy as np
import numpy.typing as npt

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



def translation(point: list, vector: list) -> npt.NDArray:

    """ 
    Description
    -----------
    
    This function applies a translation to the given point based on the provided vector
    and is versatile enough to handle translations in n-dimensional vector spaces. If point
    and vector don't have the same size, they must be broadcastable to a common shape
    (which becomes the shape of the output).
    
    Example
    --------
    >>> x = translation([3, 4, -1], [1, 4, 0])

    >>> x
    [ 4  8 -1] # Translation applied to the point [3, 4, -1] according to the direction given by the vector [1, 4, 0].

    """

    result = np.add(point, vector)

    return result



def homothety(center: list, point: list, ratio: float = 1.01) -> npt.NDArray[np.float64]:

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

    result = ratio*np.array(point) + (1-ratio)*np.array(center)
    
    return result



def rotation(point: list, alpha: float, beta: float, gamma: float) -> npt.NDArray[np.float64]:

    """ 
     Description
    -----------
    
    This function rotates a point in 3D space according to the specified angles alpha, beta, and gamma.
    These angles correspond to counterclockwise rotations around the X, Y, and Z axes, respectively, when
    viewed from the positive direction of each axis. In aviation lingo, this movements are also called roll,
    pitch and yaw. Note in the examples the non-commutativity of rotation composition.

    Example
    --------
    >>> x = rotation([1, 1, 1], np.pi/2, np.pi/2, -np.pi)

    >>> x
    [ 0. -1. -1.]

    >>> y = rotation(rotation(rotation([1, 1, 1], np.pi/2, 0, 0), 0, np.pi/2, 0), 0, 0, np.pi/2)

    >>> y
    [ 1.  1. -1.]

    >>> z = rotation(rotation(rotation([1, 1, 1], 0, 0, np.pi/2), 0, np.pi/2, 0), np.pi/2, 0, 0)

    >>> z
    [ 1. -1.  1.]

    """

    roll_matrix = np.array([[1,             0,              0], 
                            [0, np.cos(alpha), -np.sin(alpha)], 
                            [0, np.sin(alpha),  np.cos(alpha)]])
    pitch_matrix = np.array([[np.cos(beta), 0, np.sin(beta)],
                             [0            , 1,            0], 
                             [-np.sin(beta), 0, np.cos(beta)]])
    yaw_matrix = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                           [np.sin(gamma),  np.cos(gamma), 0],
                           [0            ,              0, 1]])
    
    rotation_matrix = yaw_matrix @ pitch_matrix @ roll_matrix
    result = rotation_matrix @ point

    return result



def xy_projection(point: list) -> npt.NDArray[np.float64]:

    """ 
     Description
    -----------
    
    This function projects a point in 3D space onto the XY-plane.
    This is also known as a parallel projection.

    Example
    --------
    >>> x = xy_projection([3, 4, 5])

    >>> x
    [3 4]

    """

    xy_projection_matrix = np.array([[1, 0, 0], 
                                     [0, 1, 0], 
                                     [0, 0, 0]])
                                    
    result = xy_projection_matrix @ point
    result = result[:-1]
    
    return result