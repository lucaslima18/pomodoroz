from prompt_toolkit.document import Document
from questionary import Validator, ValidationError


class BasicDTO:
    @staticmethod
    def int_validator(document: Document) -> bool:
        try:
            int(document.text)
            return True

        except ValueError:
            raise ValidationError(message="Type just Numbers!")


class TimeForPomodoroSecDTO(Validator):
    def max_time(self, document: Document) -> bool:
        if int(document.text) > 100:
            raise ValidationError(message="The number cannot be greater than 10!")
        return True

    def validate(self, document: Document) -> None:
        BasicDTO.int_validator(document=document)
        self.max_time(document=document)


class PomodoroCountDTO(Validator):
    def validate(self, document: Document) -> None:
        BasicDTO.int_validator(document=document)
