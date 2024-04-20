"""
Returns a list of contents contained in the file with the finite automaton definition.
"""
def read_file() -> list:
    while True:
        filename = input("Enter the name of the file containing DFA/NFA description: ")
        try:
            with open(f'{filename}', 'r') as file:
                lines = file.readlines()
        except FileNotFoundError: 
            print("File not found try again.")
        else:
            print("File read successfully.")
            return lines

"""
Returns a hashmap that defines the finite automaton as key-value pairs.
"""
def construct_finite_automaton(file_contents: list) -> map:
    finite_automaton_map = {}
    # Alphabet of NFA/DFA
    finite_automaton_map["alphabet"] = file_contents[0].strip()
    # Number of states in NFA/DFA
    finite_automaton_map["num_of_states"] = file_contents[1].strip()



def main():
    # Open the file and store its contents as a list
    finite_automaton_file_contents = read_file()
    # Store the finite automaton as a hashmap with key value pairs
    finite_automaton_definition = construct_finite_automaton(file_contents=finite_automaton_file_contents)
    print(finite_automaton_definition)


if __name__ == "__main__":
    main()
