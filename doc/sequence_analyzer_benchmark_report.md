# Performance Evaluation: Single-Pass vs. Built-In Sequence Analysis

## 1. Objective

This experiment compares two Python implementations of a sequence analyser:

- **Custom single-pass implementation:** calculates the minimum, maximum, sum, arithmetic mean, and counts of positive, negative, and zero values in one main traversal.
- **Built-in implementation:** uses Python's `max()`, `min()`, and `sum()` functions, plus generator expressions to count positive, negative, and zero values.

The goal is to compare their observed execution times and relate the measurements to theoretical time and auxiliary-space complexity.

## 2. Test Environment

| Item | Details |
|---|---|
| Computer | Apple Silicon Mac with M1 chip *(exact MacBook model not specified)* |
| Editor | Visual Studio Code |
| Operating system | macOS 15.7.5 (Build 24G624) |
| Platform | `macOS-15.7.5-arm64-arm-64bit` |
| Machine architecture | `arm64` |
| Python version | Python 3.12.3 |

The Python version and platform details were obtained from the benchmark environment. Other details, such as the exact MacBook model, power mode, and background workload, were not recorded.

## 3. Method

Four input sizes were tested: 100, 10,000, 100,000, and 1,000,000 elements. The input consisted of pseudo-random integers generated with Python's `random` module after setting a fixed seed.

Before timing each input size, the benchmark asserted that both implementations returned equal results for the same input. The improved benchmark warmed up each function, collected seven measurements using `timeit.repeat` with five calls per measurement, and reported the median time per call.

The input generation was outside the timed function, so the reported execution times measure the sequence-analysis functions rather than random-data generation.

## 4. Results

The following values are the measurements reported by the benchmark run.

| Input size | Custom single-pass | Built-in version | Custom speedup |
|---:|---:|---:|---:|
| 100 | 0.000009 s (0.009 ms) | 0.000018 s (0.018 ms) | 2.00× |
| 10,000 | 0.001154 s (1.154 ms) | 0.001707 s (1.707 ms) | 1.48× |
| 100,000 | 0.011523 s (11.523 ms) | 0.017178 s (17.178 ms) | 1.49× |
| 1,000,000 | 0.123119 s (123.119 ms) | 0.169094 s (169.094 ms) | 1.37× |

Speedup is calculated as:

\[
\text{Speedup} =
\frac{\text{Built-in execution time}}
{\text{Custom execution time}}
\]

A speedup greater than 1 means that the custom implementation was faster in that measurement. At one million elements, the measured speedup was approximately 1.37×. The custom implementation took about 27.2% less time than the built-in version in that run.

Because the timings are rounded and are from a single reported benchmark run, the speedup values should be treated as approximate.

## 5. Interpretation

### 5.1 Asymptotic time complexity

For ordinary numeric values under the usual unit-cost model, both implementations have linear time complexity:

\[
T(n) = \Theta(n)
\]

The custom implementation processes the elements in one main loop. The built-in implementation performs separate traversals for minimum, maximum, sum, and the three category counts. Both therefore perform work proportional to the number of input elements, although their constant factors differ.

The measurements are consistent with linear scaling: increasing the input size by a factor of ten from 10,000 to 100,000 increased the custom runtime by approximately a factor of ten. Empirical timing alone, however, is not a proof of asymptotic complexity.

### 5.2 Why the custom version may be faster

The custom implementation combines the calculations into one traversal, reducing repeated passes over the input. In this experiment, that benefit appears to outweigh the overhead of performing the loop in Python.

This is an interpretation rather than a proven causal result. Runtime depends on implementation details, Python version, input types, hardware, system activity, and measurement conditions. Python built-ins are often highly optimised, so another implementation or environment may produce different results.

### 5.3 Auxiliary-space complexity

The intended custom algorithm uses \(\Theta(1)\) auxiliary space if it iterates over the original list without creating a slice. For example:

```python
for i in range(1, len(numbers)):
    number = numbers[i]
```

By contrast, iterating over `numbers[1:]` creates a new list containing the remaining elements, requiring \(\Theta(n)\) additional space. The implementation used for the benchmark should be checked to establish which space-complexity claim applies.

The built-in implementation shown in the project uses generator expressions for the category counts, avoiding intermediate lists. Under the standard model, its auxiliary space is also \(\Theta(1)\), excluding the input itself and assuming the built-ins do not create input-sized copies.

## 6. Limitations

1. The report contains one set of benchmark results; it does not establish that the custom implementation is always faster.
2. The exact Python version and macOS version were not recorded.
3. Hardware and background activity may influence timings, especially for the smallest input.
4. The benchmark uses one data-generation pattern. Different input types and distributions may affect performance.
5. The implementations must be checked to ensure that the custom version does not use list slicing if constant auxiliary space is claimed.
6. No variability statistic or confidence interval was reported. Although the benchmark code uses the median of repeated measurements, the individual samples were not saved for further analysis.

## 7. Conclusion

In the reported experiment on an Apple M1 Mac, the custom single-pass sequence analyser was faster than the built-in version at all four tested input sizes. The observed speedup ranged from approximately 1.37× to 2.00×, with a speedup of approximately 1.37× at one million elements.

Both implementations are theoretically linear-time under the stated assumptions. The results illustrate that algorithms with the same asymptotic complexity can exhibit different practical runtimes because of constant factors and implementation details.

The findings should be described as preliminary and specific to the tested implementations and environment. A stronger conclusion requires recording the exact software environment, verifying the implementation details, saving individual timing samples, and repeating the experiment under controlled conditions.

## 8. Reproducibility checklist

Before treating this as a final experimental report:

- [ ] Confirm the Python version with `python --version` in the same VS Code terminal/environment used for the benchmark.
- [ ] Record the macOS version.
- [ ] Confirm that the custom implementation uses index-based iteration rather than `numbers[1:]` if claiming \(\Theta(1)\) auxiliary space.
- [ ] Keep the correctness assertion before each timing run.
- [ ] Save the individual timing samples, not only the median.
- [ ] Repeat the benchmark in a quiet environment and compare the results.
- [ ] Commit the benchmark script and both implementations to the repository.

## 9. Reproduction environment commands

The environment was recorded using the following commands in the VS Code terminal:

```bash
python --version
python -c "import platform, sys; print('Python:', sys.version); print('Platform:', platform.platform()); print('Machine:', platform.machine())"
sw_vers
```

The confirmed Python version is **3.12.3**.
