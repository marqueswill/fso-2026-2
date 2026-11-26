# =================================================================================================
# MÓDULO DE MEMÓRIA (memory)
# =================================================================================================
#
# Implementar um módulo de gerência de memória de um Sistema Operacional capaz de simular a
# execução de processos que usam memória virtual por meio da técnica de paginação. O sistema
# deverá receber uma sequência de páginas que serão referenciadas durante a execução do processo
# (string de referência) e uma quantidade fixa de frames disponíveis na memória principal, que
# será o tamanho máximo do conjunto de trabalho do processo (working set). Durante a simulação,
# cada página referenciada, que não estiver carregada nos frames, deverá gerar um page fault, que
# será contabilizado para o respectivo processo. Deve ser utilizado um tamanho fixo de memória
# principal de 20 frames, sendo cada frame de 1k. Dessa quantidade, 8 frames são reservados para
# os processos de tempo real. Assim, esses 8 frames nunca poderão ser alocados para processos de
# usuário. Da mesma maneira, os 12 frames de processos de usuário não podem ser alocados para
# processos de tempo real.
#
# O algoritmo de substituição de páginas deve ser o LRU (Least Recently Used), aplicado no escopo
# local. Além disso, para facilitar a implementação, vamos ignorar o tempo necessário para tratar
# cada falta de página, e o processo que tiver uma falta de página, continuará de posse da CPU
# sem afetar o seu tempo de uso da CPU. É importante considerar que para todos os processos a
# pré-carga é definida em uma página.
# =================================================================================================
