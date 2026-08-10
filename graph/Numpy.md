---
broader: "[[Python]]"
inferred:skos:ancestor:
  - "[[Programming language]]"
  - "[[Python]]"
---
# NumPy

## Definition

NumPy is a fundamental package for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices along with a collection of mathematical functions, created by Travis Oliphant in 2005 by unifying features from Numeric and Numarray.

## Historical Development

1. **Numeric (1995)**: Jim Hugunin's original array package
2. **Numarray (2001)**: Alternative implementation with new features
3. **NumPy Creation (2005)**: Oliphant unifies both projects
4. **SciPy Integration**: Scientific computing ecosystem
5. **Modern NumPy**: Core foundation for data science in Python

## Oliphant's Original Vision

According to Oliphant (2006):
- Unify competing array implementations
- High-performance multidimensional arrays
- Broadcasting functionality
- Universal functions (ufuncs)
- C-API for extension modules
- Memory-efficient data structures

## Core Features

1. **ndarray Object**:
   - N-dimensional array type
   - Homogeneous data storage
   - Efficient memory layout
   - Vectorized operations

2. **Broadcasting**:
   - Automatic array shape matching
   - Element-wise operations
   - Dimension expansion rules
   - Performance optimization

3. **Universal Functions (ufuncs)**:
   - Element-wise operations
   - Vectorized computations
   - Type casting rules
   - Mathematical operations

4. **Linear Algebra**:
   - Matrix operations
   - Decompositions
   - Eigenvalue computations
   - Solve systems of equations

## Key Components

1. **Data Types**:
   - Numeric types (int, float, complex)
   - Boolean arrays
   - String arrays
   - Structured arrays
   - Custom data types

2. **Array Creation**:
   - zeros(), ones(), empty()
   - arange(), linspace()
   - random number generation
   - Loading from files

3. **Array Manipulation**:
   - Reshaping
   - Transposing
   - Concatenation
   - Splitting
   - Indexing and slicing

4. **Mathematical Functions**:
   - Trigonometric
   - Exponential/logarithmic
   - Statistical
   - Financial
   - Special functions

## Performance Features

1. **Memory Efficiency**:
   - Contiguous memory blocks
   - Minimal overhead
   - Cache-friendly layout
   - Memory views

2. **Vectorization**:
   - SIMD operations
   - Batch processing
   - Loop optimization
   - Parallel execution

3. **C-API Integration**:
   - External library interface
   - Extension modules
   - Performance-critical code
   - Custom operations

## Scientific Computing Applications

1. **Data Analysis**:
   - Statistical computations
   - Time series analysis
   - Signal processing
   - Image processing

2. **Machine Learning**:
   - Feature engineering
   - Model implementation
   - Neural networks
   - Data preprocessing

3. **Scientific Research**:
   - Physics simulations
   - Biological modeling
   - Climate science
   - Engineering calculations

4. **Visualization**:
   - Data preparation for plotting
   - Graphics processing
   - 3D rendering support
   - Animation data handling

## Ecosystem Integration

1. **SciPy Stack**:
   - SciPy (scientific algorithms)
   - Matplotlib (visualization)
   - Pandas (data structures)
   - IPython (interactive computing)

2. **Machine Learning Libraries**:
   - scikit-learn
   - TensorFlow
   - PyTorch
   - XGBoost

3. **Specialized Libraries**:
   - Astropy (astronomy)
   - BioPython (biology)
   - Seaborn (statistical visualization)
   - NetworkX (graph analysis)

## Best Practices

1. **Memory Management**:
   - Use views instead of copies
   - Preallocate arrays
   - Monitor memory usage
   - Use appropriate data types

2. **Performance Optimization**:
   - Vectorized operations
   - Avoid Python loops
   - Use broadcasting
   - Profile code

3. **Code Organization**:
   - Clear array naming
   - Documentation
   - Type hints
   - Error handling

## Scientific Impact

NumPy has:
- Revolutionized scientific computing in Python
- Enabled complex numerical operations
- Created standard array interface
- Unified the scientific Python ecosystem

## Future Developments

1. **Performance Improvements**:
   - SIMD optimizations
   - GPU acceleration
   - JIT compilation
   - Parallel processing

2. **Enhanced Features**:
   - Better type support
   - Improved error messages
   - Extended ufunc system
   - Advanced indexing

## Related Concepts
- [[Scientific computing]]
- [[Array programming]]
- [[Linear algebra]]
- [[Data science]]
- [[Python]]

## References

Oliphant, T. E. (2006). Guide to NumPy. Trelgol Publishing.

Harris, C. R., et al. (2020). Array programming with NumPy. Nature, 585(7825), 357-362.