from _typeshed import Incomplete
from enum import Enum

class VType(str, Enum):
    """
    The type of a variable is either continuous or integer.
    Variable Types can be directly used as a constant.
    CONTINUOUS is  VType.CONTINUOUS
    INTEGER is VType.INTEGER
    """
    CONTINUOUS = 'C'
    INTEGER = 'I'

CONTINUOUS: Incomplete
INTEGER: Incomplete

class CType(str, Enum):
    """
    The sense of a constraint is either LE, GE or EQ.
    Constraint Sense Types can be directly used as a constant.
    LE is CType.LE
    GE is CType.GE
    EQ is CType.EQ
    """
    LE = 'L'
    GE = 'G'
    EQ = 'E'

LE: Incomplete
GE: Incomplete
EQ: Incomplete

class sense(int, Enum):
    """
    The sense of a model is either MINIMIZE or MAXIMIZE.
    Model objective sense can be directly used as a constant.
    MINIMIZE is sense.MINIMIZE
    MAXIMIZE is sense.MAXIMIZE
    """
    MAXIMIZE = -1
    MINIMIZE = 1

MAXIMIZE: Incomplete
MINIMIZE: Incomplete

class Variable:
    """
    cuOpt variable object initialized with details of the variable
    such as lower bound, upper bound, type and name.
    Variables are always associated with a problem and can be
    created using :py:meth:`Problem.addVariable`.

    Parameters
    ----------
    lb : float
        Lower bound of the variable. Defaults to  0.
    ub : float
        Upper bound of the variable. Defaults to infinity.
    vtype : enum
        CONTINUOUS or INTEGER. Defaults to CONTINUOUS.
    obj : float
        Coefficient of the Variable in the objective.
    name : str
        Name of the variable. Optional.

    Attributes
    ----------
    VariableName : str
        Name of the Variable.
    VariableType : CONTINUOUS or INTEGER
        Variable type.
    LB : float
        Lower Bound of the Variable.
    UB : float
        Upper Bound of the Variable.
    Obj : float
        Coefficient of the variable in the Objective function.
    Value : float
        Value of the variable after solving.
    ReducedCost : float
        Reduced Cost after solving an LP problem.
    """
    index: int
    LB: Incomplete
    UB: Incomplete
    Obj: Incomplete
    Value: Incomplete
    ReducedCost: Incomplete
    VariableType: Incomplete
    VariableName: Incomplete
    def __init__(self, lb: float = 0.0, ub=..., obj: float = 0.0, vtype=..., vname: str = '') -> None: ...
    def getIndex(self):
        """
        Get the index position of the variable in the problem.
        """
    def getValue(self):
        """
        Returns the Value of the variable computed in current solution.
        Defaults to 0
        """
    def getObjectiveCoefficient(self):
        """
        Returns the objective coefficient of the variable.
        """
    def setObjectiveCoefficient(self, val) -> None:
        """
        Sets the objective cofficient of the variable.
        """
    def setLowerBound(self, val) -> None:
        """
        Sets the lower bound of the variable.
        """
    def getLowerBound(self):
        """
        Returns the lower bound of the variable.
        """
    def setUpperBound(self, val) -> None:
        """
        Sets the upper bound of the variable.
        """
    def getUpperBound(self):
        """
        Returns the upper bound of the variable.
        """
    def setVariableType(self, val) -> None:
        """
        Sets the variable type of the variable.
        Variable types can be either CONTINUOUS or INTEGER.
        """
    def getVariableType(self):
        """
        Returns the type of the variable.
        """
    def setVariableName(self, val) -> None:
        """
        Sets the name of the variable.
        """
    def getVariableName(self):
        """
        Returns the name of the variable.
        """
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __le__(self, other): ...
    def __ge__(self, other): ...
    def __eq__(self, other): ...

class LinearExpression:
    """
    LinearExpressions contain a set of variables, the coefficients
    for the variables, and a constant.
    LinearExpressions can be used to create constraints and the
    objective in the Problem.
    LinearExpressions can be added and subtracted with other
    LinearExpressions and Variables and can also be multiplied and
    divided by scalars.
    LinearExpressions can be compared with scalars, Variables, and
    other LinearExpressions to create Constraints.

    Parameters
    ----------
    vars : List
        List of Variables in the linear expression.
    coefficients : List
        List of coefficients corresponding to the variables.
    constant : float
        Constant of the linear expression.
    """
    vars: Incomplete
    coefficients: Incomplete
    constant: Incomplete
    def __init__(self, vars, coefficients, constant) -> None: ...
    def getVariables(self):
        """
        Returns all the variables in the linear expression.
        """
    def getVariable(self, i):
        """
        Gets Variable at ith index in the linear expression.
        """
    def getCoefficients(self):
        """
        Returns all the coefficients in the linear expression.
        """
    def getCoefficient(self, i):
        """
        Gets the coefficient of the variable at ith index of the
        linear expression.
        """
    def getConstant(self):
        """
        Returns the constant in the linear expression.
        """
    def zipVarCoefficients(self): ...
    def getValue(self):
        """
        Returns the value of the expression computed with the
        current solution.
        """
    def __len__(self) -> int: ...
    def __iadd__(self, other): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __isub__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __imul__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __itruediv__(self, other): ...
    def __truediv__(self, other): ...
    def __le__(self, other): ...
    def __ge__(self, other): ...
    def __eq__(self, other): ...

class Constraint:
    """
    cuOpt constraint object containing a linear expression,
    the sense of the constraint, and the right-hand side of
    the constraint.
    Constraints are associated with a problem and can be
    created using :py:meth:`Problem.addConstraint`.

    Parameters
    ----------
    expr : LinearExpression
        Linear expression corresponding to a problem.
    sense : enum
        Sense of the constraint. Either LE for <=,
        GE for >= or EQ for == .
    rhs : float
        Constraint right-hand side value.
    name : str, Optional
        Name of the constraint. Optional.

    Attributes
    ----------
    ConstraintName : str
        Name of the constraint.
    Sense : LE, GE or EQ
        Row sense. LE for >=, GE for <= or EQ for == .
    RHS : float
        Constraint right-hand side value.
    Slack : float
        Computed LHS - RHS with current solution.
    DualValue : float
        Constraint dual value in the current solution.
    """
    vindex_coeff_dict: Incomplete
    vars: Incomplete
    index: int
    Sense: Incomplete
    RHS: Incomplete
    ConstraintName: Incomplete
    DualValue: Incomplete
    Slack: Incomplete
    def __init__(self, expr, sense, rhs, name: str = '') -> None: ...
    def __len__(self) -> int: ...
    def getConstraintName(self):
        """
        Returns the name of the constraint.
        """
    def getSense(self):
        """
        Returns the sense of the constraint.
        Constraint sense can be LE(<=), GE(>=) or EQ(==).
        """
    def getRHS(self):
        """
        Returns the right-hand side value of the constraint.
        """
    def getCoefficient(self, var):
        """
        Returns the coefficient of a variable in the constraint.
        """
    def compute_slack(self): ...

class Problem:
    '''
    A Problem defines a Linear Program or Mixed Integer Program
    Variable can be be created by calling addVariable()
    Constraints can be added by calling addConstraint()
    The objective can be set by calling setObjective()
    The problem data is formed when calling solve().

    Parameters
    ----------
    model_name : str, optional
        Name of the model. Default is an empty string.

    Attributes
    ----------
    Name : str
        Name of the model.
    ObjSense : sense
        Objective sense (MINIMIZE or MAXIMIZE).
    ObjConstant : float
        Constant term in the objective.
    Status : int
        Status of the problem after solving.
    SolveTime : float
        Time taken to solve the problem.
    SolutionStats : object
        Solution statistics for LP or MIP problem.
    ObjValue : float
        Objective value of the problem.
    IsMIP : bool
        Indicates if the problem is a Mixed Integer Program.
    NumVariables : int
        Number of Variables in the problem.
    NumConstraints : int
        Number of constraints in the problem.
    NumNZs : int
        Number of non-zeros in the problem.

    Examples
    --------
    >>> problem = problem.Problem("MIP_model")
    >>> x = problem.addVariable(lb=-2.0, ub=8.0, vtype=INTEGER)
    >>> y = problem.addVariable(name="Var2")
    >>> problem.addConstraint(2*x - 3*y <= 10, name="Constr1")
    >>> expr = 3*x + y
    >>> problem.addConstraint(expr + x == 20, name="Constr2")
    >>> problem.setObjective(x + y, sense=MAXIMIZE)
    >>> problem.solve()
    '''
    Name: Incomplete
    vars: Incomplete
    constrs: Incomplete
    ObjSense: Incomplete
    ObjConstant: float
    Status: int
    ObjValue: Incomplete
    warmstart_data: Incomplete
    model: Incomplete
    solved: bool
    rhs: Incomplete
    row_sense: Incomplete
    constraint_csr_matrix: Incomplete
    lower_bound: Incomplete
    upper_bound: Incomplete
    var_type: Incomplete
    def __init__(self, model_name: str = '') -> None: ...
    class dict_to_object:
        def __init__(self, mdict) -> None: ...
    def update(self) -> None:
        """
        Update the problem. This is mandatory if attributes of
        existing Variables, Constraints or Objective has been
        modified.
        """
    def reset_solved_values(self) -> None: ...
    def addVariable(self, lb: float = 0.0, ub=..., obj: float = 0.0, vtype=..., name: str = ''):
        '''
        Adds a variable to the problem defined by lower bound,
        upper bound, type and name.

        Parameters
        ----------
        lb : float
            Lower bound of the variable. Defaults to  0.
        ub : float
            Upper bound of the variable. Defaults to infinity.
        vtype : enum :py:class:`VType`
            vtype.CONTINUOUS or vtype.INTEGER. Defaults to CONTINUOUS.
        name : string
            Name of the variable. Optional.

        Returns
        -------
        variable : :py:class:`Variable`
            Variable object added to the problem.

        Examples
        --------
        >>> problem = problem.Problem("MIP_model")
        >>> x = problem.addVariable(lb=-2.0, ub=8.0, vtype=INTEGER,
                name="Var1")
        '''
    def addConstraint(self, constr, name: str = ''):
        '''
        Adds a constraint to the problem defined by constraint object
        and name. A constraint is generated using LinearExpression,
        Sense and RHS.

        Parameters
        ----------
        constr : :py:class:`Constraint`
            Constructed using LinearExpressions (See Examples)
        name : string
            Name of the variable. Optional.

        Examples
        --------
        >>> problem = problem.Problem("MIP_model")
        >>> x = problem.addVariable(lb=-2.0, ub=8.0, vtype=INTEGER)
        >>> y = problem.addVariable(name="Var2")
        >>> problem.addConstraint(2*x - 3*y <= 10, name="Constr1")
        >>> expr = 3*x + y
        >>> problem.addConstraint(expr + x == 20, name="Constr2")
        '''
    def updateConstraint(self, constr, coeffs=[], rhs=None) -> None:
        '''
        Updates a previously added constraint. Values that can be updated are
        constraint coefficients and RHS.

        Parameters
        ----------
        constr : :py:class:`Constraint`
            Constraint to be updated.
        coeffs : List[Tuple[:py:class:`Variable`, coefficient]]
            List of Tuples containing variable and corresponding coefficient.
            Optional.
        rhs : int|float
            New RHS value for the constraint.

        Examples
        --------
        >>> problem = problem.Problem("MIP_model")
        >>> x = problem.addVariable(lb=0.0, vtype=INTEGER)
        >>> y = problem.addVariable(lb=0.0, vtype=INTEGER)
        >>> c1 = problem.addConstraint(2 * x + y <= 7, name="c1")
        >>> c2 = problem.addConstraint(x + y <= 5, name="c2")
        >>> problem.updateConstraint(c1, coeffs=[(x, 1)], rhs=10)
        '''
    def setObjective(self, expr, sense=...) -> None:
        '''
        Set the Objective of the problem with an expression that needs to
        be MINIMIZED or MAXIMIZED.

        Parameters
        ----------
        expr : :py:class:`LinearExpression` or :py:class:`Variable` or Constant
            Objective expression that needs maximization or minimization.
        sense : enum :py:class:`sense`
            Sets whether the problem is a maximization or a minimization
            problem. Values passed can either be MINIMIZE or MAXIMIZE.
            Defaults to MINIMIZE.

        Examples
        --------
        >>> problem = problem.Problem("MIP_model")
        >>> x = problem.addVariable(lb=-2.0, ub=8.0, vtype=INTEGER)
        >>> y = problem.addVariable(name="Var2")
        >>> problem.addConstraint(2*x - 3*y <= 10, name="Constr1")
        >>> expr = 3*x + y
        >>> problem.addConstraint(expr + x == 20, name="Constr2")
        >>> problem.setObjective(x + y, sense=MAXIMIZE)
        '''
    def updateObjective(self, coeffs=[], constant=None, sense=None) -> None:
        '''
        Updates the objective of the problem. Values that can be updated are
        objective coefficients, constant and sense.

        Parameters
        ----------
        coeffs : List[Tuple[:py:class:`Variable`, coefficient]]
            List of Tuples containing variable and corresponding coefficient.
            Optional.
        constant : int|float
            New Objective constant for the problem. Optional.
        sense : enum :py:class:`sense`
            Sets the objective sense to either maximize or minimize. Optional.

        Examples
        --------
        >>> problem = problem.Problem("MIP_model")
        >>> x = problem.addVariable(lb=0.0, vtype=INTEGER)
        >>> y = problem.addVariable(lb=0.0, vtype=INTEGER)
        >>> problem.setObjective(4*x + y + 4, MAXIMIZE)
        >>> problem.updateObjective(coeffs=[(x1, 1.0), (x2, 3.0)], constant=5,
                sense=MINIMIZE)
        '''
    def get_incumbent_values(self, solution, vars):
        """
        Extract incumbent values of the vars from a problem solution.
        """
    def get_pdlp_warm_start_data(self):
        '''
        Note: Applicable to only LP.
        Allows to retrieve the warm start data from the PDLP solver
        once the problem is solved.
        This data can be used to warmstart the next PDLP solve by setting it
        in :py:meth:`cuopt.linear_programming.solver_settings.SolverSettings.set_pdlp_warm_start_data`  # noqa

        Examples
        --------
        >>> problem = problem.Problem.readMPS("LP.mps")
        >>> problem.solve()
        >>> warmstart_data = problem.get_pdlp_warm_start_data()
        >>> settings.set_pdlp_warm_start_data(warmstart_data)
        >>> updated_problem = problem.Problem.readMPS("updated_LP.mps")
        >>> updated_problem.solve(settings)
        '''
    def getObjective(self):
        """
        Get the Objective expression of the problem.
        """
    def getVariables(self):
        """
        Get a list of all the variables in the problem.
        """
    def getVariable(self, identifier):
        """
        Get a Variable by its index or name.
        """
    def getConstraints(self):
        """
        Get a list of all the Constraints in a problem.
        """
    def getConstraint(self, identifier):
        """
        Get a Constraint by its index or name.
        """
    @classmethod
    def readMPS(cls, mps_file):
        '''
        Initiliaze a problem from an `MPS <https://en.wikipedia.org/wiki/MPS_(format)>`__ file.  # noqa

        Examples
        --------
        >>> problem = problem.Problem.readMPS("model.mps")
        '''
    def writeMPS(self, mps_file) -> None:
        '''
        Write the problem into an `MPS <https://en.wikipedia.org/wiki/MPS_(format)>`__ file.  # noqa

        Examples
        --------
        >>> problem.writeMPS("model.mps")
        '''
    @property
    def NumVariables(self): ...
    @property
    def NumConstraints(self): ...
    @property
    def NumNZs(self): ...
    @property
    def IsMIP(self): ...
    @property
    def Obj(self): ...
    def getCSR(self):
        """
        Computes and returns the CSR representation of the
        constraint matrix.
        """
    def relax(self):
        '''
        Relax a MIP problem into an LP problem and return the relaxed model.
        The relaxed model has all variable types set to CONTINUOUS.

        Examples
        --------
        >>> mip_problem = problem.Problem.readMPS("MIP.mps")
        >>> lp_problem = problem.relax()
        '''
    SolveTime: Incomplete
    SolutionStats: Incomplete
    def populate_solution(self, solution) -> None: ...
    def solve(self, settings=...) -> None:
        '''
        Optimizes the LP or MIP problem with the added variables,
        constraints and objective.

        Examples
        --------
        >>> problem = problem.Problem("MIP_model")
        >>> x = problem.addVariable(lb=-2.0, ub=8.0, vtype=INTEGER)
        >>> y = problem.addVariable(name="Var2")
        >>> problem.addConstraint(2*x - 3*y <= 10, name="Constr1")
        >>> expr = 3*x + y
        >>> problem.addConstraint(expr + x == 20, name="Constr2")
        >>> problem.setObjective(x + y, sense=MAXIMIZE)
        >>> problem.solve()
        '''
