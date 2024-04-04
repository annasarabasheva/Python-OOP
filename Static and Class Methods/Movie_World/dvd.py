import datetime

class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month_as_string, year = date.split('.')
        monthinteger = int(month_as_string)
        month = datetime.date(1900, monthinteger, 1).strftime('%B')

        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self):
        result = ''
        if self.is_rented:
            result = 'rented'
        else:
            result = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {result}"