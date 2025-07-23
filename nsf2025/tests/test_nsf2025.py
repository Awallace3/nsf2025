"""
Unit and regression test for the nsf2025 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy as np

import nsf2025
from pprint import pprint


def test_nsf2025_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "nsf2025" in sys.modules


def test_compute_angle():
    expected_angle = 90.0
    v = nsf2025.measure.calculate_angle(
        np.array([0, 0, -1]), np.array([0, 0, 0]), np.array([1, 0, 0]), degrees=True
    )
    print(v)
    assert np.abs(v - expected_angle) < 1e-8, "Angle calculation failed"


def test_build_bond_list():
    ref_bond_list = {
        (0, 1): np.float64(1.4),
        (0, 2): np.float64(1.4),
        (0, 3): np.float64(1.4),
        (0, 4): np.float64(1.4),
    }

    coordinates = np.array(
        [
            [1, 1, 1],
            [2.4, 1, 1],
            [-0.4, 1, 1],
            [1, 1, 2.4],
            [1, 1, -0.4],
        ]
    )
    bond_list = nsf2025.molecule.build_bond_list(coordinates, max_bond=1.5, min_bond=0)
    assert len(bond_list) == 4
    for key in ref_bond_list:
        assert key in bond_list, f"Bond {key} not found in bond list"
        assert np.abs(bond_list[key] - ref_bond_list[key]) < 1e-8, f"Bond {
            key
        } has incorrect distance: {bond_list[key]} != {ref_bond_list[key]}"


def test_build_bond_list_failure():
    ref_bond_list = {
        (0, 1): np.float64(1.4),
        (0, 2): np.float64(1.4),
        (0, 3): np.float64(1.4),
        (0, 4): np.float64(1.4),
    }

    coordinates = np.array(
        [
            [1, 1, 1],
            [2.4, 1, 1],
            [-0.4, 1, 1],
            [1, 1, 2.4],
            [1, 1, -0.4],
        ]
    )
    with pytest.raises(ValueError):
        # Test with invalid min_bond
        _ = nsf2025.molecule.build_bond_list(coordinates, max_bond=1.5, min_bond=-1)


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
@pytest.mark.xfail(raises=ValueError)
def test_build_bond_list_failure2():
    coordinates = np.array(
        [
            [1, 1, 1],
            [2.4, 1, 1],
            [-0.4, 1, 1],
            [1, 1, 2.4],
            [1, 1, -0.4],
        ]
    )
    with pytest.raises(ValueError):
        # Test with invalid min_bond
        _ = nsf2025.molecule.build_bond_list(coordinates, max_bond=1.5, min_bond=-1)


test_build_bond_list_failure()
