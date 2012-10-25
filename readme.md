Uma firma que utiliza equipamentos de informática necessita de um sistema que gerencie a sua rede de microcomputadores (ponto-a-ponto, não existe servidor da rede), controlando usuários, máquinas e impressoras. A rede é composta de servidores de impressão, estações e impressoras. O sistema também irá controlar a partir de qual estação o usuário está conectado a rede, e os seus arquivos enviados para impressão.
Para todos os micros deseja-se cadastrar: código do patrimônio, descrição, capacidade do disco rígido, quantidade de memória e, sendo uma estação a sua localização, sendo um servidor o tamanho máximo do buffer e a quantidade máxima de buffers de impressão e que ele suporta, e as impressoras ligadas a ele (no máximo 3), caso existam. Para impressoras deseja-se cadastrar: código do patrimônio, descrição, velocidade (CPS) e, consequentemente, o servidor a que está ligada. Nesta firma todas as impressoras estão ligadas a algum servidor, não sendo compartilhada por mais de um servidor.
Para controlar os usuários, o sistema só precisa do nome de guerra e senha de cada um. Como os usuários não possuem máquina fixa, a sua conexão à rede pode ocorrer a partir de qualquer estação. Tendo o usuário uma conexão ativa, o sistema não permitirá que ele se conecte a partir de outra estação. Há interesse em controlar apenas as conexões ativas (as conexões desfeitas são irrelevantes).
No caso de impressão, o sistema deverá saber qual o arquivo, de quem ele é, e em qual impressora será impresso (atenção: somente usuários com conexão ativa e que possuem condição de enviar arquivos para impressão). É o usuário que escolhe a impressora onde ele quer que o seu arquivo seja impresso. Nada impede que usuários diferentes enviem arquivos de mesmo nome para impressão, porém (nesta firma) para o mesmo usuário isso não e possível, mesmo em impressoras diferentes. Neste caso o sistema permite alterar o número de cópias a serem impressas. Só deve ser mantido registro dos arquivos que ainda estão na fila de impressão.
O sistema deverá listar, para cada impressora, os arquivos que estão aguardando impressão, com o respectivo usuário que a enviou, mesmo que o usuário não esteja mais ativo na rede. Sempre que solicitado o sistema exibirá, para cada estação, o seu código e, caso exista, o nome do usuário conectado, a data e hora início desta conexão e, se houver, nome e quantidade de cópias dos arquivos que ele enviou e que ainda estão aguardando impressão.
