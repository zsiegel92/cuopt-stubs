from modal import (
    App,
    Image,
)

image = (
    Image.from_registry(
        "nvidia/cuopt:latest-cuda13.0-py3.13",
        add_python="3.13",
    )
    .uv_sync(
        uv_project_dir="./src/",
    )
    .uv_pip_install(
        "cuopt-sh-client",
        "cuopt-server-cu13",
        "cuopt-cu13==25.10.*",
        extra_index_url="https://pypi.nvidia.com",
    )
)

app = App(
    name="gpu-milp",
    image=image,
)


@app.function()
def print_arch():
    import platform

    # print cpu architecture
    print(platform.machine())


@app.function(gpu="A100")
def solve_milp():
    from cuopt.linear_programming.problem import Problem, CONTINUOUS, MAXIMIZE
    from cuopt.linear_programming.solver_settings import SolverSettings

    # Create a new problem
    problem = Problem("Simple LP")

    # Add variables
    x = problem.addVariable(lb=0, vtype=CONTINUOUS, name="x")
    y = problem.addVariable(lb=0, vtype=CONTINUOUS, name="y")

    # Add constraints
    problem.addConstraint(x + y <= 10, name="c1")
    problem.addConstraint(x - y >= 0, name="c2")

    # Set objective function
    problem.setObjective(x + y, sense=MAXIMIZE)

    # Configure solver settings
    settings = SolverSettings()
    settings.set_parameter("time_limit", 60)

    # Solve the problem
    problem.solve(settings)

    # Check solution status
    if problem.Status.name == "Optimal":
        print(f"Optimal solution found in {problem.SolveTime:.2f} seconds")
        print(f"x = {x.getValue()}")
        print(f"y = {y.getValue()}")
        print(f"Objective value = {problem.ObjValue}")


@app.function()
def generate_stubs():
    import subprocess
    import os

    subprocess.run(["stubgen", "-p", "cuopt", "-o", "stubs"])
    print("Stubs generated successfully")
    print(os.listdir("stubs"))
    with open("stubs/cuopt/__init__.pyi", "r") as f:
        file_contents = f.read()
        return file_contents


def copy_stubs_to_local():
    import os

    stubs_pyi = generate_stubs.remote()
    with open("stubs/cuopt/__init__.pyi", "w") as f:
        f.write(stubs_pyi)
    print("Stubs copied to local successfully")
    print(os.listdir("stubs"))


@app.local_entrypoint()
def main():
    print_arch.remote()
    generate_stubs.remote()
    solve_milp.remote()
