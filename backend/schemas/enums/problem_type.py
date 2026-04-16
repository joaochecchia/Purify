import enum

class ProblemType(enum.Enum):
    VAZAMENTO = "vazamento"
    ESGOTO_ABERTO = "esgoto_aberto"
    FALTA_COLETA = "falta_coleta"
    FALTA_ABASTECIMENTO = "falta_abastecimento"
    AGUA_CONTAMINADA = "agua_contaminada"
    OUTRO = "outro"