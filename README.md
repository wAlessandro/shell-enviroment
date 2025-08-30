Conceito--><br>
Foco do shell -> gerenciamento

Lógica--><br>
 O programa separa cada parâmetro em cada espaço digitado pelo usuário e os executam dentro de tuplas, que serão utilizadas para inicializar e gerenciar as funções internas.
 A função gerente de inicialização das outras funções é a execute. Lá, ela define como os parâmetros serão enviados para as funções, utilizando a função catchTypingErrors para encontrar erros de digitação, comparando as operações dadas e as disponíveis no armazenamento. Após a verificação, execute inicializa, do armazenamento, de acordo com a quantidade de parâmetros enviados.

Tratamento de erros--><br>
 Além do tratamento de erro de digitação, dentro das funções, cada uma tem seu próprio tratamento de erros mais internos.<br>

Funcionalidades--><br>
cd [caminho]: permite alterar o caminho atual de gerenciamento.<br>
!!: execute o último comando digitado.<br>
! [x]: execute o comando indexado, a partir do histórico.<br>
exit: fecha o programa.<br>
showh: imprime os comandos do histórico.<br>
start [nome do arquivo]: executa programa indicado no diretório atual.<br>
