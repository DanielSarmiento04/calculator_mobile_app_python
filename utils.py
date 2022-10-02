import numpy as np

first_row = np.array(['AC',"+/-","%","/"], dtype=object)
second_row = np.array(['7','8','9','x'], dtype=object)
third_row = np.array(['4','5','6','-'], dtype=object)
fourth_row = np.array(['1','2','3','+'], dtype=object)
fifth_row = np.array(['0','.','='], dtype=object)
operaction_symbols = np.array(['+','-','x','/'], dtype=object)

def get_zero() -> str:
   """ Return the zero """
   return fifth_row[0]

def get_grid() -> np.array:
    """Return a 5x4 grid of buttons of calculator"""
    return np.array([first_row, second_row, third_row, fourth_row, fifth_row])

def is_number(value) -> bool:
    """Return True if value is a number"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_operation_symbol(value) -> bool:
    """Return the operation symbol"""
    if value in operaction_symbols:
        return True
    else:
        return False