"""
This is AI generated - editted slightly to remove unnecessary code
"""
import re
from itertools import product

def solve_factory_puzzle(input_data):
    """
    Parses the puzzle input and calculates the minimum total button presses.
    """
    machines = parse_input(input_data)
    for m in machines: print(m)
    
    total_min_presses = 0

    print(f"Processing {len(machines)} machines...\n")

    for i, (target_vector, button_matrix) in enumerate(machines):
        # Solve Ax = B over GF(2)
        min_presses = solve_machine(target_vector, button_matrix)
        
        if min_presses is None:
            print(f"Machine {i+1}: No solution found (Impossible configuration).")
        else:
            print(f"Machine {i+1}: Minimum presses = {min_presses}")
            total_min_presses += min_presses

    return total_min_presses

def parse_input(data):
    """
    Parses the raw input string into a list of (target_vector, button_matrix) tuples.
    """
    machines = []
    lines = data.split('\n')
    
    for line in lines:
        # 1. Parse Indicator Diagram [.##.]
        diagram_match = re.search(r'\[([.#]+)\]', line)
        if not diagram_match: continue

        diagram_str = diagram_match.group(1)
        num_lights = len(diagram_str)
        
        # Target vector B (column vector represented as a list)
        # '.' = 0 (off), '#' = 1 (on)
        target_vector = [1 if char == '#' else 0 for char in diagram_str]
        
        # 2. Parse Buttons (1,3) (2) ...
        # Find all parenthesized groups
        button_matches = re.findall(r'\(([\d,]+)\)', line)
        
        # Build the matrix A. 
        # A is size N x M (rows=lights, cols=buttons)
        # We'll build it as a list of columns first (one column per button)
        matrix_columns = []
        
        for button_str in button_matches:
            affected_indices = [int(x) for x in button_str.split(',')]
            
            # Create a column for this button
            col = [0] * num_lights
            for idx in affected_indices:
                if 0 <= idx < num_lights:
                    col[idx] = 1
            matrix_columns.append(col)
            
        # Transpose to get standard row-major matrix (list of rows)
        # A[i][j] is 1 if button j affects light i
        num_buttons = len(matrix_columns)
        button_matrix = [[matrix_columns[j][i] for j in range(num_buttons)] 
                         for i in range(num_lights)]
                         
        machines.append((target_vector, button_matrix))
        
    return machines

def solve_machine(B, A):
    """
    Solves Ax = B over GF(2) and returns the minimum Hamming weight of x.
    Uses Gaussian Elimination.

    B -> target vector
    A -> button matrix
    """
    num_rows = len(A)
    num_cols = len(A[0])
    
    # Augment matrix A with vector B: [A | B] - in other words adds B to the end of matrix A
    aug_matrix = [row[:] + [B[i]] for i, row in enumerate(A)]
    
    # --- Gaussian Elimination (Row Reduction) ---
    pivot_row = 0
    pivot_cols = [] # Keep track of which columns have pivots
    
    for col in range(num_cols):
        # Find a row with a 1 in this column (at or below pivot_row)
        candidate = -1
        for r in range(pivot_row, num_rows):
            if aug_matrix[r][col] == 1:
                candidate = r
                break
        
        if candidate == -1:
            continue # No pivot in this column, it's a free variable
            
        # Swap rows to bring pivot to current position
        aug_matrix[pivot_row], aug_matrix[candidate] = aug_matrix[candidate], aug_matrix[pivot_row]
        
        # Eliminate other rows
        for r in range(num_rows):
            if r != pivot_row and aug_matrix[r][col] == 1:
                # Row XOR Row (Modulo 2 subtraction/addition)
                for c in range(num_cols + 1):
                    aug_matrix[r][c] ^= aug_matrix[pivot_row][c]
        
        pivot_cols.append(col)
        pivot_row += 1
        
    # --- Check for Consistency ---
    # If a row is all zeros except the last element (the augmented part), 0 = 1 -> Impossible
    # for r in range(pivot_row, num_rows):
    #     if aug_matrix[r][-1] == 1:
    #         return None # No solution

    # --- Find Particular Solution ---
    # Start with all zeros
    x_particular = [0] * num_cols
    
    # Back-substitution (trivial in RREF: just map pivots to target values)
    # Because we zeroed out rows above and below pivots, the pivot row explicitly tells us the value
    for i, p_col in enumerate(pivot_cols):
        x_particular[p_col] = aug_matrix[i][-1]
        
    # --- Find Null Space Basis (Free Variables) ---
    free_vars = [c for c in range(num_cols) if c not in pivot_cols]
    null_basis_vectors = []
    
    for free_col in free_vars:
        # Construct a basis vector for this free variable
        vec = [0] * num_cols
        vec[free_col] = 1 # The free variable itself is 1
        
        # Determine the dependent variables (pivots) required to balance this free var to 0
        for i, p_col in enumerate(pivot_cols):
            if aug_matrix[i][free_col] == 1:
                vec[p_col] = 1
        
        null_basis_vectors.append(vec)
        
    # --- Find Minimum Hamming Weight ---
    # We must check all combinations of the null space vectors added to the particular solution.
    # Total solutions = 2^(number of free variables)
    
    min_weight = float('inf')
    
    # Iterate through all combinations of coefficients (0 or 1) for the free variables
    for coeffs in product([0, 1], repeat=len(free_vars)):
        current_x = list(x_particular)
        
        # Add the linear combination of basis vectors
        for i, coeff in enumerate(coeffs):
            if coeff == 1:
                # Add basis vector i to current_x
                for j in range(num_cols):
                    current_x[j] ^= null_basis_vectors[i][j]
        
        # Calculate Hamming weight (sum of 1s)
        weight = sum(current_x)
        if weight < min_weight:
            min_weight = weight
            
    return min_weight

# --- Test with the Example Input provided ---
example_input = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

if __name__ == "__main__":
    result = solve_factory_puzzle(example_input)
    print("-" * 30)
    print(f"Total Fewest Presses: {result}")