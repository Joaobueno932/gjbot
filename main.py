import requests
import time
import json
import os
 

# Ler as mensagens que estão chegando
class TelegramBot:
  def __init__(self): 
    token = '5620468326:AAES_eM5a-vBNg5RqSMjV9zXvNH5B62bUp8'
    self.url_base = f'https://api.telegram.org/bot{token}/'
  #iniciar bot
  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao['result']
      if mensagens: 
        for mensagem in mensagens:
          update_id = mensagem['update_id']
          chat_id = mensagem['message']['from']['id']
          primeira_mensagem = mensagem['message']['message_id'] == 1
          resposta = self.criar_resposta(mensagem,primeira_mensagem)
          self.responder(resposta,chat_id)
  
  #obter mensagens

  def obter_mensagens(self,update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)
    
  #criar uma resposta
  def criar_resposta(self,mensagem,primeira_mensagem):
    mensagem = mensagem['message']['text']
    if primeira_mensagem == True or mensagem.lower() in ('inicio','início'):
      return f'''Olá meu amor, tudo bem? Digite sim ou não.'''
    if mensagem.lower() in ('s','sim'):
      return f'''Opa que bom meu amor, se vc está feliz eu estou feliz, saiba que eu te amo mais que tudo nesse mundooo, porém digita "menu" pra vc ver algo especial pra vc meu amor.'''
    if mensagem.lower() in ('n','nao','não','opcoes','opçoes','opções',):
      return f'''Sério amor?? {os.linesep}Pode ficar tranquila, vou te ajudar com isso.{os.linesep}Qual desses vc quer saber primeiro, um conselho, deixe o 4 por ultimo:{os.linesep}1- Porque eu te amo?{os.linesep}2- O quanto eu te amo?{os.linesep}3- Quem de fato é a Geórgia?{os.linesep}4- Aonde vc vai estar daqui a 10 anos.{os.linesep}5- Aperte quando terminar de ler todos.'''
    if mensagem.lower() == 'menu':
      return f'''1- Porque eu te amo?{os.linesep}2- O quanto eu te amo?{os.linesep}3- Quem de fato é a Geórgia?{os.linesep}4- Aonde vc vai estar daqui a 10 anos.{os.linesep}5- Aperte quando terminar de ler todos.'''
    if mensagem.lower() in ('1','um'):
      return f'''Porque assim como o oxigênio, vc que me mantem vivo, vc é a cor no meu mundo preto e branco, eu te amo, porque quando penso em felicidade, penso em vc me fazendo rir com esse seu sorriso contagiante, me fazendo sorrir quando estou triste. Quando penso em futuro, penso no nosso casamento, nossa casa, nossos filhos, Nossa linda familia que teremos. Vc é meu mundo, é meu tudo.{os.linesep}Se quiser voltar para o menu e ler as outras opções, digite "menu".'''
    if mensagem.lower() in ('2','dois'):
      return f'''O quanto de grãos de areias há no mundo, gotas de agua há no mar, estrelas há no céu, comparado ao amor que eu sinto por vc, parece que são pequenos numeros, pois nada consegue ser tão grande quanto ao amor  que eu sinto por vc, o tamanho do meu amor por vc é mais do que ontem, e menos do que amanhã. Uma coisa vc pode ter certeza, sempre será só vc q eu quero e mais ninguém.{os.linesep}Se quiser voltar para o menu e ler as outras opções, digite "menu".'''
    if mensagem.lower() in ('3','tres'):
      return f''' Geórgia Galiano Pimenta, uma mulher linda que nasceu no dia 12/11/1998, signo de escorpião, com 1,65 de altura. Bom, oque dizer sobre algo perfeito? tambem não tenho palavras para descrever a pessoa mais perfeita do mundo, mas vamos la. Um exemplo de mulher guerreira, trabalhadora, inteligente, independente, que sempre vai atrás do sim na vida dela, que se quiser conquista o mundo todo com seu sorriso encantador, uma mulher que trás a felicidade aonde há tristeza, uma mulher que realmente sabe oque quer para o seu futuro, e não vamos esquecer de sua beleza inesquecível, uma boca linda, um corpo gostoso, que me deixa louco so de lembrar dele, me fazendo ter uma vontade louca de beija lo o dia inteiro, e com uma voz que acalma o coração de qualquer um.{os.linesep}Se quiser voltar para o menu e ler as outras opções, digite "menu".'''
    if mensagem.lower() in ('4','quartro'):
      return f''' Oii amor, sou eu, só que do futuro haha, vou te dar um leve spoiler de como está o 2032, o covid já não é mais um problema, ele finalmente virou uma gripe normal no mundo todo, o presidente do Brasil agora é o Tiririca, com 100% de aprovação, e querendo ou não o Brasil está melhorando agora ksksk brincadeira, mas não vamos falar disso, deixa eu te dar um leve spoilei da nossa vida, sim estamos no Canadá ihuuu, ja fazem uns 7 anos, temos dois cachorros ksksk e dois filhos, que são a nossa alegria, pensa em umas crianças lindas, são os nossos filhos, e se vc tem dúvida se vai ser uma boa mãe, fica tranquila, vc se tornou a melhor mãe do mundo meu amor. Bom, ja a nossa vida financeira, temos a casa e os carros do nosso sonho, um seu, outro meu, e mais um de passeio para a gente, e além do mais, temos uma casa na praia no Brasil tbm, pra quando formos visitar nossa familia e amigos la, conseguimos tambem dar uma vida mt boa para nossas mães, e estamos viajando o mundo inteiro todo ano. Já nós dois, como estamos?! estamos juntos cada dia mais meu amor, pode ficar tranquila que o meu eu do futuro, e esse meu eu do seu presente, te ama mais que tudo nesse mundo, e não vive sem vc, e vai sempre fazer de tudo para q vcs/nós sejamos sempre felizes e juntos.{os.linesep}Se quiser voltar para o menu e ler as outras opções, digite "menu".'''
    if mensagem.lower() in ('5','cinco'):
      return f'''Fiz esse bot amor, para quando vc estiver se sentindo triste, ou com ansiedade, para vc ter uma noção do meu amor por vc, basta dizer um olá.'''
   
    else:
      return 'Olá meu amor, digite "inicio" para iniciar.'
      
  #responder as mensagens
  def responder(self,resposta,chat_id):
    #enviar as respostas das mensagens
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)
 
bot = TelegramBot()
bot.Iniciar()