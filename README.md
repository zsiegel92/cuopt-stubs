# cuOpt Stub Generation

This repository contains a script to auto-generate stubs for Nvidia's cuOpt Python interface. It generates those by installing cuOpt on a container on Modal.com, using MyPy's `stubgen` utility, and serializing the stubs as a tarball to the development machine.

The stubs are on PyPi! https://pypi.org/project/cuopt-stubs/0.2.0/


Install the stubs with `uv add cuopt-stubs` or `pip install cuopt-stubs`.

Installing these stubs

## Rebuilding stubs

```sh
# Bump the version number in stubs/pyproject.toml
python -m modal run src.generate_stubs
cd stubs/
rm -rf dist/ build/ *.egg-info
python -m build
# Upload to PyPI
python -m twine upload dist/*
```

# Run MILPs on GPU with cuOpt

- [Install cuOpt](https://docs.nvidia.com/cuopt/user-guide/latest/cuopt-python/quick-start.html)
- [cuOpt base images](https://hub.docker.com/r/nvidia/cuopt/tags)


----


## [Does Gurobi Support GPUs?](https://support.gurobi.com/hc/en-us/articles/360012237852-Does-Gurobi-support-GPUs?utm_source=chatgpt.com)
>
> The answer to the question "Does Gurobi support GPUs" is: Yes, we have the ability to benchmark Gurobi users' optimization models on NVIDIA GPU hardware, and users can download and try our GPU-enabled PDHG implementation.
>
>This article documents the latest and previous updates on Gurobi's efforts to leverage GPU technology within the field of mathematical optimization. We plan to update this article with resources for Gurobi's latest benchmark results on GPUs as they become available, while keeping previous statements as record to show the rapid evolution of this field.  
>
> 2025
> The Gurobi development team is partnering with NVIDIA to advance first-order methods for large-scale optimization.  Gurobi is excited about the open-source release of cuOpt’s PDLP, which will help bring more GPU-friendly algorithms to linear programming. We also look forward to understanding how other parts of cuOpt might help optimization users.  
>
> In September we released an alpha version of our GPU-enabled solver for public testing.  
>
> For the full story of our recent GPU journey and testing methodology, see the blog post Using GPUs to Solve LPs: What’s in It for Me?
>
> 2024
> The Gurobi development team is collaborating with NVIDIA to study the performance on the Grace Hopper chip. For a full report, see the blog post Boosting Mathematical Optimization Performance and Energy Efficiency on the NVIDIA Grace CPU. This work was presented at NVIDIA GTC in March 2024.
>
> In December of 2024, Gurobi founder Ed Rothberg presented our first benchmarking results on Grace Hopper GPU in the webinar New Options for Solving Giant LPs. What changed since 2023? The ability to leverage libraries for sparse linear algebra on GPU and the implementation of the barrier method and first-order LP algorithms (i.e., PDHG) on GPU. 
>
> 2023
> The Gurobi development team is watching GPUs (Graphics Processing Units) closely, but up to this point, all of the evidence indicates that they aren't well suited to the needs of an LP/MIP/QP solver. Specifically:
>
> GPUs don't work well for sparse linear algebra, which dominates much of linear programming. GPUs rely on keeping hundreds or even thousands of independent processors busy at a time. The extremely sparse matrices that are typical in linear programming don't admit nearly that level of parallelism.
> GPUs are built around SIMD computations, where all processors perform the same instruction in each cycle (but on different data). Parallel MIP explores different sections of the search tree on different processors. The computations required at different nodes in the search tree are quite different, so SIMD computation is not well suited to the needs of parallel MIP.
> Note that CPUs and GPUs are both improving parallelism as a means to increase performance. The Gurobi Optimizer is designed to effectively exploit multiple cores in a CPU, so you'll definitely see a benefit from more parallelism in the future.