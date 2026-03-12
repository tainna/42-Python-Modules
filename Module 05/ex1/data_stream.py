from abc import ABC, classmethod, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @classmethod
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process one list of data. The chield is"""
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Implementação padrão. Retorna um dicionário.
        Union significa que os valores do dicionário podem ser texto, inteiros ou decimais.
        """
        return {"stream_id": self.stream_id, "status": "active"}


class SensorStream(DataStream):

    def __init__(self, stream_id: str):
        # Usamos o super() para chamar o __init__ da classe mãe e guardar o ID lá!
        super().__init__(stream_id)
        # Podes inicializar variáveis extra aqui para guardar estatísticas (ex: self.total_lidos = 0)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data_batch.isinstance(int)
        except ValueError as e:
            print("Error: {e}")

        # TODO: Implementar a lógica do sensor usando try/except e isinstance()!
        pass

    # TODO: Fazer override do get_stats ou do filter_data, se a lógica do sensor exigir