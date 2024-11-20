from enum import Enum
from typing import Dict, List

class Area(Enum):
    SOFTWARE_DEVELOPMENT_AND_ENGINEERING = "Software Development and Engineering"
    DATA_PERSISTENCE_AND_ANALYSIS = "Data Persistence and Analysis"
    COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION = "Computational Methodologies and Optimization"
    COMPUTER_NETWORKS_AND_SYSTEMS = "Computer Networks and Systems"
    COMPUTATION_THEORY = "Computation Theory"
    MATHEMATICS_OF_COMPUTATION = "Mathematics of Computation"
    MANAGEMENT_AND_ADMINISTRATION = "Management and Administration"
    HUMAN_ASPECTS_IN_COMPUTING = "Human Aspects in Computing"
    
class StudentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"

class SubjectType(Enum):
    REQUIRED = "Required"
    OPTIONAL = "Optional"

class Subject:
    def __init__(self, studentStatus: StudentStatus, cod: str, name: str, area: Area, default_semester: int, 
                 type: SubjectType, credit: int, prerequisites: List[str]):
        self.studentStatus = studentStatus
        self.cod = cod
        self.name = name
        self.area = area
        self.default_semester = default_semester
        self.type = type
        self.credit = credit
        self.prerequisites = prerequisites