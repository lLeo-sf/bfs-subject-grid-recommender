from typing import List, Dict, Set
from collections import deque
from grids.sin import subjects as sin_subjects
from grids.cco import subjects as cco_subjects
from data_structures.subject import Area, StudentStatus, Subject, SubjectType
from data_structures.course import Course

class BfsSubjectSelection:
    def __init__(self, course: Course, max_credits: int = 400, optative_area: Area = None):
        self.course = course
        self.max_credits = max_credits
        self.completed_subjects: Set[str] = set()
        self.subjects_graph: Dict[str, Subject] = {}
        self.equivalents: Dict[str, str] = {}
        self.optative_credits = 0
        self.optative_credit_goal = 608 if course == Course.SISTEMAS_DE_INFORMACAO else 672
        self.optative_area = optative_area

    def build_graph(self, subjects: List[Subject]):
        """Cria o grafo de disciplinas e mapeia equivalências."""
        self.subjects_graph = {subject.cod: subject for subject in subjects}

        for subject in subjects:
            if subject.cod.startswith("X"):
                self.equivalents[subject.cod] = subject.cod

            for prereq in subject.prerequisites:
                if prereq not in self.subjects_graph and prereq not in self.equivalents:
                    raise ValueError(f"Pré-requisito desconhecido: {prereq} para a disciplina {subject.cod} ({subject.name})")

    def load_completed_subjects(self, subjects: List[Subject]):
        """Carrega as disciplinas já cursadas pelo aluno."""
        self.completed_subjects = {
            subject.cod for subject in subjects if subject.studentStatus == StudentStatus.COMPLETED
        }

    def update_completed_subjects(self, subjects: List[Subject]):
        """Atualiza a lista de disciplinas concluídas após cada semestre."""
        for subject in subjects:
            if subject.cod not in self.completed_subjects:
                self.completed_subjects.add(subject.cod)
                if subject.type == SubjectType.OPTIONAL:
                    self.optative_credits += subject.credit

    def get_fixed_first_semester_subjects(self) -> List[str]:
        """Retorna as disciplinas fixas para o primeiro semestre baseado no curso."""
        if self.course == Course.SISTEMAS_DE_INFORMACAO:
            return ["XDES01", "SAHC04", "SAHC05", "MAT00A", "IEPG01", "IEPG22"]
        elif self.course == Course.CIENCIA_DA_COMPUTACAO:
            return ["XDES01", "CRSC03", "MAT00A", "XMACO01", "CAHC04"]
        return []

    def find_available_subjects(self, semester_number: int) -> List[Subject]:
        """Retorna disciplinas disponíveis para o semestre, priorizando a área de interesse."""
        queue = deque()
        available_subjects = []
        current_credits = 0

        # Adiciona disciplinas fixas no primeiro semestre
        if semester_number == 1:
            fixed_subjects = self.get_fixed_first_semester_subjects()
            for subject_cod in fixed_subjects:
                if subject_cod in self.subjects_graph:
                    subject = self.subjects_graph[subject_cod]
                    if subject.cod not in self.completed_subjects:
                        available_subjects.append(subject)
                        self.completed_subjects.add(subject.cod)
                        current_credits += subject.credit
                        if subject.type == SubjectType.OPTIONAL:
                            self.optative_credits += subject.credit
            return available_subjects

        # Inicializa BFS para encontrar disciplinas disponíveis com base nos pré-requisitos
        for subject in self.subjects_graph.values():
            if subject.studentStatus != StudentStatus.COMPLETED and all(
                prereq in self.completed_subjects for prereq in subject.prerequisites
            ):
                queue.append(subject)

        # Seleciona disciplinas optativas priorizando a área de interesse
        while queue and current_credits < self.max_credits:
            subject = queue.popleft()
            if subject.default_semester % 2 == semester_number % 2 and subject.cod not in self.completed_subjects:
                if current_credits + subject.credit <= self.max_credits:
                    if subject.type == SubjectType.OPTIONAL:
                        if self.optative_area is None or subject.area == self.optative_area:
                            available_subjects.append(subject)
                            current_credits += subject.credit
                            self.completed_subjects.add(subject.cod)
                            self.optative_credits += subject.credit
                    else:
                        available_subjects.append(subject)
                        current_credits += subject.credit
                        self.completed_subjects.add(subject.cod)
        return available_subjects

    def has_completed_optative_credits(self) -> bool:
        """Verifica se o aluno completou o mínimo de créditos optativos necessários."""
        return self.optative_credits >= self.optative_credit_goal
