# Code Instrumentation and Sampling for Python Programs

## Project Overview
This project was developed as part of the Software Testing course during the second semester of 2022 at Pontificia Universidad Católica de Chile. The main focus of the project is to explore dynamic analysis techniques, specifically **code instrumentation** and **sampling**, to collect and report runtime data of Python programs.

The project involves modifying an existing instrumentor to collect metrics on function calls and execution times, as well as implementing a call context tree using a sampling method.

## Objectives
The objectives of this project are:
- To understand the logic behind code instrumentation and sampling techniques used in dynamic analysis.
- To grasp the advantages, limitations, and trade-offs of these techniques.
- To implement an instrumentor that reports various metrics about the functions in a Python program.
- To modify a sampler to produce a **Call Context Tree**, showing execution time per method in different call contexts.

## Key Features
### Instrumentor (Code Instrumentation)
The instrumentor collects the following metrics during the execution of Python programs:
- **Frequency**: The number of times each function is called.
- **Execution Time**: The maximum, minimum, and average time taken by each function.
- **Callers**: The functions that invoked each analyzed function.
- **Cacheable**: Identifies functions that could benefit from caching, based on repeated argument patterns and return values.

### Sampler (Code Sampling)
The sampler is used to build a **Call Context Tree**, which shows the execution time of functions in the context of their calling environment. This is done by periodically checking the execution stack of a program.

## Project Structure
- **`instrumentor/`**: Contains the code for the instrumentor, which analyzes Python programs by instrumenting their functions.
- **`instrumentor/input_code/`**: Sample Python code for testing the instrumentor.
- **`sampler/`**: Contains the code for the sampler, which analyzes the call context of functions during execution.
- **`sampler/input_code/`**: Sample Python code for testing the sampler.

## Requirements
- Python 3.x
- Basic knowledge of terminal commands.

## How to Run
1. Clone the repository:

   ```bash
   git clone <repository-url>
    ```

2. Navigate to the **instrumentor** directory:

    ```bash
    cd instrumentor
    ```

    To run the **instrumentor** on a Python program, use the following command:

    ```bash
    python3 profile.py code{i}
    ```

    This will produce a report in the console, showing metrics like function frequency, execution time, and caller relationships.

3. Navigate to the **sampler** directory:

    ```bash
    cd sampler
    ```

    To run the **sampler** on a Python program, use the following command:

    ```bash
    python3 profile.py code{i}
    ```

    This will output a Call Context Tree, showing the execution time of each function in various contexts.

## Example Output

### Instrumentor Output

```bash
fun     freq   avg     max     min     cache   callers
main    1      13.013  13.013  13.013  1       []
foo     1      13.013  13.013  13.013  1       ['main']
bar     2      5.011   5.015   5.007   0       ['foo']
```

### Sampler Output

```bash
total (7 seconds)
    _bootstrap (7 seconds)
        _bootstrap_inner (7 seconds)
            run (7 seconds)
                execute_script (7 seconds)
                    <module> (6 seconds)
                        main(6 seconds)
                            foo(6 seconds)
                                bar(1 second)
                            zoo(3 seconds)
                                bar(1 second)
```

## How to Test

- The project includes several sample Python programs located in the input_code directories of both the instrumentor and sampler. You can run these examples as described above to see the functionality in action.