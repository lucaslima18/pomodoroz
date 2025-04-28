from prompt_toolkit.document import Document
from questionary import Validator, ValidationError


class BasicDTO:
    @staticmethod
    def int_validator(document: Document) -> bool:
        try:
            int(document.text)
            return True

        except ValueError:
            raise ValidationError(message="Type just Numbers")


class TimeForPomodoroSecDTO(Validator):
    def validate(self, document: Document) -> None:
        BasicDTO.int_validator(document=document)


class PomodoroCountDTO(Validator):
    def validate(self, document: Document) -> None:
        BasicDTO.int_validator(document=document)
