from dataclasses import dataclass, field
from enum import Enum


# =================================================================================================
# MÓDULO DE PROCESSOS (process)
# =================================================================================================


@dataclass
class Process:
    pid:int
    priority:int
    max_frames:int

    start_time:int
    cpu_time:int
    remaining_time:int

    printer:bool
    driver:bool
    scanner:bool
