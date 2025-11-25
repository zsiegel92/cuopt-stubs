# python -m modal run src.main
from src.app_infra import app, copy_stubs_to_local


@app.function(gpu="A100")
def solve_milp():
    from src.toy_milp import solve_toy_milp

    solve_toy_milp()


@app.local_entrypoint()
def main():
    copy_stubs_to_local()
    solve_milp.remote()
