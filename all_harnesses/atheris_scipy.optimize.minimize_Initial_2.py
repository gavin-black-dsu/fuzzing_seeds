import atheris
import numpy as np
from scipy.optimize import minimize
import sys

def fuzz_optimize(data):
    x0 = np.array(data)
    method = 'BFGS'
    
    try:
        res = minimize(lambda x: np.sum(x**2), x0, method=method)
    except Exception as e:
        pass

def main():
    atheris.Setup(sys.argv, fuzz_optimize)
    atheris.Fuzz()

if __name__ == "__main__":
    main()