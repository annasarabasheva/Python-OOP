class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return self.min_length <= len(name)

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        arguments = email.split('@')
        name = arguments[0]
        other_args = arguments[1].split('.')
        mail = other_args[0]
        domain = other_args[1]
        if self.__is_domain_valid(domain) and self.__is_mail_valid(mail) and self.__is_name_valid(name):
            return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
