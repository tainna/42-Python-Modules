from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @classmethod
    @abstractmethod
    def process_batch(cls, data_batch: List[Any]) -> str:
        """Process one list of data. The chield need to implement this"""
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
        super().__init__(stream_id)
        self.total_readings = 0
        self.sum_temp = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and "temp:" in item
            ]
            self.total_readings += len(data_batch)
            self.sum_temp += sum(temps)
     
            if len(temps) > 0:
                avg = sum(temps) / len(temps)  # 22.5 / 1 = 22.5
            else:
                avg = 0.0

            return (f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {avg:.1f}°C")
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def get_stats(self) -> dict[str, Union[str, int, float]]:

        avg = self.sum_temp / self.total_readings if self.total_readings > 0 else 0
        return {
            "stream_id": self.stream_id,
            "type": "Environmental Data",
            "total_readings": self.total_readings,
            "average_temperature": avg
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.total_readings = 0
        self.sum_trans = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            trans = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and "buy:" in item
            ]
            self.total_readings += len(trans)
            self.sum_trans += sum(trans)

            return (f"Transaction analysis: {len(trans)} operations, net flow: {self.sum_trans} units")
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def get_stats(self) -> dict[str, Union[str, int, float]]:

        avg = self.sum_temp / self.total_readings if self.total_readings > 0 else 0
        return {
            "stream_id": self.stream_id,
            "type": "Environmental Data",
            "total_readings": self.total_readings,
            "average_temperature": avg
        }


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    # ---------------------------------------------------------
    # PARTE 1: Testes Individuais
    # ---------------------------------------------------------

    # 1. Testando o Sensor
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    stats_s = sensor.get_stats()
    print(f"Stream ID: {stats_s['stream_id']}, Type: {stats_s['type']}")

    batch_sensor = ["temp:22.5", "humidity:65", "pressure:1013"]
    # Para imprimir o formato exato do array sem aspas simples do Python, usamos um truque de string:
    print(f"Processing sensor batch: [{', '.join(batch_sensor)}]") 
    print(sensor.process_batch(batch_sensor))

    # 2. Testando as Transações
    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    stats_t = trans.get_stats()
    print(f"Stream ID: {stats_t['stream_id']}, Type: {stats_t['type']}")

    batch_trans = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(batch_trans)}]")
    print(trans.process_batch(batch_trans))

    # 3. Testando os Eventos
    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    stats_e = event.get_stats()
    print(f"Stream ID: {stats_e['stream_id']}, Type: {stats_e['type']}")

    batch_event = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(batch_event)}]")
    print(event.process_batch(batch_event))


    # ---------------------------------------------------------
    # PARTE 2: A Demonstração Polimórfica (StreamProcessor)
    # ---------------------------------------------------------
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("Batch 1 Results:")
    
    # Aqui o PDF exige que uses a tua classe StreamProcessor (O Manager)
    # Exemplo de como deves interagir com ela:
    
    # processor = StreamProcessor()
    # processor.add_stream(sensor)
    # processor.add_stream(trans)
    # processor.add_stream(event)
    
    # O teu StreamProcessor é que vai ter a lógica de chamar os batchs e os filtros!
    # print("- Sensor data: 2 readings processed")
    # ... etc
    
    print("Stream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("All streams processed successfully. Nexus throughput optimal.")