from Bank.clients.adult import Adult
from Bank.clients.student import Student
from Bank.loans.mortgage_loan import MortgageLoan
from Bank.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity):
        self.capacity = capacity  # The number of clients а Bank can have
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in ["StudentLoan", "MortgageLoan"]:
            raise Exception("Invalid loan type!")
        if loan_type == "StudentLoan":
            loan = StudentLoan()
            self.loans.append(loan)
            return f"{loan_type} was successfully added."
        elif loan_type == "MortgageLoan":
            loan = MortgageLoan()
            self.loans.append(loan)
            return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in ["Student", "Adult"]:
            raise Exception("Invalid client type!")
        if self.capacity == 0:
            return f"Not enough bank capacity."
        if client_type == "Student":
            client = Student(client_name, client_id, income)
            self.clients.append(client)
            self.capacity -= 1
            return f"{client_type} was successfully added."
        elif client_type == "Adult":
            client = Adult(client_name, client_id, income)
            self.clients.append(client)
            self.capacity -= 1
            return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = [loan for loan in self.loans if loan.__class__.__name__ == loan_type][0]
        client = [client for client in self.clients if client.client_id == client_id][0]

        if client.__class__.__name__ == 'Student' and loan.__class__.__name__ == 'StudentLoan':
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        elif client.__class__.__name__ == 'Adult' and loan.__class__.__name__ == 'MortgageLoan':
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        client_list = []
        for client in self.clients:
            if client.client_id == client_id:
                client_list.append(client)
        if not client_list:
            raise Exception("No such client!")
        client = client_list[0]
        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        self.capacity += 1
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = []
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                changed_loans.append(loan)
        return f"Successfully changed {len(changed_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients = []
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_clients.append(client)
        return f"Number of clients affected: {len(changed_clients)}."

    def get_statistics(self):
        total_income = 0.0
        granted_loans = []
        total_client_interest_rate = 0.0
        for client in self.clients:
            total_income += client.income
            total_client_interest_rate += client.interest
            if client.loans:
                for loan in client.loans:
                    granted_loans.append(loan)
        available_loans = []
        for loan in self.loans:
            available_loans.append(loan)
        total_sum_granted_loans = 0.0
        for loan in granted_loans:
            total_sum_granted_loans += loan.amount
        total_sum_available_loans = 0.0
        for loan in available_loans:
            total_sum_available_loans += loan.amount

        average_client_interest_rate = 0
        if len(self.clients) > 0:
            average_client_interest_rate += total_client_interest_rate / len(self.clients)

        result = f"Active Clients: {len(self.clients)}\nTotal Income: {total_income:.2f}\nGranted Loans: {len(granted_loans)}, Total Sum: {total_sum_granted_loans:.2f}\n"
        result += f"Available Loans: {len(available_loans)}, Total Sum: {total_sum_available_loans:.2f}\nAverage Client Interest Rate: {average_client_interest_rate:.2f}"

        return result





















