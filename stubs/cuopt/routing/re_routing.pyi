from cuopt.routing import DataModel as DataModel

def construct_rerouting_model(original_model, optimized_route, reroute_from_time, new_order_data, new_distances, print_debug_info: bool = False):
    """
    Creates a new data model for re-routing/re-optimization

    Parameters
    ----------
    original_model:  routing.DataModel object
        the model that used earlier for generating optimized route
    optimized_route: cudf.DataFrame representing the optimized route
        generated with original_model
    reroute_from_time: Float
        time from which the re-routing should start from
    new_order_data: cudf.DataFrame object
        new batch of orders
    new_distances: updated distance/cost matrix
    print_debug_info: option to display debug messages

    Examples
    --------
    >>> original_route = cuopt.Solver(original_model).solve()
    >>> rescheduling_from = 60
    >>> new_order_data = {}
    >>> new_order_data['order_locations'] = [10, 12, 19, 23]
    >>> new_order_data['pickup_indices'] = [0, 1]
    >>> new_order_data['delivery_indices'] = [2, 3]
    >>> new_order_data['earliest_time'] = [65, 75, 90, 85]
    >>> new_order_data['latest_time'] = [75, 80, 95, 95]
    >>> new_order_data['service_time] = [1, 2, 1, 1]
    >>> new_order_data['demand'] = [5, 5, -5, -5]
    >>> rescheduled_model = construct_rerouting_model(
    >>>    original_model, original_route, rescheduling_from,
    >>>    new_order_data, distances)
    >>> rescheduled_route = cuopt.Solver(rescheduled_model).solve()

    Assumptions
    -----------
    1. Re-routing is done from a specified time
    2. Fleet is not changing
    3. Vehicles en route to service a particular order will finish
       that order first
    4. The original optimized plan is going according to the plan, so we can
       determine the finished orders just based on the time
    5. The problem is pickup and delivery only, for now
    6. There is only one capacity demand dimension

    Approach
    --------
    1. Using the optimized route and the time of re-optimization, we figure
       out which orders are fulfilled (picked up and delivered), partially
       fulfilled (picked up but not delivered), and not initiated
    2. We remove the orders that are fulfilled while keeping the orders that
       are not initiated. For the partially fulfilled orders, we create dummy
       pickup orders at vehicle start locations
    """
def generate_capacity_constraints_for_vehicle_order_match(pickup_order_to_vehicle, pickup_indices, delivery_indices, vehicle_num, order_num): ...
