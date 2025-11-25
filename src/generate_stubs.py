# python -m modal run src.main
from src.app_infra import app, copy_stubs_to_local





@app.local_entrypoint()
def main():
    copy_stubs_to_local()
