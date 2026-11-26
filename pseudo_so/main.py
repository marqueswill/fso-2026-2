# =================================================================================================
# PSEUDO-SO (main)
# =================================================================================================
#
# -------------------------------------------------------------------------------------------------
# Visão geral
# -------------------------------------------------------------------------------------------------
#
# Implementação de um pseudo-SO multiprogramado, composto por um Gerenciador de Processos, por um
# Gerenciador de Memória, por um Gerenciador de E/S e por um Gerenciador de Arquivos. O
# gerenciador de processos deve ser capaz de agrupar os processos em quatro níveis de
# prioridades. O gerenciador de memória deve garantir que um processo não acesse as regiões de
# memória de um outro processo. O gerenciador de E/S deve ser responsável por administrar a
# alocação e a liberação de todos os recursos disponíveis, garantindo uso exclusivo deles. E o
# gerenciador de arquivos deve permitir que os processos possam criar e deletar arquivos, de
# acordo com o modelo de alocação determinado. Os detalhes para a implementação desse pseudo-SO
# são descritos nas próximas seções.
#
# -------------------------------------------------------------------------------------------------
# Módulos
# -------------------------------------------------------------------------------------------------
#
# Conforme descrito anteriormente, espera-se que o programa seja dividido em, pelo menos, cinco
# grandes módulos: processo, memória, filas, recursos e arquivos. Esses modelos devem ser:
#
#   • Módulo de Processos – classes e estruturas de dados relativas ao processo. Basicamente,
#     mantém informações específicas do processo.
#   • Módulo de Filas – mantém as interfaces e funções que operam sobre os processos;
#   • Módulo de Memória – provê uma interface de abstração de memória RAM;
#   • Módulo de Recurso – trata a alocação e liberação dos recursos de E/S para os processos;
#   • Módulo de Arquivos – trata as operações create e delete sobre os arquivos.
#
# É importante ressaltar também que outros módulos podem ser utilizados, caso sejam necessários
#
# -------------------------------------------------------------------------------------------------
# Arquivos de entrada
# -------------------------------------------------------------------------------------------------
#
# O programa deve ler três arquivos. O primeiro é um arquivo contendo as informações dos
# processos a serem criados e gerenciados pelo pseudo-SO. O segundo arquivo traz a descrição das
# operações a serem realizadas pelo sistema de arquivos. E o terceiro arquivo contém as strings
# de referência das páginas usadas na execução de cada processo.
#
# --- 1º arquivo (processos) ---
#
# No primeiro arquivo, cuja extensão deve ser .txt, cada linha contém as informações de um único
# processo. Portanto, um arquivo com 2 linhas deve disparar 2 processos, outro arquivo com 5
# linhas fará com que o programa dispare 5 processos, e assim por diante. Cada processo,
# portanto, cada linha, deve conter os seguintes dados:
#
#   <tempo de inicialização>, <prioridade>, <tempo de processador>,
#   <tamanho máximo do conjunto de trabalho>, <requisição da impressora>,
#   <requisição do scanner>, <requisição do modem>, <requisição do disco SATA>
#
# --- 2º arquivo (sistema de arquivos) ---
#
# No segundo arquivo, cuja extensão também deve ser .txt, haverá a quantidade total de blocos no
# disco, a quantidade de blocos ocupados, a identificação de quais arquivos já estão gravados no
# disco, a localização dos blocos usados por cada arquivo, a identificação de qual processo
# efetuará cada operação, a identificação das operações, sendo código 0 para criar um arquivo, e
# código 1 para deletar um arquivo. Além disso, para as operações de criação deve constar o nome
# do arquivo a ser criado, e a quantidade de blocos ocupada pelo arquivo. Por outro lado, na
# operação de deletar um arquivo, deve constar apenas o nome do arquivo a ser deletado. Dessa
# forma, a organização interna do arquivo de entrada com as operações de arquivo deve ser:
#
#   - Linha 1: Quantidade de blocos do disco;
#   - Linha 2: Quantidade de segmentos ocupados no disco (n);
#   - A partir da Linha 3 até Linha n + 2: arquivo (a ser identificado por uma letra), número do
#     primeiro bloco gravado, quantidade de blocos ocupados por este arquivo;
#   - A partir da linha n + 3: cada linha representa uma operação a ser efetivada pelo sistema de
#     arquivos do pseudo-SO. Para isso, essas linhas vão conter:
#
#       <ID_Processo>, <Código_Operação>, <Nome_arquivo>, <se_operacaoCriar_numero_blocos>.
#
#     Para padronizar, o <ID_Processo> deve sempre iniciar em 0 (zero), ou seja, os processos vão
#     ser numerados de <0> até <Quantidade de Processos – 1>.
#
# --- 3º arquivo (strings de referência) ---
#
# O terceiro arquivo de entrada, também com extensão .txt, deve ter em cada linha a string de
# referência que será usada na execução de cada processo. Todas as páginas e frames têm o mesmo
# tamanho, que foi especificado em 1k
# =================================================================================================
