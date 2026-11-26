# =================================================================================================
# MÓDULO DE FILAS (queues)
# =================================================================================================
#
# O programa deve ter duas filas de prioridades distintas: a fila de processos de tempo real e a
# fila de processos de usuários.

# Processos de tempo real entram para a fila de maior prioridade, sendo gerenciados pela política de escalonamento FIFO (First In First Out), sem preempção.
# Os processos devem receber um ID. Esse ID deve sempre iniciar em 0 (zero) e ir até a quantidade de
# processos – 1.

# Processos de usuário devem utilizar múltiplas filas de prioridades com realimentação. Para
# isso, devem ser mantidas três filas com prioridades distintas.

# Para evitar starvation, o sistema operacional deve modificar a prioridade dos processos executados mais frequentemente e/ou
# utilizar uma técnica de envelhecimento (aging). Quanto menor for o valor da prioridade
# atribuída a um processo, maior será a sua prioridade no escalonamento. Dessa forma, os
# processos de tempo real, que são os mais prioritários, terão prioridade definida como 0 (zero).

# Além disso, é importante destacar que processos de usuário podem ser preemptados e o quantum
# deve ser definido de 1 milissegundo.

# As filas devem suportar no máximo 1000 processos. Portanto, recomenda-se utilizar uma fila
# “global”, que permita avaliar os recursos disponíveis antes da execução e que facilite
# classificar o tipo de processo.
# =================================================================================================


from collections import deque

MAX_PROCESSES = 1000


class ProcessQueue: 
    """_summary_ 
    """

    def __init__(self, capacity = MAX_PROCESSES):
        self._items = deque()
        self._capacity = capacity

    # adiciona na fila
    def push(self):
        pass

    # retira o primeiro
    def pop(self):
        pass

    # usado para preempcao
    def remove(self):
        # chechar se o processo e de user
        pass
    
    def is_empty(self):
        pass


class Scheduler:
    """_summary_ Contém todas as filas 
    """

    NUM_USER_QUEUES = 3
    QUANTUM_SIZE = 1 # 1 ms
    AGING_LIMIT = 5 # se ficar 5 ms sem executar, aumentar a prioridade

    def __init__(self) -> None:
        self.global_queue = ProcessQueue() # fila de staging -> NEW e BLOCKED

        self.real_time_queue = ProcessQueue()
        self.user_queues = [ProcessQueue() for _ in range(self.NUM_USER_QUEUES)]

    # determina a prioridade e adiciona para sua respectiva fila
    def admit(self, process):
        pass

    # pega proximo processo com base na fila de prioridade
    def next_process(self):
        # tempo real (p0)
        # user (p1)
        # user (p2)
        # user (p3)
        pass

    # retira da CPU quando o quantum acabar e diminui a prioridade
    # apenas para processos de usuario
    def preempt(self, process):
        pass

    # se esperar demais aumenta a prioridade
    # TODO: definir quando aplicar
    def apply_aging(self):
        pass
