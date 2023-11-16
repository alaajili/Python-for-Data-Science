import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values based on height and weight.
    
    Args:
    - height (list): List of integers or floats representing heights.
    - weight (list): List of integers or floats representing weights.
    
    Returns:
    - list: List of BMI values calculated for each corresponding height and weight pair.
    """

    height_arr = np.array(height)
    weight_arr = np.array(weight)
    
    if height_arr.shape != weight_arr.shape:
        raise AssertionError("AssertionError: height and weight arrays must have the same shape")
    
    if height_arr.dtype not in [np.float32, np.float64, np.int64] or weight_arr.dtype not in [np.float32, np.float64, np.int64]:
        raise AssertionError("AssertionError: height and weight arrays must contain only integers or floats")
    
    bmi = weight_arr / (height_arr ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a BMI limit and generate a list of booleans indicating whether each BMI value exceeds the limit.
    
    Args:
    - bmi (list): List of integers or floats representing BMI values.
    - limit (int): Limit value for BMI comparison.
    
    Returns:
    - list: List of booleans indicating whether each BMI value exceeds the specified limit.
    """

    bmi_arr = np.array(bmi)
    if bmi_arr.dtype not in [np.float32, np.float64, np.int64]:
        raise AssertionError("AssertionError: BMI array must contain only integers or floats")
    
    above_limit = bmi_arr > limit
    return above_limit.tolist()
    