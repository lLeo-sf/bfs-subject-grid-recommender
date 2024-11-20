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
        self.other_course_graph: Dict[str, Subject] = {}
        self.optative_credits = 0
        self.optative_credit_goal = 608 if course == Course.SISTEMAS_DE_INFORMACAO else 672
        self.optative_area = optative_area

    def build_graph(self, course_subjects: List[Subject], other_course_subjects: List[Subject]):
        """
        Constrói os grafos de disciplinas do curso principal e do outro curso.
        """
        # Grafo principal com disciplinas do curso selecionado
        self.subjects_graph = {subject.cod: subject for subject in course_subjects}

        # Grafo secundário com disciplinas do outro curso
        self.other_course_graph = {subject.cod: subject for subject in other_course_subjects}

        # Adicionar optativas do curso principal ao grafo principal
        for subject in course_subjects:
            if subject.type == SubjectType.OPTIONAL:
                self.subjects_graph[subject.cod] = subject

        # Adicionar optativas do outro curso ao grafo principal
        for subject in other_course_subjects:
            if subject.type == SubjectType.OPTIONAL and subject.cod not in self.subjects_graph:
                self.subjects_graph[subject.cod] = subject

    def load_completed_subjects(self, subjects: List[Subject]):
        """
        Carrega as disciplinas já concluídas pelo aluno.
        """
        self.completed_subjects = {
            subject.cod for subject in subjects if subject.studentStatus == StudentStatus.COMPLETED
        }

    def is_prerequisite_completed(self, prereq: str) -> bool:
        """
        Verifica se um pré-requisito foi concluído, considerando equivalências
        baseadas no prefixo 'X' para disciplinas equivalentes.
        """
        if prereq in self.completed_subjects:
            return True

        # Verifica equivalência trocando o prefixo 'X' pelo outro curso
        course_prefix = "S" if self.course == Course.SISTEMAS_DE_INFORMACAO else "C"
        equivalent_prereq = course_prefix + prereq[1:]

        return equivalent_prereq in self.completed_subjects

    def calculate_weight(self, subject: Subject, current_semester: int) -> int:
        """
        Calcula o peso de uma disciplina para priorização.
        """
        prereq_weight = len(subject.prerequisites)
        semester_distance = subject.default_semester - current_semester
        semester_weight = abs(semester_distance)
        optative_penalty = 10 if current_semester <= 5 and subject.type == SubjectType.OPTIONAL else 0

        return prereq_weight + semester_weight + optative_penalty

    def find_best_equivalence(self, subject: Subject, current_semester: int) -> Subject:
        """
        Retorna a melhor equivalência entre a disciplina atual e sua equivalente no outro curso.
        """
        if not subject.cod.startswith("X"):
            return subject

        # Identifica a disciplina equivalente na outra grade
        other_prefix = "C" if self.course == Course.SISTEMAS_DE_INFORMACAO else "S"
        equivalent_cod = other_prefix + subject.cod[1:]

        # Verifica se a equivalente existe no grafo do outro curso
        equivalent_subject = self.other_course_graph.get(equivalent_cod)
        if not equivalent_subject:
            return subject

        # Compara pesos para determinar a melhor opção
        current_weight = self.calculate_weight(subject, current_semester)
        equivalent_weight = self.calculate_weight(equivalent_subject, current_semester)

        return subject if current_weight <= equivalent_weight else equivalent_subject

    def find_available_subjects(self, semester_number: int) -> List[Subject]:
        """
        Retorna disciplinas disponíveis para o semestre, respeitando o limite de créditos por semestre.
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
                        # Verificar se o limite de créditos não será ultrapassado
                        if current_credits + subject.credit <= self.max_credits:
                            available_subjects.append(subject)
                            self.completed_subjects.add(subject.cod)
                            current_credits += subject.credit
                            if subject.type == SubjectType.OPTIONAL:
                                self.optative_credits += subject.credit
            return available_subjects

        # Inicializa BFS para disciplinas disponíveis
        for subject in self.subjects_graph.values():
            # Verificar se todos os pré-requisitos estão cumpridos
            if subject.cod not in self.completed_subjects and all(
                self.is_prerequisite_completed(prereq) for prereq in subject.prerequisites
            ):
                # Considerar equivalência para selecionar a melhor disciplina
                best_subject = self.find_best_equivalence(subject, semester_number)
                queue.append(best_subject)

        # Ordenar disciplinas por peso, priorizando obrigatórias e semestres atrasados
        queue = deque(sorted(queue, key=lambda s: self.calculate_weight(s, semester_number)))

        # Explorar disciplinas disponíveis respeitando o limite de créditos
        while queue and current_credits < self.max_credits:
            subject = queue.popleft()

            # Adicionar optativas se obrigatório não está disponível
            if subject.type == SubjectType.OPTIONAL:
                if self.optative_credits >= self.optative_credit_goal:
                    continue
                if self.optative_area and subject.area != self.optative_area:
                    continue

            # Adicionar disciplina se respeitar os limites de créditos
            if current_credits + subject.credit <= self.max_credits:
                available_subjects.append(subject)
                current_credits += subject.credit
                self.completed_subjects.add(subject.cod)

                if subject.type == SubjectType.OPTIONAL:
                    self.optative_credits += subject.credit

        # FORÇAR OPTATIVAS SE O MÍNIMO AINDA NÃO FOI ATINGIDO
        if not self.has_completed_optative_credits():
            additional_optatives = [
                subj for subj in self.subjects_graph.values()
                if subj.type == SubjectType.OPTIONAL and subj.cod not in self.completed_subjects
            ]

            # Adicionar optativas até atingir o mínimo necessário, respeitando o limite de créditos
            for optative in sorted(additional_optatives, key=lambda s: self.calculate_weight(s, semester_number)):
                if self.optative_credits >= self.optative_credit_goal or current_credits + optative.credit > self.max_credits:
                    break
                available_subjects.append(optative)
                self.completed_subjects.add(optative.cod)
                self.optative_credits += optative.credit
                current_credits += optative.credit

        return available_subjects



    def update_completed_subjects(self, subjects: List[Subject]):
        """
        Atualiza a lista de disciplinas concluídas após cada semestre.
        """
        for subject in subjects:
            if subject.cod not in self.completed_subjects:
                self.completed_subjects.add(subject.cod)
                if subject.type == SubjectType.OPTIONAL:
                    self.optative_credits += subject.credit

    def get_fixed_first_semester_subjects(self) -> List[str]:
        """
        Retorna as disciplinas fixas do primeiro semestre.
        """
        if self.course == Course.SISTEMAS_DE_INFORMACAO:
            return ["XDES01", "SAHC04", "SAHC05", "MAT00A", "IEPG01", "IEPG22"]
        elif self.course == Course.CIENCIA_DA_COMPUTACAO:
            return ["XDES01", "CRSC03", "MAT00A", "XMACO01", "CAHC04"]
        return []

    def has_completed_optative_credits(self) -> bool:
        """
        Verifica se o aluno completou o mínimo de créditos optativos necessários.
        """
        return self.optative_credits >= self.optative_credit_goal
