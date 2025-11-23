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

class SteaneCode(CSSCode):

    def __init__(self, distance: int, stabiliser_type: PauliBasis = PauliBasis.Z, use_ancilla_qubits: bool = True, use_looping_stabiliser: bool = False, default_schedule: bool = True, odd_data_qubit_coords: bool = False):
        self.distance = distance
        self.stabiliser_type = stabiliser_type
        self.use_ancilla_qubits = use_ancilla_qubits
        self.use_looping_stabiliser = use_looping_stabiliser
        self.default_schedule = default_schedule
        self.odd_data_qubit_coords = odd_data_qubit_coords

        super().__init__(use_ancilla_qubits=use_ancilla_qubits, use_looping_stabiliser=use_looping_stabiliser, default_schedule=default_schedule, odd_data_qubit_coords=odd_data_qubit_coords)

    def _calculate_data_qubits(self) -> Set[Qubit]: