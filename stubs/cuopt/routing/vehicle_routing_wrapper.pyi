import _cython_3_1_6
import enum
from cuopt.routing.assignment import Assignment as Assignment
from typing import Any, Callable, ClassVar

Solve: _cython_3_1_6.cython_function_or_method
__reduce_cython__: _cython_3_1_6.cython_function_or_method
__setstate_cython__: _cython_3_1_6.cython_function_or_method
__test__: dict
handle_exception: _cython_3_1_6.cython_function_or_method
type_cast: _cython_3_1_6.cython_function_or_method

class DataModel:
    """DataModel(int num_locations, int fleet_size, int n_orders=-1)"""
    def __init__(self, intnum_locations, intfleet_size, intn_orders=...) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def add_break_dimension(self, break_earliest, break_latest, break_duration) -> Any:
        """DataModel.add_break_dimension(self, break_earliest, break_latest, break_duration)"""
    def add_capacity_dimension(self, name, demand, capacity) -> Any:
        """DataModel.add_capacity_dimension(self, name, demand, capacity)"""
    def add_cost_matrix(self, costs, vehicle_type) -> Any:
        """DataModel.add_cost_matrix(self, costs, vehicle_type)"""
    def add_initial_solutions(self, vehicle_ids, routes, types, sol_offsets) -> Any:
        """DataModel.add_initial_solutions(self, vehicle_ids, routes, types, sol_offsets)"""
    def add_order_precedence(self, node_id, preceding_nodes) -> Any:
        """DataModel.add_order_precedence(self, node_id, preceding_nodes)"""
    def add_order_vehicle_match(self, o_id, vehicles) -> Any:
        """DataModel.add_order_vehicle_match(self, o_id, vehicles)"""
    def add_transit_time_matrix(self, times, vehicle_type) -> Any:
        """DataModel.add_transit_time_matrix(self, times, vehicle_type)"""
    def add_vehicle_break(self, vehicle_id, earliest, latest, duration, locations) -> Any:
        """DataModel.add_vehicle_break(self, vehicle_id, earliest, latest, duration, locations)"""
    def add_vehicle_order_match(self, v_id, orders) -> Any:
        """DataModel.add_vehicle_order_match(self, v_id, orders)"""
    def get_break_dimensions(self) -> Any:
        """DataModel.get_break_dimensions(self)"""
    def get_break_locations(self) -> Any:
        """DataModel.get_break_locations(self)"""
    def get_capacity_dimensions(self) -> Any:
        """DataModel.get_capacity_dimensions(self)"""
    def get_cost_matrix(self, vehicle_type) -> Any:
        """DataModel.get_cost_matrix(self, vehicle_type)"""
    def get_drop_return_trips(self) -> Any:
        """DataModel.get_drop_return_trips(self)"""
    def get_fleet_size(self) -> Any:
        """DataModel.get_fleet_size(self)"""
    def get_initial_solutions(self) -> Any:
        """DataModel.get_initial_solutions(self)"""
    def get_min_vehicles(self) -> Any:
        """DataModel.get_min_vehicles(self)"""
    def get_non_uniform_breaks(self) -> Any:
        """DataModel.get_non_uniform_breaks(self)"""
    def get_num_locations(self) -> Any:
        """DataModel.get_num_locations(self)"""
    def get_num_orders(self) -> Any:
        """DataModel.get_num_orders(self)"""
    def get_objective_function(self) -> Any:
        """DataModel.get_objective_function(self)"""
    def get_order_locations(self) -> Any:
        """DataModel.get_order_locations(self)"""
    def get_order_prizes(self) -> Any:
        """DataModel.get_order_prizes(self)"""
    def get_order_service_times(self, vehicle_id) -> Any:
        """DataModel.get_order_service_times(self, vehicle_id)"""
    def get_order_time_windows(self) -> Any:
        """DataModel.get_order_time_windows(self)"""
    def get_order_vehicle_match(self) -> Any:
        """DataModel.get_order_vehicle_match(self)"""
    def get_pickup_delivery_pairs(self) -> Any:
        """DataModel.get_pickup_delivery_pairs(self)"""
    def get_skip_first_trips(self) -> Any:
        """DataModel.get_skip_first_trips(self)"""
    def get_transit_time_matrices(self) -> Any:
        """DataModel.get_transit_time_matrices(self)"""
    def get_transit_time_matrix(self, vehicle_type) -> Any:
        """DataModel.get_transit_time_matrix(self, vehicle_type)"""
    def get_vehicle_fixed_costs(self) -> Any:
        """DataModel.get_vehicle_fixed_costs(self)"""
    def get_vehicle_locations(self) -> Any:
        """DataModel.get_vehicle_locations(self)"""
    def get_vehicle_max_costs(self) -> Any:
        """DataModel.get_vehicle_max_costs(self)"""
    def get_vehicle_max_times(self) -> Any:
        """DataModel.get_vehicle_max_times(self)"""
    def get_vehicle_order_match(self) -> Any:
        """DataModel.get_vehicle_order_match(self)"""
    def get_vehicle_time_windows(self) -> Any:
        """DataModel.get_vehicle_time_windows(self)"""
    def get_vehicle_types(self) -> Any:
        """DataModel.get_vehicle_types(self)"""
    def set_break_locations(self, break_locations) -> Any:
        """DataModel.set_break_locations(self, break_locations)"""
    def set_drop_return_trips(self, set_drop_return_trips) -> Any:
        """DataModel.set_drop_return_trips(self, set_drop_return_trips)"""
    def set_min_vehicles(self, min_vehicles) -> Any:
        """DataModel.set_min_vehicles(self, min_vehicles)"""
    def set_objective_function(self, objectives, objective_weights) -> Any:
        """DataModel.set_objective_function(self, objectives, objective_weights)"""
    def set_order_locations(self, order_locations) -> Any:
        """DataModel.set_order_locations(self, order_locations)"""
    def set_order_prizes(self, prizes) -> Any:
        """DataModel.set_order_prizes(self, prizes)"""
    def set_order_service_times(self, service_times, vehicle_id=...) -> Any:
        """DataModel.set_order_service_times(self, service_times, vehicle_id=-1)"""
    def set_order_time_windows(self, earliest, latest) -> Any:
        """DataModel.set_order_time_windows(self, earliest, latest)"""
    def set_pickup_delivery_pairs(self, pickup_indices, delivery_indices) -> Any:
        """DataModel.set_pickup_delivery_pairs(self, pickup_indices, delivery_indices)"""
    def set_skip_first_trips(self, set_skip_first_trips) -> Any:
        """DataModel.set_skip_first_trips(self, set_skip_first_trips)"""
    def set_vehicle_fixed_costs(self, vehicle_fixed_costs) -> Any:
        """DataModel.set_vehicle_fixed_costs(self, vehicle_fixed_costs)"""
    def set_vehicle_locations(self, vehicle_start_locations, vehicle_return_locations) -> Any:
        """DataModel.set_vehicle_locations(self, vehicle_start_locations, vehicle_return_locations)"""
    def set_vehicle_max_costs(self, vehicle_max_costs) -> Any:
        """DataModel.set_vehicle_max_costs(self, vehicle_max_costs)"""
    def set_vehicle_max_times(self, vehicle_max_times) -> Any:
        """DataModel.set_vehicle_max_times(self, vehicle_max_times)"""
    def set_vehicle_time_windows(self, vehicle_earliest, vehicle_latest) -> Any:
        """DataModel.set_vehicle_time_windows(self, vehicle_earliest, vehicle_latest)"""
    def set_vehicle_types(self, vehicle_types) -> Any:
        """DataModel.set_vehicle_types(self, vehicle_types)"""
    def __reduce__(self):
        """DataModel.__reduce_cython__(self)"""

class ErrorStatus(enum.IntEnum):
    __new__: ClassVar[Callable] = ...
    OutOfMemoryError: ClassVar[ErrorStatus] = ...
    RuntimeError: ClassVar[ErrorStatus] = ...
    Success: ClassVar[ErrorStatus] = ...
    ValidationError: ClassVar[ErrorStatus] = ...
    _generate_next_value_: ClassVar[Callable] = ...
    _member_map_: ClassVar[dict] = ...
    _member_names_: ClassVar[list] = ...
    _member_type_: ClassVar[type[int]] = ...
    _unhashable_values_: ClassVar[list] = ...
    _unhashable_values_map_: ClassVar[dict] = ...
    _use_args_: ClassVar[bool] = ...
    _value2member_map_: ClassVar[dict] = ...
    def __format__(self, *args, **kwargs) -> str:
        """Convert to a string according to format_spec."""

class NodeType(enum.IntEnum):
    """
    Types for nodes/route returned by the solver

    DEPOT    - Indicates whether a given node is depot
    PICKUP   - Indicates whether a given node corresponds to a pickup
    DELIVERY - Indicates whether a given node corresponds to a delivery
    BREAK    - Indicates whether a given node corresponds to a break
    """
    __new__: ClassVar[Callable] = ...
    BREAK: ClassVar[NodeType] = ...
    DELIVERY: ClassVar[NodeType] = ...
    DEPOT: ClassVar[NodeType] = ...
    PICKUP: ClassVar[NodeType] = ...
    _generate_next_value_: ClassVar[Callable] = ...
    _member_map_: ClassVar[dict] = ...
    _member_names_: ClassVar[list] = ...
    _member_type_: ClassVar[type[int]] = ...
    _unhashable_values_: ClassVar[list] = ...
    _unhashable_values_map_: ClassVar[dict] = ...
    _use_args_: ClassVar[bool] = ...
    _value2member_map_: ClassVar[dict] = ...
    def __format__(self, *args, **kwargs) -> str:
        """Convert to a string according to format_spec."""

class Objective(enum.IntEnum):
    """
    Enums to configure objective of the solution

    COST                - Models with respect to total cost

    TRAVEL_TIME         - Models with respect to travel time (This includes drive, service and wait time) # noqa

    VARIANCE_ROUTE_SIZE - Models with respect to dissimilarity of route sizes

        It computes the L2 variance (squared) in the number of orders served
        by each route.

    VARIANCE_ROUTE_SERVICE_TIME - Models with respect to disssimilarty of route
                                  service times

        It computes L2 variance (squared) of the accumulated service times of
        of each route

    PRIZE               - Models with respect to prizes collected by the
                          serviced orders
    VEHICLE_FIXED_COST                - Models cost per vehicle. Enabled when set_vehicle_fixed_costs is used.
    """
    __new__: ClassVar[Callable] = ...
    COST: ClassVar[Objective] = ...
    PRIZE: ClassVar[Objective] = ...
    TRAVEL_TIME: ClassVar[Objective] = ...
    VARIANCE_ROUTE_SERVICE_TIME: ClassVar[Objective] = ...
    VARIANCE_ROUTE_SIZE: ClassVar[Objective] = ...
    VEHICLE_FIXED_COST: ClassVar[Objective] = ...
    _generate_next_value_: ClassVar[Callable] = ...
    _member_map_: ClassVar[dict] = ...
    _member_names_: ClassVar[list] = ...
    _member_type_: ClassVar[type[int]] = ...
    _unhashable_values_: ClassVar[list] = ...
    _unhashable_values_map_: ClassVar[dict] = ...
    _use_args_: ClassVar[bool] = ...
    _value2member_map_: ClassVar[dict] = ...
    def __format__(self, *args, **kwargs) -> str:
        """Convert to a string according to format_spec."""

class SolverSettings:
    """SolverSettings()"""
    config_file_path: ClassVar[None] = ...
    file_path: ClassVar[None] = ...
    interval: ClassVar[None] = ...
    def __init__(self) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def dump_best_results(self, file_path, interval) -> Any:
        """SolverSettings.dump_best_results(self, file_path, interval)"""
    def dump_config_file(self, file_name) -> Any:
        """SolverSettings.dump_config_file(self, file_name)"""
    def get_best_results_file_path(self) -> Any:
        """SolverSettings.get_best_results_file_path(self)"""
    def get_best_results_interval(self) -> Any:
        """SolverSettings.get_best_results_interval(self)"""
    def get_config_file_name(self) -> Any:
        """SolverSettings.get_config_file_name(self)"""
    def get_time_limit(self) -> Any:
        """SolverSettings.get_time_limit(self)"""
    def set_error_logging_mode(self, boollogging) -> Any:
        """SolverSettings.set_error_logging_mode(self, bool logging)"""
    def set_time_limit(self, seconds) -> Any:
        """SolverSettings.set_time_limit(self, seconds)"""
    def set_verbose_mode(self, boolverbose) -> Any:
        """SolverSettings.set_verbose_mode(self, bool verbose)"""
    def __reduce__(self):
        """SolverSettings.__reduce_cython__(self)"""
