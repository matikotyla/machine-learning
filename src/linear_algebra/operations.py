def add_vectors(v1: list[float], v2: list[float]) -> list[float]:
    """Adds two vectors of the same length."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return [x + y for x, y in zip(v1, v2)]
