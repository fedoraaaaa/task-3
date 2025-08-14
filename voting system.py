class VotingSystem:
    def __init__(self):
        self.__candidates = {}  # Private dictionary to store candidates and votes
    
    def add_candidate(self, name):
        """Add a new candidate to the voting system"""
        if name not in self.__candidates:
            self.__candidates[name] = 0
            print(f"Candidate '{name}' added successfully.")
        else:
            print(f"Candidate '{name}' already exists.")
    
    def remove_candidate(self, name):
        """Remove a candidate from the voting system"""
        if name in self.__candidates:
            del self.__candidates[name]
            print(f"Candidate '{name}' removed successfully.")
        else:
            print(f"Candidate '{name}' not found.")
    
    def vote_to_candidate(self, name):
        """Vote for a specific candidate"""
        if name in self.__candidates:
            self.__candidates[name] += 1
            print(f"Vote for '{name}' recorded.")
        else:
            print(f"Candidate '{name}' not found. Vote not counted.")
    
    def display_winner(self):
        """Display the candidate with the most votes"""
        if not self.__candidates:
            print("No candidates in the system.")
            return
        
        max_votes = max(self.__candidates.values())
        winners = [name for name, votes in self.__candidates.items() if votes == max_votes]
        
        if len(winners) == 1:
            print(f"The winner is {winners[0]} with {max_votes} votes.")
        else:
            print(f"It's a tie between {', '.join(winners)} with {max_votes} votes each.")
    
    def display_results(self):
        """Display all candidates and their votes"""
        print("\nCurrent Voting Results:")
        for name, votes in self.__candidates.items():
            print(f"{name}: {votes} votes")

# Example usage
if __name__ == "__main__":
    vs = VotingSystem()
    
    vs.add_candidate("Alice")
    vs.add_candidate("Bob")
    vs.add_candidate("Charlie")
    
    vs.vote_to_candidate("Alice")
    vs.vote_to_candidate("Bob")
    vs.vote_to_candidate("Alice")
    vs.vote_to_candidate("Charlie")
    vs.vote_to_candidate("Bob")
    vs.vote_to_candidate("Alice")
    
    vs.display_results()
    vs.display_winner()
    
    vs.remove_candidate("Charlie")
    vs.display_results()