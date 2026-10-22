
import random
import timeit
import statistics

from miniproject1 import seq_analyzer
from seq_analyzer_builtin import seq_analyzer_builtin


random.seed(42)

sizes = [100, 10_000, 100_000, 1_000_000]

# for n in sizes:
#     numbers = [random.randint(-1000, 1000) for _ in range(n)]

#     # Check correctness before benchmarking.
#     assert seq_analyzer(numbers) == seq_analyzer_builtin(numbers)

#     custom_time = min(
#         timeit.repeat(
#             lambda: seq_analyzer(numbers),
#             number=3,
#             repeat=5,
#         )
#     ) / 3

#     builtin_time = min(
#         timeit.repeat(
#             lambda: seq_analyzer_builtin(numbers),
#             number=3,
#             repeat=5,
#         )
#     ) / 3

#     print(
#         f"n={n:>9,} | "
#         f"single-pass={custom_time:.6f}s | "
#         f"built-in={builtin_time:.6f}s | "
#         f"ratio={custom_time / builtin_time:.2f}x"
#     )


def benchmark(func, numbers):
    # Warm-up: execute once before collecting measurements.
    func(numbers)

    measurements = timeit.repeat(
        lambda: func(numbers),
        number=5,
        repeat=7,
    )

    # Median time per execution, in seconds.
    return statistics.median(measurements) / 5


for n in sizes:
    numbers = [random.randint(-1000, 1000) for _ in range(n)]

    assert seq_analyzer(numbers) == seq_analyzer_builtin(numbers)

    custom_time = benchmark(seq_analyzer, numbers)
    builtin_time = benchmark(seq_analyzer_builtin, numbers)

    ratio = custom_time / builtin_time

    print(
        f"n={n:>9,} | "
        f"custom={custom_time:.6f}s | "
        f"built-in={builtin_time:.6f}s | "
        f"ratio={ratio:.2f}x"
    )
