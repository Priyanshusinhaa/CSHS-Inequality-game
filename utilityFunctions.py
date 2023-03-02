import numpy as np


# utility function
def tensor(arr_list: list[np.ndarray]) -> np.ndarray:
    """
    Repeatedly apply tensor product between arrays from left to right in list

    Args:
        mat_list: list of arrays to multiply

    Returns:
        product of all arrays from left to right

        Example:
        a, b, c = np.array([1, 0]), np.array([1, 0]), np.array([1, 0])
        result = tensor([a, b, c])

        Applies the following operation (a x b) x c, x being the cross product
        result: np.array([1, 0, 0, 0, 0, 0, 0, 0])
    """
    if len(arr_list) < 2:
        raise Exception("Not enough elements in list")
    if len(arr_list) == 2:
        prod = np.kron(arr_list[0], arr_list[1])
        return prod
    else:
        prod = np.kron(arr_list[-2], arr_list[-1])
        new_list = arr_list[:len(arr_list)-2] + [prod]
        return tensor(new_list)