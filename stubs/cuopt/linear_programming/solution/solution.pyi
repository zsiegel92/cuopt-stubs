from _typeshed import Incomplete
from cuopt.linear_programming.solver.solver_wrapper import LPTerminationStatus as LPTerminationStatus, MILPTerminationStatus as MILPTerminationStatus, ProblemCategory as ProblemCategory

class PDLPWarmStartData:
    current_primal_solution: Incomplete
    current_dual_solution: Incomplete
    initial_primal_average: Incomplete
    initial_dual_average: Incomplete
    current_ATY: Incomplete
    sum_primal_solutions: Incomplete
    sum_dual_solutions: Incomplete
    last_restart_duality_gap_primal_solution: Incomplete
    last_restart_duality_gap_dual_solution: Incomplete
    initial_primal_weight: Incomplete
    initial_step_size: Incomplete
    total_pdlp_iterations: Incomplete
    total_pdhg_iterations: Incomplete
    last_candidate_kkt_score: Incomplete
    last_restart_kkt_score: Incomplete
    sum_solution_weight: Incomplete
    iterations_since_last_restart: Incomplete
    def __init__(self, current_primal_solution, current_dual_solution, initial_primal_average, initial_dual_average, current_ATY, sum_primal_solutions, sum_dual_solutions, last_restart_duality_gap_primal_solution, last_restart_duality_gap_dual_solution, initial_primal_weight, initial_step_size, total_pdlp_iterations, total_pdhg_iterations, last_candidate_kkt_score, last_restart_kkt_score, sum_solution_weight, iterations_since_last_restart) -> None: ...

class Solution:
    """
    A container of LP solver output

    Parameters
    ----------
    problem_category : int
        Whether it is a LP-0, MIP-1 or IP-2 solution
    vars : Dict[str, float64]
        Dictionary mapping each variable (name) to its value.
    primal_solution : numpy.array
        Primal solution of the LP problem
    dual_solution : numpy.array
        Note: Applicable to only LP
        Dual solution of the LP problem
    reduced_cost : numpy.array
        Note: Applicable to only LP
        The reduced cost.
        It contains the dual multipliers for the linear constraints.
    termination_status: Integer
        Termination status value.
    primal_residual: Float64
        L2 norm of the primal residual: measurement of the primal infeasibility
    dual_residual: Float64
        Note: Applicable to only LP
        L2 norm of the dual residual: measurement of the dual infeasibility
    primal_objective: Float64
        Value of the primal objective
    dual_objective: Float64
        Note: Applicable to only LP
        Value of the dual objective
    gap: Float64
        Difference between the primal and dual objective
    nb_iterations: Int
        Number of iterations the LP solver did before converging
    mip_gap: float64
        Note: Applicable to only MILP
        The relative difference between the best integer objective value
        found so far and the objective bound. A value of 0.01 means the
        solution is guaranteed to be within 1% of optimal.
    solution_bound: float64
        Note: Applicable to only MILP
        The best known bound on the optimal objective value.
        For minimization problems, this is a lower bound on the optimal value.
        For maximization problems, this is an upper bound.
    max_constraint_violation: float64
        Note: Applicable to only MILP
        The maximum amount by which any constraint is violated in
        the current solution. Should be close to zero for a feasible solution.
    max_int_violation: float64
        Note: Applicable to only MILP
        The maximum amount by which any integer variable deviates from being
        an integer. A value of 0 means all integer variables have
        integral values.
    max_variable_bound_violation: float64
        Note: Applicable to only MILP
        The maximum amount by which any variable violates its upper or
        lower bounds in the current solution. Should be zero for a
        feasible solution.
    presolve_time: float64
        Note: Applicable to only MILP
        Time used for pre-solve
    solve_time: Float64
        Solve time in seconds
    solved_by_pdlp: bool
        Whether the problem was solved by PDLP or Dual Simplex
    """
    problem_category: Incomplete
    primal_solution: Incomplete
    dual_solution: Incomplete
    pdlp_warm_start_data: Incomplete
    error_status: Incomplete
    error_message: Incomplete
    primal_objective: Incomplete
    dual_objective: Incomplete
    solve_time: Incomplete
    solved_by_pdlp: Incomplete
    vars: Incomplete
    lp_stats: Incomplete
    reduced_cost: Incomplete
    milp_stats: Incomplete
    def __init__(self, problem_category, vars, solve_time: float = 0.0, primal_solution=None, dual_solution=None, reduced_cost=None, current_primal_solution=None, current_dual_solution=None, initial_primal_average=None, initial_dual_average=None, current_ATY=None, sum_primal_solutions=None, sum_dual_solutions=None, last_restart_duality_gap_primal_solution=None, last_restart_duality_gap_dual_solution=None, initial_primal_weight: float = 0.0, initial_step_size: float = 0.0, total_pdlp_iterations: int = 0, total_pdhg_iterations: int = 0, last_candidate_kkt_score: float = 0.0, last_restart_kkt_score: float = 0.0, sum_solution_weight: float = 0.0, iterations_since_last_restart: int = 0, termination_status: int = 0, error_status: int = 0, error_message: str = '', primal_residual: float = 0.0, dual_residual: float = 0.0, primal_objective: float = 0.0, dual_objective: float = 0.0, gap: float = 0.0, nb_iterations: int = 0, solved_by_pdlp=None, mip_gap: float = 0.0, solution_bound: float = 0.0, presolve_time: float = 0.0, max_constraint_violation: float = 0.0, max_int_violation: float = 0.0, max_variable_bound_violation: float = 0.0, num_nodes: int = 0, num_simplex_iterations: int = 0) -> None: ...
    def raise_if_milp_solution(self, function_name) -> None: ...
    def raise_if_lp_solution(self, function_name) -> None: ...
    def get_primal_solution(self):
        """
        Returns the primal solution as numpy.array with float64 type.
        """
    def get_dual_solution(self):
        """
        Note: Applicable to only LP
        Returns the dual solution as numpy.array with float64 type.
        """
    def get_primal_objective(self):
        """
        Returns the primal objective as a float64.
        """
    def get_dual_objective(self):
        """
        Note: Applicable to only LP
        Returns the dual objective as a float64.
        """
    def get_termination_status(self):
        """
        Returns the termination status as per TerminationReason.
        """
    def get_termination_reason(self):
        """
        Returns the termination reason as per TerminationReason.
        """
    def get_error_status(self):
        """
        Returns the error status as per ErrorStatus.
        """
    def get_error_message(self):
        """
        Returns the error message as per ErrorMessage.
        """
    def get_solve_time(self):
        """
        Returns the engine solve time in seconds as a float64.
        """
    def get_solved_by_pdlp(self):
        """
        Returns whether the problem was solved by PDLP or Dual Simplex
        """
    def get_vars(self):
        """
        Returns the dictionnary mapping each variable (name) to its value.
        """
    def get_lp_stats(self):
        '''
        Note: Applicable to only LP
        Returns the convergence statistics as a dictionary:

        "primal_residual": float64
          Measurement of the primal infeasibility.
          This quantity is being reduced until primal tolerance is met
          (see SolverSettings primal_tolerance).

        "dual_residual": float64,
          Measurement of the dual infeasibility.
          This quantity is being reduced until dual tolerance is met
          (see SolverSettings dual_tolerance).

        "gap": float64
          Difference between the primal and dual objective.
          This quantity is being reduced until gap tolerance is met
          (see SolverSettings gap_tolerance).

        - "nb_iterations": int
            Number of iterations the LP solver did before converging.
        '''
    def get_reduced_cost(self):
        """
        Returns the reduced cost as numpy.array with float64 type.
        """
    def get_pdlp_warm_start_data(self):
        """
        Note: Applicable to only LP

        Allows to retrieve the warm start data from the PDLP solver.

        See `SolverSettings.set_pdlp_warm_start_data` for more details.
        """
    def get_milp_stats(self):
        """
        Note: Applicable to only MILP
        Returns the convergence statistics as a dictionary:

        mip_gap: float64
            The relative difference between the best integer objective value
            found so far and the objective bound. A value of 0.01 means the
            solution is guaranteed to be within 1% of optimal.

        presolve_time: float64
            Time took for pre-solve

        max_constraint_violation: float64
            The maximum amount by which any constraint is violated
            in the current solution.
            Should be close to zero for a feasible solution
            .
        max_int_violation: float64
            The maximum amount by which any integer variable deviates
            from being an integer. A value of 0 means all integer variables
            have integral values.

        max_variable_bound_violation: float64
            The maximum amount by which any variable violates
            its upper or lower bounds in the current solution.
            Should be zero for a feasible solution.

        solution_bound: float64
            The best known bound on the optimal objective value.
            For minimization problems, this is a lower bound on the optimal
            value.
            For maximization problems, this is an upper bound.

        num_nodes: int
            Number of nodes explored during the MIP solve

        num_simplex_iterations: int
            Number of simplex iterations performed during the MIP solve
        """
    def get_problem_category(self):
        """
        Returns one of the problem category from ProblemCategory

        LP  - 0
        MIP - 1
        IP  - 2
        """
