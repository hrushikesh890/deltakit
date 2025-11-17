# (c) Copyright Riverlane 2020-2025.
"""
This module implements a Steane code for quantum memory and stability experiments.
"""

from typing import Callable, List, Set, Tuple

from deltakit_circuit import PauliX, PauliZ, Qubit
from deltakit_circuit._basic_maps import BASIS_TO_PAULI
from deltakit_circuit._basic_types import Coord2D, Coord2DDelta
from deltakit_circuit._qubit_identifiers import PauliGate
from deltakit_circuit.gates import PauliBasis
from deltakit_explorer.codes._css._css_code import CSSCode
from deltakit_explorer.codes._stabiliser import Stabiliser