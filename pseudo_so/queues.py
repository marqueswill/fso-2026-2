# =================================================================================================
# MÓDULO DE FILAS (queues)
# =================================================================================================
#
# O programa deve ter duas filas de prioridades distintas: a fila de processos de tempo real e a
# fila de processos de usuários. Processos de tempo real entram para a fila de maior prioridade,
# sendo gerenciados pela política de escalonamento FIFO (First In First Out), sem preempção. Os
# processos devem receber um ID. Esse ID deve sempre iniciar em 0 (zero) e ir até a quantidade de
# processos – 1.
#
# Processos de usuário devem utilizar múltiplas filas de prioridades com realimentação. Para
# isso, devem ser mantidas três filas com prioridades distintas. Para evitar starvation, o sistema
# operacional deve modificar a prioridade dos processos executados mais frequentemente e/ou
# utilizar uma técnica de envelhecimento (aging). Quanto menor for o valor da prioridade
# atribuída a um processo, maior será a sua prioridade no escalonamento. Dessa forma, os
# processos de tempo real, que são os mais prioritários, terão prioridade definida como 0 (zero).
# Além disso, é importante destacar que processos de usuário podem ser preemptados e o quantum
# deve ser definido de 1 milissegundo.
#
# As filas devem suportar no máximo 1000 processos. Portanto, recomenda-se utilizar uma fila
# “global”, que permita avaliar os recursos disponíveis antes da execução e que facilite
# classificar o tipo de processo. A Figura 1 ilustra o esquema indicado.
# =================================================================================================
