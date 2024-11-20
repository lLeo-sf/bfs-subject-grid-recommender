from typing import List
from data_structures.subject import StudentStatus, Subject, Area, SubjectType
import json

subjects: List[Subject] = [
    Subject(StudentStatus.PENDING, "XDES01", "Fundamentos da Programação", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "XDES02", "Programação Orientada a Objetos", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 2, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES01"]),
    Subject(StudentStatus.PENDING, "XDES03", "Programação Web", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 3, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES02"]),
    Subject(StudentStatus.PENDING, "XDES04", "Engenharia de Software I", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 2, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "SDES05", "Engenharia de Software II", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 3, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "SDES06", "Gerência de Projetos de Software", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 6, type=SubjectType.REQUIRED, credit=64, prerequisites=["SDES05"]),
    Subject(StudentStatus.PENDING, "SDES07", "Desenvolvimento de Sistemas Web", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 7, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES03", "XDES04", "XPAD01"]),
    
    Subject(StudentStatus.PENDING, "XPAD01", "Banco de Dados I", Area.DATA_PERSISTENCE_AND_ANALYSIS, 4, type=SubjectType.REQUIRED, credit=64, prerequisites=["STCO02"]),
    Subject(StudentStatus.PENDING, "SPAD02", "Banco de Dados II", Area.DATA_PERSISTENCE_AND_ANALYSIS, 5, type=SubjectType.REQUIRED, credit=64, prerequisites=["XPAD01"]),
    Subject(StudentStatus.PENDING, "SPAD03", "Introdução à Análise de Dados", Area.DATA_PERSISTENCE_AND_ANALYSIS, 5, type=SubjectType.REQUIRED, credit=64, prerequisites=["XMAC02"]),
    
    Subject(StudentStatus.PENDING, "XMCO01", "Inteligência Artificial", Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 6, type=SubjectType.REQUIRED, credit=64, prerequisites=["XMAC02"]),
    
    Subject(StudentStatus.PENDING, "XRSC01", "Redes de Computadores", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 5, type=SubjectType.REQUIRED, credit=64, prerequisites=["SRSC02"]),
    Subject(StudentStatus.PENDING, "SRSC02", "Sistemas Operacionais", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 4, type=SubjectType.REQUIRED, credit=64, prerequisites=["SRSC03", "SRSC03"]),
    Subject(StudentStatus.PENDING, "SRSC03", "Organização e Arquitetura de Computadores", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 3, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    
    Subject(StudentStatus.PENDING, "IEPG04", "Mapeamento de Processos", Area.MANAGEMENT_AND_ADMINISTRATION, 2, type=SubjectType.REQUIRED, credit=32, prerequisites=[]),
    Subject(StudentStatus.PENDING, "STCO01", "Algoritmos e Programação I", Area.COMPUTATION_THEORY, 2, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES01"]),
    Subject(StudentStatus.PENDING, "STCO02", "Algoritmos e Programação II", Area.COMPUTATION_THEORY, 3, type=SubjectType.REQUIRED, credit=64, prerequisites=["STCO01"]),
    
    Subject(StudentStatus.PENDING, "MAT00A", "Cálculo A", Area.MATHEMATICS_OF_COMPUTATION, 1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "XMAC01", "Matemática Discreta", Area.MATHEMATICS_OF_COMPUTATION, 2, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "XMAC02", "Métodos Matemáticos para a Análise de Dados", Area.MATHEMATICS_OF_COMPUTATION, 4, type=SubjectType.REQUIRED, credit=64, prerequisites=["MAT00A", "XMAC01", "STCO01", "STCO02"]),
    Subject(StudentStatus.PENDING, "SMAC03", "Grafos", Area.MATHEMATICS_OF_COMPUTATION, 4, type=SubjectType.REQUIRED, credit=64, prerequisites=["STCO02"]),
    
    Subject(StudentStatus.PENDING, "IEPG14", "Comportamentos Organizacional I", Area.MANAGEMENT_AND_ADMINISTRATION, 4, type=SubjectType.REQUIRED, credit=32, prerequisites=[]),
    Subject(StudentStatus.PENDING, "ECN001", "Economia", Area.MANAGEMENT_AND_ADMINISTRATION, 3, type=SubjectType.REQUIRED, credit=48, prerequisites=[]),
    Subject(StudentStatus.PENDING, "IEPG01", "Empreendedorismo e Inovação", Area.MANAGEMENT_AND_ADMINISTRATION, 1, type=SubjectType.REQUIRED, credit=48, prerequisites=[]),
    Subject(StudentStatus.PENDING, "ADM03E", "Empreendedorismo Tecnológico", Area.MANAGEMENT_AND_ADMINISTRATION, 8, type=SubjectType.REQUIRED, credit=48, prerequisites=["IEPG01"]),
    Subject(StudentStatus.PENDING, "IEPG10", "Engenharia Econômica", Area.MANAGEMENT_AND_ADMINISTRATION, 6, type=SubjectType.REQUIRED, credit=48, prerequisites=[]),
    Subject(StudentStatus.PENDING, "ADM51E", "Gestão do Conhecimento", Area.MANAGEMENT_AND_ADMINISTRATION, 5, type=SubjectType.REQUIRED, credit=48, prerequisites=[]),
    Subject(StudentStatus.PENDING, "SADG01", "Gestão e Governança de TI", Area.MANAGEMENT_AND_ADMINISTRATION, 9, type=SubjectType.REQUIRED, credit=64, prerequisites=["IEPG22"]),
    Subject(StudentStatus.PENDING, "IEPG22", "Administração Aplicada", Area.MANAGEMENT_AND_ADMINISTRATION, 1, type=SubjectType.REQUIRED, credit=32, prerequisites=[]),

    Subject(StudentStatus.PENDING, "XAHC01", "Computação e Sociedade", Area.HUMAN_ASPECTS_IN_COMPUTING, 8, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "XAHC02", "Interação Humano-Computador", Area.HUMAN_ASPECTS_IN_COMPUTING, 7, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES03"]),
    Subject(StudentStatus.PENDING, "XAHC03", "Metodologia Científica", Area.HUMAN_ASPECTS_IN_COMPUTING, 8, type=SubjectType.REQUIRED, credit=64, prerequisites=["XAHC02"]),
    Subject(StudentStatus.PENDING, "SAHC04", "Projeto Integrado", Area.HUMAN_ASPECTS_IN_COMPUTING, 1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "SAHC05", "Fundamentos de Sistemas da Informação", Area.HUMAN_ASPECTS_IN_COMPUTING, 1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    
    Subject(StudentStatus.PENDING, "XDES08", "Arquitetura de Software", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 7, type=SubjectType.OPTIONAL, credit=64, prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "XDES09", "Padrões de Projeto", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 6, type=SubjectType.OPTIONAL, credit=64, prerequisites=["XDES03", "XDES04",]),
    Subject(StudentStatus.PENDING, 'XDES10', 'Engenharia de Software Experimental', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 6, SubjectType.OPTIONAL, 64, ["XDES04"]),
    Subject(StudentStatus.PENDING, 'XDES11', 'Tópicos em DES I', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 7, SubjectType.OPTIONAL, 64, ["XDES04"]),
    Subject(StudentStatus.PENDING, 'XDES12', 'Tópicos em DES II', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 7, SubjectType.OPTIONAL, 64, ["XDES04"]),
    Subject(StudentStatus.PENDING, 'XDES13', 'Desenvolvimento de Jogos', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 6, SubjectType.OPTIONAL, 64, ["XDES01"]),
    Subject(StudentStatus.PENDING, 'XDES14', 'Desenvolvimento para Dispositivos Móveis', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 7, SubjectType.OPTIONAL, 64, ["XDES03"]),
    Subject(StudentStatus.PENDING, 'XDES15', 'Reutilização de Software', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 7, SubjectType.OPTIONAL, 64, ["SDES05", "XDES02", "XDES09"]),
    
    Subject(StudentStatus.PENDING, 'ECOX21', 'Maratona de programação I', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 6, SubjectType.OPTIONAL, 48, ["STCO01"]),
    Subject(StudentStatus.PENDING, 'ECOX22', 'Maratona de programação II', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 7, SubjectType.OPTIONAL, 48, ["ECOX21"]),
    
    Subject(StudentStatus.PENDING, 'XPAD04', 'Bancos de Dados NoSQL', Area.DATA_PERSISTENCE_AND_ANALYSIS, 6, SubjectType.OPTIONAL, 64, [ "XPAD01"]),
    Subject(StudentStatus.PENDING, 'SPAD05', 'Análise de Dados Geoespaciais', Area.DATA_PERSISTENCE_AND_ANALYSIS, 7, SubjectType.OPTIONAL, 64, ["SPAD02", "XDES03"]),
    Subject(StudentStatus.PENDING, 'SPAD06', 'Mineração de Dados', Area.DATA_PERSISTENCE_AND_ANALYSIS, 6, SubjectType.OPTIONAL, 64, ["SPAD03"]),
    Subject(StudentStatus.PENDING, 'XPAD08', 'Armazém de Dados', Area.DATA_PERSISTENCE_AND_ANALYSIS, 7, SubjectType.OPTIONAL, 64, ["SPAD03"]),

    Subject(StudentStatus.PENDING, 'XMCO03', 'Tópicos em PAD', Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 6, SubjectType.OPTIONAL, 64, ["XPAD01", "SPAD03"]),
    Subject(StudentStatus.PENDING, 'XMCO03', 'Métodos Exatos', Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 6, SubjectType.OPTIONAL, 64, ["XMAC02", "SMAC03"]),
    Subject(StudentStatus.PENDING, 'XMCO04', 'Metaheurísticas', Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 7, SubjectType.OPTIONAL, 64, ["XMAC02", "SMAC03"]),
    Subject(StudentStatus.PENDING, 'XMCO05', 'Tópicos em MCO', Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 7, SubjectType.OPTIONAL, 64, ["XMAC02", "SMAC03"]),
    
    Subject(StudentStatus.PENDING, 'CRSC05', 'Sistemas Embarcados', Area.COMPUTER_NETWORKS_AND_SYSTEMS, 6, SubjectType.OPTIONAL, 64, ["SRSC02"]),
    Subject(StudentStatus.PENDING, 'XRSC06', 'Auditoria e Segurança de SI', Area.COMPUTER_NETWORKS_AND_SYSTEMS, 7, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, 'XRSC07', 'Computação em Nuvem', Area.COMPUTER_NETWORKS_AND_SYSTEMS, 6, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, 'XRSC08', 'Programação Paralela', Area.COMPUTER_NETWORKS_AND_SYSTEMS, 7, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, 'XRSC09', 'Sistemas Distribuídos', Area.COMPUTER_NETWORKS_AND_SYSTEMS, 6, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, 'XRSC10', 'Tópicos em RSC', Area.COMPUTER_NETWORKS_AND_SYSTEMS, 7, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    
    Subject(StudentStatus.PENDING, 'ECOS04', 'Simulação e Avaliação de Desempenho', Area.COMPUTER_NETWORKS_AND_SYSTEMS, 8, SubjectType.OPTIONAL, 32, ["XRSC09"]),
    
    Subject(StudentStatus.PENDING, 'SADG02', 'Economia da Informação', Area.MANAGEMENT_AND_ADMINISTRATION, 7, SubjectType.OPTIONAL, 64, []),
    Subject(StudentStatus.PENDING, 'XADG03', 'Tópicos em ADG', Area.MANAGEMENT_AND_ADMINISTRATION, 7, SubjectType.OPTIONAL, 64, []),
    Subject(StudentStatus.PENDING, 'ADM01F', 'Finanças: Conceitos e Aplicações', Area.MANAGEMENT_AND_ADMINISTRATION, 7, SubjectType.OPTIONAL, 32, []),
    Subject(StudentStatus.PENDING, 'IEPG05', 'Finanças para Executivos', Area.MANAGEMENT_AND_ADMINISTRATION, 6, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, 'IEPG13', 'Custos Empresariais', Area.MANAGEMENT_AND_ADMINISTRATION, 7, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, 'IEPG15', 'Logística e Gestão da Cadeia de Suprimentos', Area.MANAGEMENT_AND_ADMINISTRATION, 6, SubjectType.OPTIONAL, 32, []),
    
    Subject(StudentStatus.PENDING, 'XAHC06', 'Tópicos em AHC', Area.HUMAN_ASPECTS_IN_COMPUTING, 8, SubjectType.OPTIONAL, 64, []),
    Subject(StudentStatus.PENDING, 'IEPG21', 'Ciências Humanas e Sociais', Area.HUMAN_ASPECTS_IN_COMPUTING, 6, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, 'ADM08H', 'Psicologia: As relações Indivíduo-Grupo', Area.HUMAN_ASPECTS_IN_COMPUTING, 7, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, 'ADM52H', 'Comportamento Organizacional II', Area.HUMAN_ASPECTS_IN_COMPUTING, 7, SubjectType.OPTIONAL, 32, []),
    Subject(StudentStatus.PENDING, 'ADM54H', 'Gestão de Carreira', Area.HUMAN_ASPECTS_IN_COMPUTING, 6, SubjectType.OPTIONAL, 32, []),
    Subject(StudentStatus.PENDING, 'ADM58H', 'Psicologia Organizacional e do Trabalho', Area.HUMAN_ASPECTS_IN_COMPUTING, 6, SubjectType.OPTIONAL, 32, []),
    Subject(StudentStatus.PENDING, 'ADM51H', 'Ciências, Tecnologias e Organizações', Area.HUMAN_ASPECTS_IN_COMPUTING, 7, SubjectType.OPTIONAL, 48, []),

    Subject(StudentStatus.PENDING, 'TCC1', 'TCC1', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 8, SubjectType.REQUIRED, 144, []),
    Subject(StudentStatus.PENDING, 'TCC2', 'TCC2', Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 9, SubjectType.REQUIRED, 216, ["TCC1"])
]


