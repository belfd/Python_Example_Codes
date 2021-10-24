
from enum import Enum
class ProgrammingLanguage(Enum):
    PYTHON = "Python"
    JAVA = "Java"
    C = "C"
    JAVASCRIPT = "JavaScript"
    PHP = "Php"

print(f"The language I write is: {ProgrammingLanguage.PYTHON.value}")