from typing import List, Dict, Set
from collections import deque
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
            # Adicionar equivalências para disciplinas com prefixo "X"
            if subject.cod.startswith("X"):
                self.equivalents[subject.cod] = subject.cod

            # Verificar existência de pré-requisitos no grafo ou nas equivalências
            for prereq in subject.prerequisites:
                if prereq not in self.subjects_graph and prereq not in self.equivalents:
                    raise ValueError(f"Pré-requisito desconhecido: {prereq} para a disciplina {subject.cod} ({subject.name})")

    def load_completed_subjects(self, subjects: List[Subject]):
        self.completed_subjects = {
            subject.cod for subject in subjects if subject.studentStatus == StudentStatus.COMPLETED
        }

    def is_prerequisite_completed(self, prereq: str) -> bool:
        """
        Verifica se um pré-requisito foi concluído, considerando a troca da primeira letra 
        para a grade do curso atual (S ou C).
        """
        # Curso atual define o prefixo
        course_prefix = "S" if self.course == Course.SISTEMAS_DE_INFORMACAO else "C"
        equivalent_prereq = course_prefix + prereq[1:] 

        # Verifica se o pré-requisito ou seu equivalente foi concluído
        return prereq in self.completed_subjects or equivalent_prereq in self.completed_subjects


    def calculate_weight(self, subject: Subject, current_semester: int) -> int:
        """
        Calcula o peso de uma disciplina para priorização.
        """
        prereq_weight = len(subject.prerequisites)
        semester_distance = subject.default_semester - current_semester
        semester_weight = abs(semester_distance)
        optative_penalty = 10 if current_semester <= 5 and subject.type == SubjectType.OPTIONAL else 0

        return prereq_weight + semester_weight + optative_penalty

    def find_available_subjects(self, semester_number: int) -> List[Subject]:
        """
        Retorna disciplinas disponíveis para o semestre, priorizando obrigatórias até completar todas.
        """
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

        # Inicializa BFS para disciplinas disponíveis
        for subject in self.subjects_graph.values():
            # Ignorar disciplinas fora do escopo do curso atual
            if self.course == Course.SISTEMAS_DE_INFORMACAO and subject.cod.startswith("C"):
                continue
            if self.course == Course.CIENCIA_DA_COMPUTACAO and subject.cod.startswith("S"):
                continue

            # Verificar se todos os pré-requisitos (ou equivalentes concluídos) estão cumpridos
            if subject.cod not in self.completed_subjects and all(
                self.is_prerequisite_completed(prereq) for prereq in subject.prerequisites
            ):
                queue.append(subject)

        # Ordenar disciplinas por peso, priorizando obrigatórias e semestres atrasados
        queue = deque(sorted(queue, key=lambda s: self.calculate_weight(s, semester_number)))

        # Explorar disciplinas disponíveis
        while queue and current_credits < self.max_credits:
            subject = queue.popleft()

            # Garantir que obrigatórias sejam priorizadas antes de optativas
            if subject.type == SubjectType.OPTIONAL:
                # Verificar limite de créditos optativos
                if self.optative_credits >= self.optative_credit_goal:
                    continue
                # Optativas são recomendadas somente após as obrigatórias (até o 5º semestre)
                if semester_number <= 5:
                    continue
                # Verificar a área preferida para optativas
                if self.optative_area and subject.area != self.optative_area:
                    continue

            # Adicionar disciplina se respeitar os limites de créditos
            if current_credits + subject.credit <= self.max_credits:
                available_subjects.append(subject)
                current_credits += subject.credit
                self.completed_subjects.add(subject.cod)

                if subject.type == SubjectType.OPTIONAL:
                    self.optative_credits += subject.credit

        return available_subjects

    def update_completed_subjects(self, subjects: List[Subject]):
        for subject in subjects:
            if subject.cod not in self.completed_subjects:
                self.completed_subjects.add(subject.cod)
                if subject.type == SubjectType.OPTIONAL:
                    self.optative_credits += subject.credit

    def get_fixed_first_semester_subjects(self) -> List[str]:
        if self.course == Course.SISTEMAS_DE_INFORMACAO:
            return ["XDES01", "SAHC04", "SAHC05", "MAT00A", "IEPG01", "IEPG22"]
        elif self.course == Course.CIENCIA_DA_COMPUTACAO:
            return ["XDES01", "CRSC03", "MAT00A", "XMACO01", "CAHC04"]
        return []

    def has_completed_optative_credits(self) -> bool:
        return self.optative_credits >= self.optative_credit_goal
