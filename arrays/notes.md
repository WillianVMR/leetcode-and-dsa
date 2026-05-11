# Arrays - Good for cache

## Static vs Dynamic Arrays

### Static Arrays

Fixed-size arrays where the length is determined at creation and cannot change.

- **Memory:** Stack / static memory — size fixed at compile time
- **Doesn't change size** — fewer operations needed, no resizing overhead
- **Performance gain** — contiguous memory, no indirection, cache-friendly
- **Safety** — fewer memory leaks since no dynamic allocation involved
- **Best for:** performance-critical systems (C, Rust)

**C++:**

```cpp
// Stack-allocated, fixed size known at compile time
int arr[5] = {1, 2, 3, 4, 5};

// std::array (preferred in modern C++) — fixed size, bounds-checked with .at()
#include <array>
std::array<int, 5> arr = {1, 2, 3, 4, 5};
```

**Python:**

Python has no true static array built-in. The closest equivalent is a fixed-size array from the `array` module or a tuple (immutable, but not resizable):

```python
import array
arr = array.array('i', [1, 2, 3, 4, 5])  # typed, but still resizable

# Tuple — immutable, fixed content
arr = (1, 2, 3, 4, 5)
```

**Rust:**

```rust
// Fixed size, type and length in the type signature
let arr: [i32; 8] = [0; 8];
```

### Dynamic Arrays

Resizable arrays that grow/shrink as elements are added or removed. They allocate extra capacity and resize (usually 2x) when full, giving **amortized O(1)** append.

- **Memory:** Heap — variable size allocated at runtime
- **Grows and shrinks** — flexibility to handle variable-size data
- **Resize cost:** O(n) — when capacity is exceeded, a new block is allocated and all elements are copied
- **Tradeoffs:** higher risk of fragmentation and memory leaks due to dynamic allocation
- **Best for:** general-purpose systems with variable-size data (JS, Python, Rust `Vec`, C++ `std::vector`, Java `ArrayList`)

**C++:**

```cpp
#include <vector>
std::vector<int> vec = {1, 2, 3};
vec.push_back(4);    // O(1) amortized
vec.pop_back();      // O(1)
vec[0];              // O(1) access
vec.size();          // current number of elements
vec.capacity();      // allocated capacity before next resize
```

**Python:**

```python
lst = [1, 2, 3]
lst.append(4)        # O(1) amortized
lst.pop()            # O(1)
lst[0]               # O(1) access
len(lst)             # current number of elements
```

Python's `list` is a dynamic array internally (array of pointers). There is no built-in way to inspect capacity.

### Key Differences

|                      | Static                         | Dynamic                                                  |
| -------------------- | ------------------------------ | -------------------------------------------------------- |
| Size                 | Fixed at compile time          | Variable at runtime                                      |
| Memory location      | Stack / static memory          | Heap                                                     |
| Insert at end        | N/A (full)                     | O(1) amortized                                           |
| Resize               | N/A                            | O(n) — copies all elements                               |
| Access by index      | O(1)                           | O(1)                                                     |
| Insert/delete middle | O(n)                           | O(n)                                                     |
| Memory usage         | Exact allocation               | Over-allocates for growth                                |
| Cache performance    | Excellent (contiguous)         | Good (contiguous, but pointer indirection in Python)     |
| Safety               | Fewer memory leaks             | Risk of fragmentation / memory leaks                     |
| Advantage            | Performance                    | Flexibility                                              |
| Best for             | Performance-critical (C, Rust) | General-purpose (JS, Python, C++ vector, Java ArrayList) |
