from src.crud.base import CRUDBase
from src.models.disease import Disease
from src.schemas.disease import DiseaseCreate, DiseaseUpdate


class CRUDDisease(CRUDBase[Disease, DiseaseCreate, DiseaseUpdate]):
    pass


disease = CRUDDisease(Disease)
