from typing import List

from matplotlib import pyplot as plt
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
    Subject(StudentStatus.PENDING, "XMAC01", "Matemática Discreta",area=Area.MATHEMATICS_OF_COMPUTATION,default_semester=1,type=SubjectType.REQUIRED,credit=64,prerequisites=[]),
    Subject(StudentStatus.PENDING, "IEPG04", "Mapeamento de Processos", Area.MANAGEMENT_AND_ADMINISTRATION, 2, type=SubjectType.REQUIRED, credit=32, prerequisites=[]),
]


# Selecionar o curso e a área de interesse para as optativas
course = Course.SISTEMAS_DE_INFORMACAO
optative_area = Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING

# Carregar todas as disciplinas disponíveis (SIN + CCO)
all_subjects = sin_subjects + cco_subjects

# Criar uma instância de SubjectSelection para o curso selecionado
selection = BfsSubjectSelection(course, optative_area=optative_area)
selection.build_graph(all_subjects)

# Disciplinas já concluídas
completed_subjects = []

selection.load_completed_subjects(completed_subjects)

# Recomendação de disciplinas por semestre
semester_number = 1
recommended_subjects_by_semester = {}

while True:
    # Encontrar disciplinas disponíveis para o semestre atual
    available_subjects = selection.find_available_subjects(semester_number)

    # Se não houver disciplinas disponíveis, encerrar o loop
    if not available_subjects:
        break

    # Adicionar as disciplinas recomendadas ao dicionário
    recommended_subjects_by_semester[semester_number] = available_subjects

    # Atualizar disciplinas concluídas
    for subject in available_subjects:
        subject.studentStatus = StudentStatus.COMPLETED
        completed_subjects.append(subject)
    
    selection.update_completed_subjects(available_subjects)

    # Verificar se todas as obrigatórias e optativas foram concluídas
    if all(
        subj.cod in selection.completed_subjects for subj in all_subjects if subj.type == SubjectType.REQUIRED
    ) and selection.has_completed_optative_credits():
        break

    # Passar para o próximo semestre
    semester_number += 1
    selection.build_graph(all_subjects)

# Imprimir a recomendação de disciplinas por semestre
print("\nRecomendações de Disciplinas por Semestre:")
for semester, subjects in recommended_subjects_by_semester.items():
    print(f"\nSemestre {semester}:")
    for subject in subjects:
        print(f"  - {subject.cod}: {subject.name} ({subject.credit} créditos)")
