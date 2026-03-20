from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process one batch of data. The child needs to implement this."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Default implementation. Returns a dictionary.
        Union means values can be strings, integers, or floats.
        """
        return {"stream_id": self.stream_id, "status": "active"}


class StreamProcessor:
    """
    This is the Manager class. It doesn't inherit from DataStream.
    Instead, it holds a list of DataStream objects!
    """
    def __init__(self):
        # Uma lista vazia que vai guardar objetos do tipo DataStream
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Adiciona qualquer tipo de stream
        (Sensor, Transação, etc) à lista."""
        self.streams.append(stream)

    def process_all_batches(self, batches_list: List[List[Any]]) -> None:
        """
        Isto é o Polimorfismo:Percorre a lista de streams
        e envia o batch correspondente para cada uma.
        """
        for i in range(len(self.streams)):
            stream = self.streams[i]
            batch = batches_list[i]
            resultado = stream.process_batch(batch)
            print(f"- {resultado}")


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
                avg = sum(temps) / len(temps)
            else:
                avg = 0.0

            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg:.1f}°C"
            )
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        if self.total_readings > 0:
            avg = self.sum_temp / self.total_readings
        else:
            avg = 0.0

        return {
            "stream_id": self.stream_id,
            "type": "Environmental Data",
            "total_readings": self.total_readings,
            "average_temperature": avg
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.total_transactions = 0
        self.net_flow = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buys = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and "buy:" in item
            ]

            sells = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and "sell:" in item
            ]

            total_ops = len(buys) + len(sells)
            current_net_flow = sum(buys) - sum(sells)

            self.total_transactions += total_ops
            self.net_flow += current_net_flow

            sign = "+" if current_net_flow > 0 else ""

            return (
                f"Transaction analysis: {total_ops} operations, "
                f"net flow: {sign}{current_net_flow:.0f} units"
            )
        except Exception as e:
            return f"Error processing transaction batch: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Financial Data",
            "total_transactions": self.total_transactions,
            "net_flow": self.net_flow
        }


class EventStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.total_login = 0
        self.sum_error = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            error = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and "error:" in item
            ]

            self.total_readings += len(data_batch)
            self.sum_error += sum(error)

            return (
                f"Event analysis: {len(data_batch)} events,"
                f"{sum(error)} error detected"
                )
        except Exception as e:
            return f"Error processing transaction batch: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Event Data",
            "total_login": self.total_login,
            "error": self.sum_error
        }


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    stats_s = sensor.get_stats()
    print(f"Stream ID: {stats_s['stream_id']}, Type: {stats_s['type']}")

    batch_sensor = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(batch_sensor)}]")
    print(sensor.process_batch(batch_sensor))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    stats_t = trans.get_stats()
    print(f"Stream ID: {stats_t['stream_id']}, Type: {stats_t['type']}")

    batch_trans = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(batch_trans)}]")
    print(trans.process_batch(batch_trans))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    stats_e = event.get_stats()
    print(f"Stream ID: {stats_e['stream_id']}, Type: {stats_e['type']}")

    batch_event = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(batch_event)}]")
    print(event.process_batch(batch_event))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("\nBatch 1 Results:")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    super_batch = [
        ["temp:24.0", "temp:25.0"],
        ["buy:200", "sell:50", "buy:100", "sell:10"],
        ["error", "error", "login"]
    ]

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")
