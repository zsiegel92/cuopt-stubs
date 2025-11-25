import _cython_3_1_6
from typing import Any

__reduce_cython__: _cython_3_1_6.cython_function_or_method
__setstate_cython__: _cython_3_1_6.cython_function_or_method
__test__: dict

class WaypointMatrix:
    """WaypointMatrix(offsets, indices, weights)"""
    def __init__(self, offsets, indices, weights) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def compute_cost_matrix(self, target_locations) -> Any:
        """WaypointMatrix.compute_cost_matrix(self, target_locations)"""
    def compute_shortest_path_costs(self, target_locations, weights) -> Any:
        """WaypointMatrix.compute_shortest_path_costs(self, target_locations, weights)"""
    def compute_waypoint_sequence(self, target_locations, route_df) -> Any:
        """WaypointMatrix.compute_waypoint_sequence(self, target_locations, route_df)"""
    def __reduce__(self):
        """WaypointMatrix.__reduce_cython__(self)"""
