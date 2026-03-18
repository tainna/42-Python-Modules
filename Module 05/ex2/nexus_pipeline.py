from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import collections


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        print(f"Input: {data}")
        # Mock logic based on the input type
        return {"raw": data, "status": "parsed"}


class TransformStage:
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # You will add print statements here depending on what is being processed
        # e.g., "Transform: Enriched with metadata..."
        return {"transformed": True, "data": data}


class OutputStage:
    def process(self, data: Dict[str, Any]) -> str:
        # You will return the final formatted string here
        return "Output: Processed data"


class ProcessingPipeline(ABC):
    def __init__(self):
        # Esta lista aceita QUALQUER classe que cumpra o ProcessingStage Protocol!
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self) -> None:
        pass # Vamos implementar a logica disto dps