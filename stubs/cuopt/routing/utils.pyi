from _typeshed import Incomplete
from cuopt import routing as routing
from cuopt.routing import utils_wrapper as utils_wrapper

def generate_dataset(locations: int = 100, asymmetric: bool = True, min_demand=..., max_demand=..., min_capacities=..., max_capacities=..., min_service_time: int = 0, max_service_time: int = 0, tw_tightness: float = 0.0, drop_return_trips: float = 0.0, shifts: int = 1, n_vehicle_types: int = 1, n_matrix_types: int = 1, distribution=..., center_box=None, seed: int = 0):
    """
    Constructs a dataset from the given parameters.
    locations:

    Parameters
    ----------
    locations: int32
        Number of locations to visit, including the depot.

    asymmetric : bool
        Specifies if the matrices (both cost and time)
        should be asymmetric.

    min_demand : cudf.Series
        Series will be cast to int32.
        Minimum demand value along each dimension.

    max_demand : cudf.Series
        Series will be cast to int32.
        Maximum demand value along each dimension.

    min_capacities : cudf.Series
        Series will be cast to int32.
        Minimum capacity value along each dimension.

    max_capacities : cudf.Series
        Series will be cast to int32.
        Maximum capacity value along each dimension.

    min_service_time : int32
        Lower bound for generated service time.

    max_service_time : int32
        Upper bound for generated service time.

    tw_tightness : float32
        Can make a problem more or less difficult to solve.
        Feasibility is ensured because we made sure the latest time of
        a node is larger than its depot-node distance.

    drop_return_trips : float32
        Percentage of vehicles in the fleet that shouldn't return to the depot.

    shifts : int32
        The number of shifts in the dataset. This will create vehicle
        time windows that split the fleet into multiple shifts.

    n_vehicle_types : int32
        Multiple vehicle types can be generated each with a corresponding
        cost matrix or time matrix.

    n_matrix_types : int32
        There can be one cost and time matrix per vehicle type.
        The cupy array generated is of size dim4(n_vehicle_types,
        n_matrix_types, nloc, nloc). In the case the n_matrix_types is 1,
        the cost matrix is used for time.

    distribution : DatasetDistribution
        The distribution of datapoints similar to what is done for the
        homberger cvrptw dataset.
        https://www.sintef.no/projectweb/top/vrptw/homberger-benchmark/
        Clustered datasets are usually faster to generate and solve.

    center_box : tuple
        The bounding box which constrains all the centroids.

    seed : int32
        Random seed for the raft generator.

    Returns
    -------
    pos_list : cudf.DataFrame
        x and y coordinates.
    matrices : cupy.ndarray
        Vehicle cost and time matrices as
        dim4(n_vehicle_types, n_matrix_types, nloc, nloc).
    orders : cudf.DataFrame
        Time windows and multi dimension demand for each location.
    vehicles : cudf.DataFrame
        Time windows and multi dimension
        capacity for each vehicle.
    """
def update_routes_and_vehicles(output_df, route, order_pdf, order_data, vehicle_constraints):
    """
    Helper function to update the final routes and vehicle time windows
    when running cuopt in batches.
    Routes are updated in output_df and vehicle time windows are
    updated in vehicle_constraints.
    """
def add_vehicle_constraints(num_vehicles, vehicle_capacity, break_earliest=None, break_latest=None, vehicle_speed: int = 1):
    """
    Helper function to add vehicle constraints when running
    cuopt in batches. Vehicle constraints that can be added
    include number of vehicles, vehicle capacity, speed of vehicles
    and earliest and latest vehicle break times.
    """
def create_pickup_delivery_data(matrix_pdf, raw_order_pdf, depot, vehicle_constraints):
    """
    Creates and returns travel matrix, order information
    and vehicle information for pickup and deliveries.
    """
def create_data_model(filename, num_vehicles=None, run_nodes=None):
    """
    Construct a data model with reduced number of vehicles and/or
    nodes from a standard Homberger and Li&Lim dataset

    This function is used mainly to create smaller tests for testing
    API functionalities

    Parameters
    ----------
    filename :  filename corresponding to the test in benchmark format
    num_vehicles: number of vehicles to be used in a modified test.
        If it is defaulted the number of vehicles is not modified
    run_nodes:  number of nodes to consider in a modified test.
        If it is defaulted the number of nodes/tasks is not modified
    """
def create_data_model_from_yaml(file_path): ...
def write_yaml_dict_if_not_empty(yamldict, keyname, data) -> None: ...
def save_data_model_to_yaml(data_model, solver_settings, solution, fname) -> None:
    """
    Writes Solver.DataModel object in yaml format in a given file name

    Parameters
    ----------
    solver_settings : Solver object that contains the data model information
    solution: Solution object that contains routing information
    fname      : file name with yaml extension used for the output
    """

RAPIDS_DATASET_ROOT_DIR: Incomplete
SOLOMON_PATH: Incomplete
REF_PATH: Incomplete
DATASETS_SOLOMON: Incomplete

def read_ref_tsp(file, test_type): ...
def read_ref(file, test_type, nodes): ...
def create_from_file_tsp(file_path): ...
def create_from_file(file_path, is_pdp: bool = False): ...
def create_from_yaml_file(file_path): ...
def euclidean_distance(coord): ...
def build_matrix(df): ...
def fill_demand(df, data_model, vehicle_capacity, n_vehicles, use_order_loc: bool = False) -> None: ...
def get_time_limit(nodes): ...
def set_limits(solver_settings, nodes) -> None: ...
def set_limits_for_quality(solver_settings, nodes) -> None: ...
def fill_tw(data_model, df, use_order_loc: bool = False) -> None: ...
def fill_pdp_index(data_model, df, use_order_loc: bool = False) -> None: ...
def create_from_solomon_inp_file(file_path): ...
def convert_solomon_inp_file_to_yaml(file_nm) -> None: ...
def create_model_dictionary_from_file(filename, is_pdp: bool = False):
    """
    Creates a dictionary (json compatible) of the model by reading
    a standard Homberber or Li&Lim test. This dictionary is eventually
    used in testing the SDK or service
    """
