# cuopt-stubs

Type stubs for NVIDIA cuOpt library.

## Installation

```bash
pip install cuopt-stubs
```

## Usage

These stubs provide type hints for the `cuopt` package. Install them alongside the `cuopt` package to enable type checking with tools like mypy, pyright, and IDEs.

```python
from cuopt.linear_programming import Problem

# Your IDE and type checker will now have full type information
problem = Problem()
```

## Compatibility

These stubs are compatible with:
- Python 3.8+
- cuOpt (specify versions if known)

## Development

These stubs were generated using `mypy stubgen` and are maintained separately from the cuOpt package.

## License

MIT License
