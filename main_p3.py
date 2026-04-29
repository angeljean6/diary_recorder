from journal_recorder import JournalRecorder

def main():
    my_journal = JournalRecorder("mylife.txt")

    print("--- Start Journal Entry ---")
    my_journal.record_multiple_lines()

if __name__ == "__main__":
    main()