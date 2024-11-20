from typing import List

from matplotlib import pyplot as plt
import pandas as pd
from data_structures.course import Course
from data_structures.subject import Area, StudentStatus, Subject, SubjectType
from bfs_subject_selection.selection import BfsSubjectSelection
from grids.sin import subjects as sin_subjects
from grids.cco import subjects as cco_subjects
import networkx as nx

completedSubject1: List[Subject] = [
    Subject(StudentStatus.COMPLETED, "XDES01", "Fundamentos da Programação", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.COMPLETED, "SAHC04", "Projeto Integrado", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.COMPLETED, "SAHC05", "Fundamentos de Sistemas da Informação", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.COMPLETED, "MAT00A", "Cálculo A", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.COMPLETED, "IEPG01", "Empreendedorismo e Inovação", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, type=SubjectType.REQUIRED, credit=48, prerequisites=[]),
    Subject(StudentStatus.COMPLETED, "IEPG22", "Administração Aplicada", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, type=SubjectType.REQUIRED, credit=32, prerequisites=[]),
]

completedSubject2: List[Subject] = [
    Subject(StudentStatus.COMPLETED, "XDES02", "Programação Orientada a Objetos", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 2, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES01"]),
    Subject(StudentStatus.COMPLETED, "XDES04", "Engenharia de Software I", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 2, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.COMPLETED, "STCO01", "Algoritmos e Programação I", Area.COMPUTATION_THEORY, 2, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES01"]),
    Subject(StudentStatus.COMPLETED, "XMAC01", "Matemática Discreta",area=Area.MATHEMATICS_OF_COMPUTATION,default_semester=1,type=SubjectType.REQUIRED,credit=64,prerequisites=[]),
    Subject(StudentStatus.COMPLETED, "IEPG04", "Mapeamento de Processos", Area.MANAGEMENT_AND_ADMINISTRATION, 2, type=SubjectType.REQUIRED, credit=32, prerequisites=[]),
]

completedSubject3: List[Subject] = [
    Subject(StudentStatus.COMPLETED, "XDES03", "Programação Web", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 3, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES02"]),
    Subject(StudentStatus.COMPLETED , "STCO02", "Algoritmos e Programação II", Area.COMPUTATION_THEORY, 3, type=SubjectType.REQUIRED, credit=64, prerequisites=["STCO01"]),
    Subject(StudentStatus.COMPLETED , "SDES05", "Engenharia de Software II", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 3, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "ECN001", "Economia", Area.MANAGEMENT_AND_ADMINISTRATION, 3, type=SubjectType.REQUIRED, credit=48, prerequisites=[]),
    Subject(StudentStatus.PENDING, "SRSC03", "Organização e Arquitetura de Computadores", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 3, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
]


# Selecionar o curso e a área de interesse para as optativas
course = Course.SISTEMAS_DE_INFORMACAO
optative_area = Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING

# Instância do algoritmo
selection = BfsSubjectSelection(course=Course.SISTEMAS_DE_INFORMACAO, optative_area=Area.DATA_PERSISTENCE_AND_ANALYSIS)

# Construir grafo com todas as disciplinas
selection.build_graph(course_subjects=sin_subjects, other_course_subjects=cco_subjects)

# Disciplinas já concluídas pelo aluno (início sem nenhuma concluída)
completed_subjects = []

# Carregar disciplinas concluídas
selection.load_completed_subjects(completed_subjects)

# Variáveis de controle
current_semester = 1
max_semesters = 12  # Limite de semestres para evitar loops

# Loop para sugerir disciplinas até concluir todas as obrigatórias e optativas
while True:
    print(f"\n--- Sugestão para o Semestre {current_semester} ---")

    # Obter disciplinas disponíveis para o semestre atual
    available_subjects = selection.find_available_subjects(semester_number=current_semester)

    # Exibir disciplinas sugeridas
    if available_subjects:
        for subject in available_subjects:
            print(f"- {subject.cod}: {subject.name} ({subject.credit} créditos)")
    else:
        print("Nenhuma disciplina disponível para este semestre.")

    # Atualizar disciplinas concluídas
    selection.update_completed_subjects(available_subjects)

    # Verificar se todas as disciplinas obrigatórias e optativas foram concluídas
    mandatory_completed = all(
        subject.cod in selection.completed_subjects for subject in sin_subjects if subject.type == SubjectType.REQUIRED
    )
    optative_completed = selection.has_completed_optative_credits()

    if mandatory_completed:
        print("\nTodas as disciplinas obrigatórias foram concluídas.")

    if optative_completed:
        print("\nTodas as disciplinas optativas foram concluídas.")

    if mandatory_completed and optative_completed: 
        break

    # Incrementar semestre
    current_semester += 1

    # Verificar se o limite de semestres foi atingido
    if current_semester > max_semesters:
        print("\nLimite de semestres atingido. Interrompendo o planejamento.")
        break
