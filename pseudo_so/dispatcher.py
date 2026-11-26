# =================================================================================================
# DESPACHANTE (dispatcher)
# =================================================================================================
#
# O processo principal é o “despachante”. Esse é o primeiro processo criado na execução do problema
# e deve ser o responsável pela criação de qualquer processo.
#
# Na criação de cada processo, o
# despachante deve exibir uma mensagem de identificação contendo as seguintes informações:
#
#   • PID (int);
#   • Prioridade do processo (int);
#   • Quantidade de páginas alocadas na memória principal;
#   • Utilização de impressora (bool);
#   • Utilização de scanner (bool);
#   • Utilização de drivers (bool).
#
# O processo deve exibir alguma mensagem que indique sua execução. Contudo, isso não é
# obrigatório.
# =================================================================================================


class Dispatcher:
    def __init__(self, processes, memory, resources, filesystem, scheduler):
        self.clock = 0
        self.running = None  # retorna processo sendo executado

        self.processes = processes
        self.memory = memory
        self.resources = resources
        self.filesystem = filesystem
        self.scheduler = scheduler

    def run(self):
        while not self._all_finished():

            self.clock += 1

        self._print_report()

    def _all_finished(self):
        return True

    def _print_report(self):
        pass
