from dataclasses import dataclass, field
from enum import Enum

# =================================================================================================
# MÓDULO DE PROCESSOS (process)
# =================================================================================================


class ProcessState(Enum):
    NEW = "new"  # criado mas não chegou na fila
    BLOCKED = "blocked"  # na fila mas sendo bloqueado
    READY = "ready"  # na fila e pronto pra ser processado
    RUNNING = "running"  # está sendo processado
    FINISHED = "finished"  # encerrou


@dataclass
class Process:
    # dados do processes.txt
    pid: int # igual o número da linha no processes.txt
    start_time: int
    priority: int
    cpu_time: int
    max_frames: int
    printer: bool
    scanner: bool
    driver: bool 
    sata: bool
    
    # estado de execução
    state: ProcessState = field(default=ProcessState.NEW, init=False)
