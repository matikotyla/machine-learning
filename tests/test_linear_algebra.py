import pytest
from linear_algebra.operations import add_vectors


def test_add_vectors_success() -> None:
    # Test basic addition
    assert add_vectors([1.0, 2.0], [3.0, 4.0]) == [4.0, 6.0]


def test_add_vectors_mismatch() -> None:
    # Test that it raises an error for different lengths
    with pytest.raises(ValueError, match="Vectors must be the same length"):
        add_vectors([1.0], [1.0, 2.0])
