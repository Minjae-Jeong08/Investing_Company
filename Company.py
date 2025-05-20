
class Company:
    def __init__(self, name, initial_investment):
        # Initializing the company with a name and an investment amount
        self.name = name
        self.initial_investment = initial_investment
        
    def __repr__(self):
        # Return a string representation of the company
        return f"Company(name='{self.name}', initial_investment={self.initial_investment})"
    
    def display_info(self):
        # Display the company details
        print(f"Company Name: {self.name}")
        print(f"Initial Investment: ${self.initial_investment}")


