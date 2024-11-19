




from typing import List

from data_structures.subject import Area, StudentStatus, Subject, SubjectType


subjects: List[Subject] = [
    Subject(StudentStatus.PENDING, "XDES01", "Fundamentos de Programação", area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, default_semester=1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "XDES02", "Programação Orientada a Objetos", area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, default_semester=3, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES01"]),
    Subject(StudentStatus.PENDING, "XDES03", "Programação Web", area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, default_semester=4, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES02"]),
    Subject(StudentStatus.PENDING, "XDES04", "Engenharia de Software I", area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, default_semester=3, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "CDES05", "Programação Lógica e Funcional", area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, default_semester=2, type=SubjectType.REQUIRED, credit=64, prerequisites=["XMAC01"]),
    Subject(StudentStatus.PENDING, "XPAD01", "Banco de Dados I", area=Area.DATA_PERSISTENCE_AND_ANALYSIS, default_semester=5, type=SubjectType.REQUIRED, credit=64, prerequisites=["CTCO02"]),
    Subject(StudentStatus.PENDING, "XMCO01", "Inteligência Artificial", area=Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, default_semester=5, type=SubjectType.REQUIRED, credit=64, prerequisites=["XMAC02"]),
    Subject(StudentStatus.PENDING, "CMCO05", "Introdução à Computação Visual", area=Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, default_semester=5, type=SubjectType.REQUIRED, credit=64, prerequisites=["XMAC02", "XDES02"]),
    Subject(StudentStatus.PENDING, "XRSC01", "Redes de Computadores", area=Area.COMPUTER_NETWORKS_AND_SYSTEMS, default_semester=4, type=SubjectType.REQUIRED, credit=64, prerequisites=["CRSC02"]),
    Subject(StudentStatus.PENDING, "CRSC02", "Sistemas Operacionais", area=Area.COMPUTER_NETWORKS_AND_SYSTEMS, default_semester=3, type=SubjectType.REQUIRED, credit=64, prerequisites=["CTCO01", "CRSC04"]),
    Subject(StudentStatus.PENDING, "CRSC03", "Arquitetura de Computadores I", area=Area.COMPUTER_NETWORKS_AND_SYSTEMS, default_semester=1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "CRSC04", "Arquitetura de Computadores II", area=Area.COMPUTER_NETWORKS_AND_SYSTEMS, default_semester=2, type=SubjectType.REQUIRED, credit=64, prerequisites=["CRSC03"]),
    Subject(StudentStatus.PENDING, "CRSC05", "Sistemas Embarcados", area=Area.COMPUTER_NETWORKS_AND_SYSTEMS, default_semester=4, type=SubjectType.REQUIRED, credit=64, prerequisites=["CRSC02"]),
    Subject(StudentStatus.PENDING, "CTCO01", "Algoritmos e Estruturas de Dados I", area=Area.COMPUTATION_THEORY, default_semester=2, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES01"]),
    Subject(StudentStatus.PENDING, "CTCO02", "Algoritmos e Estruturas de Dados II", area=Area.COMPUTATION_THEORY, default_semester=3, type=SubjectType.REQUIRED, credit=64, prerequisites=["CTCO01"]),
    Subject(StudentStatus.PENDING, "CTCO03", "Análise e Projeto Orientados a Objeto", area=Area.COMPUTATION_THEORY, default_semester=5, type=SubjectType.REQUIRED, credit=64, prerequisites=["XDES02"]),
    Subject(StudentStatus.PENDING, "CTCO04", "Projeto e Análise de Algoritmos", area=Area.COMPUTATION_THEORY, default_semester=4, type=SubjectType.REQUIRED, credit=64, prerequisites=["CTCO02"]),
    Subject(StudentStatus.PENDING, "CTCO05", "Teoria da Computação", area=Area.COMPUTATION_THEORY, default_semester=5, type=SubjectType.REQUIRED, credit=64, prerequisites=["CTCO04", "CDES05"]),
    Subject(StudentStatus.PENDING, "CTCO06", "Compiladores", area=Area.COMPUTATION_THEORY, default_semester=6, type=SubjectType.REQUIRED, credit=64, prerequisites=["CTCO05"]),
    Subject(StudentStatus.PENDING, "MAT00A", "Cálculo A", area=Area.MATHEMATICS_OF_COMPUTATION, default_semester=1, type=SubjectType.REQUIRED, credit=64, prerequisites=[]),
    Subject(StudentStatus.PENDING, "MAT00B", "Cálculo B",area=Area.MATHEMATICS_OF_COMPUTATION,default_semester=2,type=SubjectType.REQUIRED,credit=64,prerequisites=["MAT00A"]),
    Subject(StudentStatus.PENDING, "XMAC01", "Matemática Discreta",area=Area.MATHEMATICS_OF_COMPUTATION,default_semester=1,type=SubjectType.REQUIRED,credit=64,prerequisites=[]),
    Subject(StudentStatus.PENDING, "XMAC02", "Métodos Matemáticos para Análise de Dados",area=Area.MATHEMATICS_OF_COMPUTATION,default_semester=3,type=SubjectType.REQUIRED,credit=64,prerequisites=["MAT00A", "CTCO01", "XMAC01"]),
    Subject(StudentStatus.PENDING, "CMAC03", "Algoritmos em Grafos",area=Area.MATHEMATICS_OF_COMPUTATION,default_semester=3,type=SubjectType.REQUIRED,credit=64,prerequisites=["CTCO01"]),
    Subject(StudentStatus.PENDING, "CMAC04", "Modelagem Computacional",area=Area.MATHEMATICS_OF_COMPUTATION,default_semester=2,type=SubjectType.REQUIRED,credit=64,prerequisites=["MAT00A"]),
    Subject(StudentStatus.PENDING, "CMAC05", "Cálculo Numérico para Computação",area=Area.MATHEMATICS_OF_COMPUTATION,default_semester=4,type=SubjectType.REQUIRED,credit=64,prerequisites=["MAT00A"]),
    Subject(StudentStatus.PENDING, "XAHC01", "Computação e Sociedade",area=Area.HUMAN_ASPECTS_IN_COMPUTING,default_semester=7,type=SubjectType.REQUIRED,credit=64,prerequisites=[]),
    Subject(StudentStatus.PENDING, "XAHC02", "Interação Humano-Computador",area=Area.HUMAN_ASPECTS_IN_COMPUTING,default_semester=6,type=SubjectType.REQUIRED,credit=64,prerequisites=["XDES03", "XDES04"]),
    Subject(StudentStatus.PENDING, "XAHC03", "Metodologia Científica",area=Area.HUMAN_ASPECTS_IN_COMPUTING,default_semester=7,type=SubjectType.REQUIRED,credit=64,prerequisites=["TCC1"]),
    Subject(StudentStatus.PENDING, "CAHC04", "Projeto Integrado",area=Area.HUMAN_ASPECTS_IN_COMPUTING,default_semester=1,type=SubjectType.REQUIRED,credit=32,prerequisites=[]),

    Subject(StudentStatus.PENDING, "SDES05", "Engenharia de Software II",area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING,default_semester=1,type=SubjectType.OPTIONAL,credit=64,prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "SDES06", "Gerência de projetos de software",area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING,default_semester=1,type=SubjectType.OPTIONAL,credit=64,prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "SDES07", "Desenvolvimento de sistemas web", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, SubjectType.OPTIONAL, 64, ["XDES04", "XPAD01", "XDES03"]),
    Subject(StudentStatus.PENDING, "XDES08", "Arquitetura de Software",area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING,default_semester=1,type=SubjectType.OPTIONAL,credit=64,prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "XDES10", "Engenharia de Software Experimental",area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING,default_semester=1,type=SubjectType.OPTIONAL,credit=64,prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "XDES11", "Tópicos em DES I",area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING,default_semester=1,type=SubjectType.OPTIONAL,credit=64,prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "XDES12", "Tópicos em DES II",area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING,default_semester=1,type=SubjectType.OPTIONAL,credit=64,prerequisites=["XDES04"]),
    Subject(StudentStatus.PENDING, "XDES13", "Desenvolvimento de Jogos",area=Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING,default_semester=1,type=SubjectType.OPTIONAL,credit=64,prerequisites=["XDES02"]),
    Subject(StudentStatus.PENDING, "ECOX21", "Maratona de programação I", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, SubjectType.OPTIONAL, 48, ["XDES01"]),
    Subject(StudentStatus.PENDING, "ECOX22", "Maratona de programação II", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 1, SubjectType.OPTIONAL, 48, ["ECOX21"]),
    
    Subject(StudentStatus.PENDING, "SPAD02", "Banco de Dados II", Area.DATA_PERSISTENCE_AND_ANALYSIS, 1, SubjectType.OPTIONAL, 64, ["XPAD01"]),
    Subject(StudentStatus.PENDING, "SPAD03", "Introdução à Análise de Dados", Area.DATA_PERSISTENCE_AND_ANALYSIS, 1, SubjectType.OPTIONAL, 64, ["XMAC02", "XPAD01"]),
    Subject(StudentStatus.PENDING, "XPAD04", "Banco de Dados noSQL", Area.DATA_PERSISTENCE_AND_ANALYSIS, 1, SubjectType.OPTIONAL, 64, ["XPAD01"]),
    Subject(StudentStatus.PENDING, "XPAD08", "Tópicos em PAD", Area.DATA_PERSISTENCE_AND_ANALYSIS, 1, SubjectType.OPTIONAL, 64, ["XPAD01", "SPAD03"]),
    Subject(StudentStatus.PENDING, "XPAD09", "Análise e Previsão de Séries Temporais", Area.DATA_PERSISTENCE_AND_ANALYSIS, 5, SubjectType.OPTIONAL, 64, ["XMAC02"]),
    
    Subject(StudentStatus.PENDING, "XMCO03", "Métodos Exatos", Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 1, SubjectType.OPTIONAL, 64, ["XMAC02", "CTCO02"]),
    Subject(StudentStatus.PENDING, "XMCO04", "Metaheurísticas", Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 1, SubjectType.OPTIONAL, 64, ["XMAC02", "CTCO02"]),
    Subject(StudentStatus.PENDING, "XMCO05", "Tópicos em MCO", Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 1, SubjectType.OPTIONAL, 64, ["XMAC02", "CTCO02"]),
    Subject(StudentStatus.PENDING, "CMCO06", "Modelagem Geométrica e Visual", Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 1, SubjectType.OPTIONAL, 64, ["XMAC02", "CMCO05"]),
    Subject(StudentStatus.PENDING, "CMCO07", "Visão Computacional", Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 1, SubjectType.OPTIONAL, 64, ["XMAC01", "CMCO05"]),
    Subject(StudentStatus.PENDING, "CMCO08", "Teoria dos Jogos", Area.COMPUTATIONAL_METHODOLOGIES_AND_OPTIMIZATION, 1, SubjectType.OPTIONAL, 64, ["XMAC01"]),
    
    Subject(StudentStatus.PENDING, "XRSC06", "Auditoria em Segurança de SI", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 1, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, "XRSC07", "Computação em Nuvem", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 1, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, "XRSC08", "Programação Paralela", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 1, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, "XRSC09", "Sistemas Distribuidos", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 1, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, "XRSC10", "Tópicos em RSC", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 1, SubjectType.OPTIONAL, 64, ["XRSC01"]),
    Subject(StudentStatus.PENDING, "ECOS04", "Simulação e Avaliação de Desempenho", Area.COMPUTER_NETWORKS_AND_SYSTEMS, 1, SubjectType.OPTIONAL, 32, ["XRSC09"]),

    Subject(StudentStatus.PENDING, "SADG01", "Gestão e Governança de TI", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 64, ["IEPG22"]),
    Subject(StudentStatus.PENDING, "SADG02", "Economia da Informação", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 64, []),
    Subject(StudentStatus.PENDING, "IEPG01", "Empreendedorismo e Inovação", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, "IEPG10", "Engenharia Econômica", Area.MANAGEMENT_AND_ADMINISTRATION, 6, type=SubjectType.REQUIRED, credit=48, prerequisites=[]),
    Subject(StudentStatus.PENDING, "IEPG014", "Comportamento Organizacional I", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, "IEPG020", "Introdução à Economia", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, "IEPG022", "Administração Aplicada", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 32, []),
    Subject(StudentStatus.PENDING, "ADM03E", "Empreendedorismo Técnológico", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 48, ["IEPG01"]),

    Subject(StudentStatus.PENDING, "XAHC06", "Tópicos em AHC", Area.HUMAN_ASPECTS_IN_COMPUTING, 1, SubjectType.OPTIONAL, 64, []),
    Subject(StudentStatus.PENDING, "XAHC07", "Computação Aplicada a Educação", Area.HUMAN_ASPECTS_IN_COMPUTING, 1, SubjectType.OPTIONAL, 64, ["XDES03", "XDES04"]),
    Subject(StudentStatus.PENDING, "XAHC08", "Tópicos em UX Design", Area.HUMAN_ASPECTS_IN_COMPUTING, 1, SubjectType.OPTIONAL, 64, ["XMAC02", "XAHC02"]),
    Subject(StudentStatus.PENDING, "IEPG21", "Ciências Humanas e Sociais", Area.HUMAN_ASPECTS_IN_COMPUTING, 1, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, "ADM08H", "Psicologia: Relações índividuo-Grupo", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, "LET007", "LIBRAS: Linguagem Brasileira de Sinais", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, "ADM51H", "Ciências, Tecnologias e Organizações", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 48, []),
    Subject(StudentStatus.PENDING, "ADM52H", "Comportamento Organizacional II", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 32, []),
    Subject(StudentStatus.PENDING, "ADM54H", "Gestão de Carreira", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 32, []),
    Subject(StudentStatus.PENDING, "ADM58H", "Psicologia Organizacional e do Trabalho", Area.MANAGEMENT_AND_ADMINISTRATION, 1, SubjectType.OPTIONAL, 32, []),

    Subject(StudentStatus.PENDING, "TCC1", "TCC1", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 7, SubjectType.REQUIRED, 140, []),
    Subject(StudentStatus.PENDING, "TCC2", "TCC2", Area.SOFTWARE_DEVELOPMENT_AND_ENGINEERING, 8, SubjectType.REQUIRED, 210, ["TCC1"]),
]