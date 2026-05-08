import numpy as np


def main() -> None:
    a: np.ndarray = np.array([1, 2, 3])
    b: np.ndarray = np.array([4, 5, 6])
    c: np.ndarray = a + b

    print(c)


if __name__ == "__main__":
    main()
