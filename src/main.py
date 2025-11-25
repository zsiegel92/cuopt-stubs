from modal import App, Image, asgi_app
from fastapi import FastAPI

image = (
    Image.debian_slim()
    .uv_sync()
    # .uv_pip_install(
    #     "cuopt-sh-client",
    #     "cuopt-server-cu13",
    # )
)
app = App(
    name="gpu-milp-2",
    image=image,
)


@app.function()
def hello():
    print("Hello, World!")


webapp = FastAPI()


@webapp.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.function()
@asgi_app()
def create_webapp():
    return webapp


@app.local_entrypoint()
def main():
    hello.remote()
