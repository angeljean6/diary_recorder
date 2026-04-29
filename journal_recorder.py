class JournalRecorder:
    def __init__(self, output_file):
        self.output_file = output_file

    def record_multiple_lines(self):
        """Captures user input and writes to the designated file."""
        with open(self.output_file, 'w') as file:
            while True:
                user_input = input("Enter line: ")
                file.write(f"{user_input}\n")

                choice = input("Are there more lines y/n? ").lower()
                if choice != 'y':
                    break
            print(f"\nSuccess: Content saved to {self.output_file}.")