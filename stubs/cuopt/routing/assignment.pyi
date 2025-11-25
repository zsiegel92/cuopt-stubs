from _typeshed import Incomplete
from cuopt.utilities import catch_cuopt_exception as catch_cuopt_exception
from enum import Enum

class SolutionStatus(Enum):
    SUCCESS = 0
    FAIL = 1
    TIMEOUT = 2
    EMPTY = 3

class Assignment:
    """
    A container of vehicle routing solver output

    Parameters
    ----------
    vehicle_count : Integer
        Number of vehicles in the solution
    total_objective_value : Float64
        Objective value calculated as per objective functions and weights
    objective_values : dict[Objective, Float64]
    route_df: cudf.DataFrame
        Contains route, vehicle_id, arrival_stamp.
    accepted: cudf.Series
    status: Integer
        Solver status 0 - SUCCESS, 1 - FAIL, 2 - TIMEOUT and 3 - EMPTY.
    message: String
        Any error message if there is failure
    undeliverable_orders: cudf.Series
        Orders which can not be served
    """
    vehicle_count: Incomplete
    total_objective_value: Incomplete
    objective_values: Incomplete
    route: Incomplete
    accepted: Incomplete
    status: Incomplete
    message: Incomplete
    error_status: Incomplete
    error_message: Incomplete
    undeliverable_orders: Incomplete
    @catch_cuopt_exception
    def __init__(self, vehicle_count, total_objective_value, objective_values, route_df, accepted, status, message, error_status, error_message, undeliverable_orders) -> None: ...
    @catch_cuopt_exception
    def get_vehicle_count(self):
        """
        Returns the number of vehicle needed for this routing assignment.
        """
    @catch_cuopt_exception
    def get_total_objective(self):
        """
        Returns the objective value calculated based on the user
        provided objective function and the routes found by the solver.
        """
    @catch_cuopt_exception
    def get_objective_values(self):
        """
        Returns the individual objective_values as dictionary
        """
    @catch_cuopt_exception
    def get_route(self):
        """
        Returns the route, truck ids for each stop and the arrival stamp
        as cudf.DataFrame.

        Examples
        --------
        >>> import cuopt
        >>> import cudf
        >>> locations = [0, 1, 2, 3]
        >>> vehicles  = [0, 1]
        >>> cost_mat  = [
        ...   [0, 1, 5, 2],
        ...   [2, 0, 7, 4],
        ...   [1, 5, 0, 9],
        ...   [5, 6, 2, 0]
        ... ]
        >>> cost_mat = cudf.DataFrame(cost_mat)
        >>> cost_mat
           0  1  2  3
        0  0  1  5  2
        1  2  0  7  4
        2  1  5  0  9
        3  5  6  2  0
        >>> data_model = routing.DataModel(len(locations), len(vehicles))
        >>> data_model.set_matrix(cost_mat)
        >>> solver = cuopt.Solver(data_model)
        >>> solver.set_min_vehicles(len(vehicles))
        >>> solver.set_min_vehicles(len(vehicles))
        >>> solution = solver.solve()
        >>> solution.get_route()
        >>> solution.get_route()
           route  arrival_stamp  truck_id  location
        0      0            0.0         1         0
        1      3            2.0         1         3
        2      2            4.0         1         2
        3      0            5.0         1         0
        4      0            0.0         0         0
        5      1            1.0         0         1
        6      0            3.0         0         0
        """
    @catch_cuopt_exception
    def get_status(self):
        """
        Returns the final solver status as per SolutionStatus.
        """
    @catch_cuopt_exception
    def get_message(self):
        """
        Returns the final solver message as per SolutionStatus.
        """
    @catch_cuopt_exception
    def get_error_status(self):
        """
        Returns the error status as per ErrorStatus.
        """
    @catch_cuopt_exception
    def get_error_message(self):
        """
        Returns the error message as per ErrorMessage.
        """
    @catch_cuopt_exception
    def get_infeasible_orders(self):
        """
        Returns the infeasible order numbers as cudf.Series.
        """
    @catch_cuopt_exception
    def get_accepted_solutions(self):
        """ """
    @catch_cuopt_exception
    def display_routes(self) -> None:
        """
        Display the solution in human readable format.
        Intended for relatively small inputs.

        Examples
        --------
        >>> import cuopt
        >>> import cudf
        >>> locations = [0, 1, 2, 3]
        >>> vehicles  = [0, 1]
        >>> cost_mat  = [
        ...   [0, 1, 5, 2],
        ...   [2, 0, 7, 4],
        ...   [1, 5, 0, 9],
        ...   [5, 6, 2, 0]
        ... ]
        >>> cost_mat = cudf.DataFrame(cost_mat)
        >>> cost_mat
           0  1  2  3
        0  0  1  5  2
        1  2  0  7  4
        2  1  5  0  9
        3  5  6  2  0
        >>> data_model = routing.DataModel(len(locations), len(vehicles))
        >>> data_model.set_matrix(cost_mat)
        >>> solver = cuopt.Solver(data_model)
        >>> solver.set_min_vehicles(len(vehicles))
        >>> solver.set_min_vehicles(len(vehicles))
        >>> solution = solver.solve()
        >>> solution.display_routes()
        Vehicle-0 starts at: 0.0, completes at: 3.0, travel time: 3.0,  Route :
        0->1->0
        Vehicle-1 starts at: 0.0, completes at: 5.0, travel time: 5.0,  Route :
        0->3->2->0
        This results in a travel time of 8.0 to deliver all routes
        """
