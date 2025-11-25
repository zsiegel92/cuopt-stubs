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


@app.function(gpu="A100")
def generate_stubs():
    import subprocess
    import tarfile
    import io
    import sys

    print("Checking if cuopt is installed...")
    try:
        import cuopt

        print(f"✓ cuopt found at: {cuopt.__file__}")
    except ImportError as e:
        print(f"✗ cuopt not importable: {e}")
        print(f"Python path: {sys.path}")

    # Generate stubs
    result = subprocess.run(
        [
            "stubgen",
            "-p",
            "cuopt",
            "--include-docstrings",
            "--verbose",
            "-o",
            "/tmp/stubs",
        ],
        capture_output=True,
        text=True,
    )
    print(f"Stubgen stdout: {result.stdout}")
    print(f"Stubgen stderr: {result.stderr}")
    print(f"Stubgen return code: {result.returncode}")

    # Check if stubs were actually created
    import os

    if os.path.exists("/tmp/stubs/cuopt"):
        print("✓ Stubs directory created")
        print(f"Contents: {os.listdir('/tmp/stubs/cuopt')}")
    else:
        print("✗ Stubs directory not created")
        raise FileNotFoundError("stubgen failed to generate stubs for cuopt")

    # Create a tar.gz of all the stubs
    tar_buffer = io.BytesIO()
    with tarfile.open(fileobj=tar_buffer, mode="w:gz") as tar:
        tar.add("/tmp/stubs/cuopt", arcname="cuopt")

    tar_buffer.seek(0)
    print("Stubs generated and packaged successfully")
    return tar_buffer.read()


def copy_stubs_to_local():
    import tarfile
    import io
    import os
    from pathlib import Path

    # Get the tarball from the remote function
    print("Generating stubs on remote server...")
    stubs_tarball = generate_stubs.remote()

    # Create stubs directory if it doesn't exist
    stubs_dir = Path("stubs")
    stubs_dir.mkdir(exist_ok=True)

    # Extract the tarball
    print(f"Extracting stubs to {stubs_dir.absolute()}...")
    tar_buffer = io.BytesIO(stubs_tarball)
    with tarfile.open(fileobj=tar_buffer, mode="r:gz") as tar:
        tar.extractall(path=stubs_dir)

    print("Stubs copied to local successfully!")
    print(f"Stubs location: {stubs_dir.absolute() / 'cuopt'}")

    # Show the structure
    cuopt_stubs = stubs_dir / "cuopt"
    if cuopt_stubs.exists():
        print("\nGenerated stub files:")
        for root, _dirs, files in os.walk(cuopt_stubs):
            level = root.replace(str(cuopt_stubs), "").count(os.sep)
            indent = " " * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = " " * 2 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")
