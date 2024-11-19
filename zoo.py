class Zoo:
    def get_ticket_price(self, age):
        if age < 0:
            return "Invalid age"  # Handle invalid age
        elif 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:  # Fix: should include age 20
            return 100
        elif 21 <= age <= 60:  # Fix: should include age 21
            return 150
        elif age > 60:  # Fix: should only apply to age > 60
            return 100
