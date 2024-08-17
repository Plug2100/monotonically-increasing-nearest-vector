import numpy as np
import warnings


# File with the test vectors
test_vectors_file = 'data/test_vectors.txt'
# File with the manually entered vectors
input_vectors_file = 'data/input_vectors.txt'


# Convert the DeprecationWarning (wrong format of the string in the source file) to an error
warnings.simplefilter('error', DeprecationWarning)


def _enforce_non_decreasing_vector(source_vector: np.ndarray) -> np.ndarray:
    """
    Input: The source vector
    Output: The desired vector
    The function implements the algorithm from a PDF file Algorithm_explanation.pdf
    """
    len_of_source_vector = len(source_vector)
    desired_vector = np.copy(source_vector).astype(float)
    
    # Updating y using the algorithm from PDF
    for element_position in range(len_of_source_vector - 1):
        if desired_vector[element_position] > desired_vector[element_position + 1]:
            # Looking for the first element bigger than i+1
            start_of_violation = element_position
            while start_of_violation > 0 and desired_vector[start_of_violation - 1] > desired_vector[element_position + 1]:
                start_of_violation -= 1
            # Averaging the violation sequence
            violation_sequence_avg = np.mean(source_vector[start_of_violation:element_position + 2])
            desired_vector[start_of_violation:element_position + 2] = violation_sequence_avg
    return desired_vector


def _process_file(filename: str) -> None:
    """
    Input: The source file name
    Output: None
    The function processes source file line by line and prints the source vector, the desired vector, and the distance between them
    """
    with open(filename, 'r') as file:
        lines_from_source_file = file.readlines()
    
    line_number = 1
    for line in lines_from_source_file:
        # Converting a string to a np.ndarray
        if len(line) == 1:
            print(f"Empty input, line {line_number}\n")
            line_number += 1
            continue
        try:
            source_vector = np.fromstring(line, dtype=float, sep=',')
            line_number += 1
        except DeprecationWarning:
            print(f"Wrong input format, line {line_number}\n")
            line_number += 1
            continue
        except Exception as error:
            print(f"{error}, line {line_number}\n")
            line_number += 1
            continue
        
        # Applying the function which implements the algorithm from a PDF file Algorithm_explanation.pdf
        desired_vector = _enforce_non_decreasing_vector(source_vector)

        # Calculating the distance between source vector and desired vector
        distance = np.linalg.norm(source_vector - desired_vector)
        distance = round(distance, 3)
        
        # The resulting output
        print(f"Input: {source_vector}")
        print(f"Output: {desired_vector}")
        print(f"Distance: {distance}\n")


def _get_user_input() -> bool:
    """
    Input: None
    Output: source option
    The function asks the user for the type of the source file:  test vectors (0) or manually entered vectors (1)
    """
    while True:
        try:
            print("Hello. Do you want to run the program for test vectors (0) OR manually entered vectors (1) ?")
            user_input = int(input())
            if user_input in [1, 0]:
                return user_input
            else:
                print("Invalid input. Enter 0 or 1.")
        except ValueError:
            print("Invalid input. Enter 0 or 1.")

  
def main() -> None:
    """
    Input: None
    Output: None
    The function performs the task "Given a vector x containing n numbers, find a vector y, such that the Euclidean distance between the two is minimized, 
    subject to the constraint that the values in y are monotonically increasing."
    """  
    user_value = _get_user_input()
    if user_value:
        filename = input_vectors_file
    else:
        filename = test_vectors_file
    _process_file(filename)


if __name__ == "__main__":
    main()
