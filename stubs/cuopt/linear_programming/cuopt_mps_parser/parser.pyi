from cuopt_mps_parser.utilities import catch_mps_parser_exception

@catch_mps_parser_exception
def ParseMps(mps_file_path, fixed_mps_format: bool = False):
    """
    Reads the equation from the input text file which is MPS formatted

    Notes
    -----
    Read this link http://lpsolve.sourceforge.net/5.5/mps-format.htm for more
    details on both free and fixed MPS format.

    Parameters
    ----------
    mps_file_path : str
        Path to MPS formatted file
    fixed_mps_format : bool
        If MPS file should be parsed as fixed, false by default

    Returns
    -------
    data_model: DataModel
        A fully formed LP problem which represents the given MPS file

    Examples
    --------
    >>> from cuopt import linear_programming
    >>>
    >>> data_model = linear_programming.ParseMps(mps_file_path)
    >>>
    >>> # Build a solver setting object & lower the accuracy from 1e-4 to 1e-2
    >>> solver_settings = linear_programming.SolverSettings()
    >>> solver_settings.set_optimality_tolerance(1e-2)
    >>>
    >>> # Call solve
    >>> solution = linear_programming.Solve(data_model, solver_settings)
    >>>
    >>> # Print solution
    >>> print(solution.get_primal_solution())
    """
def toDict(model, json: bool = False): ...
