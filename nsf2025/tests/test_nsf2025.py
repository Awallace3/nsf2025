"""
Unit and regression test for the nsf2025 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import nsf2025


def test_nsf2025_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "nsf2025" in sys.modules
