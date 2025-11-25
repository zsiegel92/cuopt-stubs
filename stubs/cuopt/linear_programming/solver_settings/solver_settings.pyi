from _typeshed import Incomplete
from cuopt.linear_programming.solver.solver_parameters import CUOPT_ABSOLUTE_DUAL_TOLERANCE as CUOPT_ABSOLUTE_DUAL_TOLERANCE, CUOPT_ABSOLUTE_GAP_TOLERANCE as CUOPT_ABSOLUTE_GAP_TOLERANCE, CUOPT_ABSOLUTE_PRIMAL_TOLERANCE as CUOPT_ABSOLUTE_PRIMAL_TOLERANCE, CUOPT_AUGMENTED as CUOPT_AUGMENTED, CUOPT_BARRIER_DUAL_INITIAL_POINT as CUOPT_BARRIER_DUAL_INITIAL_POINT, CUOPT_CROSSOVER as CUOPT_CROSSOVER, CUOPT_CUDSS_DETERMINISTIC as CUOPT_CUDSS_DETERMINISTIC, CUOPT_DUALIZE as CUOPT_DUALIZE, CUOPT_DUAL_INFEASIBLE_TOLERANCE as CUOPT_DUAL_INFEASIBLE_TOLERANCE, CUOPT_DUAL_POSTSOLVE as CUOPT_DUAL_POSTSOLVE, CUOPT_ELIMINATE_DENSE_COLUMNS as CUOPT_ELIMINATE_DENSE_COLUMNS, CUOPT_FIRST_PRIMAL_FEASIBLE as CUOPT_FIRST_PRIMAL_FEASIBLE, CUOPT_FOLDING as CUOPT_FOLDING, CUOPT_INFEASIBILITY_DETECTION as CUOPT_INFEASIBILITY_DETECTION, CUOPT_ITERATION_LIMIT as CUOPT_ITERATION_LIMIT, CUOPT_LOG_FILE as CUOPT_LOG_FILE, CUOPT_LOG_TO_CONSOLE as CUOPT_LOG_TO_CONSOLE, CUOPT_METHOD as CUOPT_METHOD, CUOPT_MIP_ABSOLUTE_GAP as CUOPT_MIP_ABSOLUTE_GAP, CUOPT_MIP_ABSOLUTE_TOLERANCE as CUOPT_MIP_ABSOLUTE_TOLERANCE, CUOPT_MIP_HEURISTICS_ONLY as CUOPT_MIP_HEURISTICS_ONLY, CUOPT_MIP_INTEGRALITY_TOLERANCE as CUOPT_MIP_INTEGRALITY_TOLERANCE, CUOPT_MIP_RELATIVE_GAP as CUOPT_MIP_RELATIVE_GAP, CUOPT_MIP_RELATIVE_TOLERANCE as CUOPT_MIP_RELATIVE_TOLERANCE, CUOPT_MIP_SCALING as CUOPT_MIP_SCALING, CUOPT_NUM_CPU_THREADS as CUOPT_NUM_CPU_THREADS, CUOPT_ORDERING as CUOPT_ORDERING, CUOPT_PDLP_SOLVER_MODE as CUOPT_PDLP_SOLVER_MODE, CUOPT_PER_CONSTRAINT_RESIDUAL as CUOPT_PER_CONSTRAINT_RESIDUAL, CUOPT_PRESOLVE as CUOPT_PRESOLVE, CUOPT_PRIMAL_INFEASIBLE_TOLERANCE as CUOPT_PRIMAL_INFEASIBLE_TOLERANCE, CUOPT_RELATIVE_DUAL_TOLERANCE as CUOPT_RELATIVE_DUAL_TOLERANCE, CUOPT_RELATIVE_GAP_TOLERANCE as CUOPT_RELATIVE_GAP_TOLERANCE, CUOPT_RELATIVE_PRIMAL_TOLERANCE as CUOPT_RELATIVE_PRIMAL_TOLERANCE, CUOPT_SAVE_BEST_PRIMAL_SO_FAR as CUOPT_SAVE_BEST_PRIMAL_SO_FAR, CUOPT_SOLUTION_FILE as CUOPT_SOLUTION_FILE, CUOPT_STRICT_INFEASIBILITY as CUOPT_STRICT_INFEASIBILITY, CUOPT_TIME_LIMIT as CUOPT_TIME_LIMIT, CUOPT_USER_PROBLEM_FILE as CUOPT_USER_PROBLEM_FILE, get_solver_setting as get_solver_setting
from enum import IntEnum

class SolverMethod(IntEnum):
    """
    Enum representing different methods to use for solving linear programs.
    """
    Concurrent = 0
    PDLP = ...
    DualSimplex = ...
    Barrier = ...

class PDLPSolverMode(IntEnum):
    """
    Enum representing different solver modes to use in the
    `SolverSettings.set_pdlp_solver_mode` function.

    Attributes
    ----------
    Stable3
        Best overall mode from experiments; balances speed and convergence
        success. If you want to use the legacy version, use Stable1.
    Methodical1
        Takes slower individual steps, but fewer are needed to converge.
    Fast1
        Fastest mode, but with less success in convergence.

    Notes
    -----
    Default mode is Stable3.
    """
    Stable1 = 0
    Stable2 = ...
    Methodical1 = ...
    Fast1 = ...
    Stable3 = ...

class SolverSettings:
    settings_dict: Incomplete
    pdlp_warm_start_data: Incomplete
    mip_callbacks: Incomplete
    def __init__(self) -> None: ...
    def to_base_type(self, value):
        """Convert a string to a base type.

        Parameters
        ----------
        value : str
            The value to convert.

        Returns
        -------
        value : float, int, bool, or str
            The converted value.
        """
    def get_parameter(self, name):
        """Get the value of a parameter used by cuOpt's LP/MIP solvers.

        Parameters
        ----------
        name : str
            The name of the parameter to get.

        Returns
        -------
        value : float, int, bool, or str
            The value of the parameter.

        Notes
        -----
        For a list of availabe parameters, their descriptions, default values,
        and acceptable ranges, see the cuOpt documentation `parameter.rst`.
        """
    def set_parameter(self, name, value) -> None:
        """Set the value of a parameter used by cuOpt's LP/MIP solvers.

        Parameters
        ----------
        name : str
            The name of the parameter to set.
        value : str
            The value the parameter should take.

        For a list of availabe parameters, their descriptions, default values,
        and acceptable ranges, see the cuOpt documentation `parameter.rst`.
        """
    def set_optimality_tolerance(self, eps_optimal) -> None:
        """
        NOTE: Not supported for MILP, absolute is fixed to 1e-4,

        Set both absolute and relative tolerance on the primal feasibility,
        dual feasibility, and gap.
        Changing this value has a significant impact on accuracy and runtime.

        Optimality is computed as follows:

        dual_feasibility < absolute_dual_tolerance + relative_dual_tolerance
          * norm_objective_coefficient (l2_norm(c))
        primal_feasibility < absolute_primal_tolerance
          + relative_primal_tolerance * norm_constraint_bounds (l2_norm(b))
        duality_gap < absolute_gap_tolerance + relative_gap_tolerance
          * (abs(primal_objective) + abs(dual_objective))

        If all three conditions hold, optimality is reached.

        Parameters
        ----------
        eps_optimal : float64
            Tolerance to optimality

        Notes
        -----
        Default value is 1e-4.
        To set each absolute and relative tolerance, use the provided setters.
        """
    def set_pdlp_warm_start_data(self, pdlp_warm_start_data) -> None:
        """
        Set the pdlp warm start data. This allows to restart PDLP with a
        previous solution context.

        This should be used when you solve a new problem which is similar to
        the previous one.

        Parameters
        ----------
        pdlp_warm_start_data : PDLPWarmStartData
            PDLP warm start data obtained from a previous solve.
            Refer :py:meth:`cuopt.linear_programming.problem.Problem.get_pdlp_warm_start_data`  # noqa

        Notes
        -----
        For now, the problem must have the same number of variables and
        constraints as the one found in the previous solution.

        Only supported solver modes are Stable2 and Fast1.

        Examples
        --------
        >>> settings.set_pdlp_warm_start_data(pdlp_warm_start_data)
        """
    def set_mip_callback(self, callback) -> None:
        '''
        Note: Only supported for MILP

        Set the callback to receive incumbent solution.

        Parameters
        ----------
        callback : class for function callback
            Callback class that inherits from GetSolutionCallback
            or SetSolutionCallback.

        Examples
        --------
        >>> # Callback for incumbent solution
        >>> class CustomGetSolutionCallback(GetSolutionCallback):
        >>>     def __init__(self):
        >>>         super().__init__()
        >>>         self.n_callbacks = 0
        >>>         self.solutions = []
        >>>
        >>>     def get_solution(self, solution, solution_cost):
        >>>         self.n_callbacks += 1
        >>>         assert len(solution) > 0
        >>>         assert len(solution_cost) == 1
        >>>
        >>>         self.solutions.append(
        >>>             {
        >>>                 "solution": solution.copy_to_host(),
        >>>                 "cost": solution_cost.copy_to_host()[0],
        >>>             }
        >>>         )
        >>>
        >>> class CustomSetSolutionCallback(SetSolutionCallback):
        >>>     def __init__(self, get_callback):
        >>>         super().__init__()
        >>>         self.n_callbacks = 0
        >>>         self.get_callback = get_callback
        >>>
        >>>     def set_solution(self, solution, solution_cost):
        >>>         self.n_callbacks += 1
        >>>         if self.get_callback.solutions:
        >>>             solution[:] =
        >>>             self.get_callback.solutions[-1]["solution"]
        >>>             solution_cost[0] = float(
        >>>                 self.get_callback.solutions[-1]["cost"]
        >>>             )
        >>>
        >>> get_callback = CustomGetSolutionCallback()
        >>> set_callback = CustomSetSolutionCallback(get_callback)
        >>> settings.set_mip_callback(get_callback)
        >>> settings.set_mip_callback(set_callback)
        '''
    def get_mip_callbacks(self):
        """
        Return callback class object
        """
    def get_pdlp_warm_start_data(self):
        """
        Returns the warm start data. See `set_pdlp_warm_start_data` for more
        details.

        Returns
        -------
        pdlp_warm_start_data:

        """
    def toDict(self): ...
