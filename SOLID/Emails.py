from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class IProtocol(ABC):

    @abstractmethod
    def format_sender(self, sender):
        pass

    @abstractmethod
    def format_receiver(self, receiver):
        pass


class MyProtocol(IProtocol):

    def format_sender(self, sender):
        return sender

    def format_receiver(self, receiver):
        return receiver


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = self.protocol.format_sender(sender)

    def set_receiver(self, receiver):
        self.__receiver = self.protocol.format_receiver(receiver)

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)



email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
print(email)