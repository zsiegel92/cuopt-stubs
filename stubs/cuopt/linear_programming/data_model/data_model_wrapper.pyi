import _cython_3_1_6
from typing import Any

__reduce_cython__: _cython_3_1_6.cython_function_or_method
__setstate_cython__: _cython_3_1_6.cython_function_or_method
__test__: dict
get_data_ptr: _cython_3_1_6.cython_function_or_method
type_cast: _cython_3_1_6.cython_function_or_method

class DataModel:
    """DataModel()"""
    def __init__(self) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def get_ascii_row_types(self) -> Any:
        """DataModel.get_ascii_row_types(self)"""
    def get_constraint_bounds(self) -> Any:
        """DataModel.get_constraint_bounds(self)"""
    def get_constraint_lower_bounds(self) -> Any:
        """DataModel.get_constraint_lower_bounds(self)"""
    def get_constraint_matrix_indices(self) -> Any:
        """DataModel.get_constraint_matrix_indices(self)"""
    def get_constraint_matrix_offsets(self) -> Any:
        """DataModel.get_constraint_matrix_offsets(self)"""
    def get_constraint_matrix_values(self) -> Any:
        """DataModel.get_constraint_matrix_values(self)"""
    def get_constraint_upper_bounds(self) -> Any:
        """DataModel.get_constraint_upper_bounds(self)"""
    def get_initial_dual_solution(self) -> Any:
        """DataModel.get_initial_dual_solution(self)"""
    def get_initial_primal_solution(self) -> Any:
        """DataModel.get_initial_primal_solution(self)"""
    def get_objective_coefficients(self) -> Any:
        """DataModel.get_objective_coefficients(self)"""
    def get_objective_name(self) -> Any:
        """DataModel.get_objective_name(self)"""
    def get_objective_offset(self) -> Any:
        """DataModel.get_objective_offset(self)"""
    def get_objective_scaling_factor(self) -> Any:
        """DataModel.get_objective_scaling_factor(self)"""
    def get_problem_name(self) -> Any:
        """DataModel.get_problem_name(self)"""
    def get_row_names(self) -> Any:
        """DataModel.get_row_names(self)"""
    def get_row_types(self) -> Any:
        """DataModel.get_row_types(self)"""
    def get_sense(self) -> Any:
        """DataModel.get_sense(self)"""
    def get_variable_lower_bounds(self) -> Any:
        """DataModel.get_variable_lower_bounds(self)"""
    def get_variable_names(self) -> Any:
        """DataModel.get_variable_names(self)"""
    def get_variable_types(self) -> Any:
        """DataModel.get_variable_types(self)"""
    def get_variable_upper_bounds(self) -> Any:
        """DataModel.get_variable_upper_bounds(self)"""
    def set_constraint_bounds(self, b) -> Any:
        """DataModel.set_constraint_bounds(self, b)"""
    def set_constraint_lower_bounds(self, constraint_lower_bounds) -> Any:
        """DataModel.set_constraint_lower_bounds(self, constraint_lower_bounds)"""
    def set_constraint_upper_bounds(self, constraint_upper_bounds) -> Any:
        """DataModel.set_constraint_upper_bounds(self, constraint_upper_bounds)"""
    def set_csr_constraint_matrix(self, A_values, A_indices, A_offsets) -> Any:
        """DataModel.set_csr_constraint_matrix(self, A_values, A_indices, A_offsets)"""
    def set_data_model_view(self) -> Any:
        """DataModel.set_data_model_view(self)"""
    def set_initial_dual_solution(self, initial_dual_solution) -> Any:
        """DataModel.set_initial_dual_solution(self, initial_dual_solution)"""
    def set_initial_primal_solution(self, initial_primal_solution) -> Any:
        """DataModel.set_initial_primal_solution(self, initial_primal_solution)"""
    def set_maximize(self, maximize) -> Any:
        """DataModel.set_maximize(self, maximize)"""
    def set_objective_coefficients(self, c) -> Any:
        """DataModel.set_objective_coefficients(self, c)"""
    def set_objective_name(self, objective_name) -> Any:
        """DataModel.set_objective_name(self, objective_name)"""
    def set_objective_offset(self, objective_offset) -> Any:
        """DataModel.set_objective_offset(self, objective_offset)"""
    def set_objective_scaling_factor(self, objective_scaling_factor) -> Any:
        """DataModel.set_objective_scaling_factor(self, objective_scaling_factor)"""
    def set_problem_name(self, problem_name) -> Any:
        """DataModel.set_problem_name(self, problem_name)"""
    def set_row_names(self, row_names) -> Any:
        """DataModel.set_row_names(self, row_names)"""
    def set_row_types(self, row_types) -> Any:
        """DataModel.set_row_types(self, row_types)"""
    def set_variable_lower_bounds(self, variable_lower_bounds) -> Any:
        """DataModel.set_variable_lower_bounds(self, variable_lower_bounds)"""
    def set_variable_names(self, variables_names) -> Any:
        """DataModel.set_variable_names(self, variables_names)"""
    def set_variable_types(self, variable_types) -> Any:
        """DataModel.set_variable_types(self, variable_types)"""
    def set_variable_upper_bounds(self, variable_upper_bounds) -> Any:
        """DataModel.set_variable_upper_bounds(self, variable_upper_bounds)"""
    def writeMPS(self, user_problem_file) -> Any:
        """DataModel.writeMPS(self, user_problem_file)"""
    def __reduce__(self):
        """DataModel.__reduce_cython__(self)"""
