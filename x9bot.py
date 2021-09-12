from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
import requests, telegram, os
from gtts import gTTS
from dados import BOT_TOKEN, POST_CANAL
#OBSERVAÇÕES: O código foi feito com o básico do python e o mínimo possível de importações e regras desnecessárias. Mas, é de sua liberdade melhorá-lo a seu gosto. Utilizei frases/padrões para facilitar a minha interpretação, tomem isso como um estímulo para pessoas com problemas de memória assim como eu :)


#TROQUE POR SEU TOKEN
rede_do_baiano = f"{BOT_TOKEN}"
#AQUI ESTÁ O ID DA SOURCE, NÃO EDITE
source_id = "0xO01x3701"
#NÃO MEXA (AQUI O TOKEN É AUTENTICADO)
corda_da = Updater(f"{rede_do_baiano}")
levanta_baiano = telegram.Bot(token=f"{rede_do_baiano}")




fatmsg = lambda update: update.message.text[update.message.entities[0].length +1:]



#AQUI ESTÁ O HANDLER DO MÓDULO 1: RESPONDE AO COMANDO DE START
def start(update: Update, context) -> None:
	#ENVIA UMA MENSAGEM DE BOAS VINDAS PARA O COMANDO /START
	update.message.reply_text("""▫️<b>Olá tranquilo? so o !

▫️CRIADOR/DONO: @Pythonprogg

▫️Faço a checagem todo usuario que entra em seu grupo se estiver 
na minha base de lotter serar banido de imediato!
Me adcione em seu grupo e me torne de permisões de Administrador
para que eu vigie seu Grupo</b>""","html")


#AQUI ESTÁ O HANDLER DO MÓDULO 1: RESPONDE AO COMANDO DE PING
def ping(update: Update, context) -> None:
	#MENSAGEM PARA O COMANDO DE PING
	update.message.reply_text(f"<b>PONG 🟢〰🟢</b>""","html")


#AQUI ESTÁ O HANDLER DO MÓDULO 1: CHECA SE USUÁRIOS ESTÃO NA LISTA DE LOTTERS
def chk_lotter(update: Update, context) -> None:
	#FATIADOR / TRATAMENTO DE DADOS
	for acao in update.message.new_chat_members:
		#PEGA O ID DO GRUPO PARA O FILTRO DO CANAL DE INFO
		user_grupo = update.message.chat.username
		#PEGA O ID DO USUÁRIO QUE ENTROU
		user_id = acao.id
		#PEGA O USERNAME (NOME DE USUÁRIO) DO USUÁRIO QUE ENTROU
		user_username = acao.username
		#SEM USO, MAS NÃO REMOVA, POIS SERÁ USADO EM FUTURAS VERSŌES
		canal = update.message.chat.id
		#PEGA O USERNAME (NOME DE USUÁRIO DO GRUPO)
		canal_user = update.message.chat.username
		#PEGA O ID DO GRUPO
		grupo = update.message.chat.id
		#TENTA SE CONECTAR À API
		try:
			#ENVIA O ID PARA A API PRINCIPAL PARA ANÁLISE
			resultado = requests.get(f"https://pythonencode-api1.herokuapp.com/checklotter.py?user_id={user_id}&source_id={source_id}").json()["status"]
		#CASO FALHE...
		except:
			#ENVIA MENSAGEM DE ERRO DE CONEXÃO
			update.message.reply_text(f"""<b>Impossível manter o contato com o baiano😐

Possíveis erros;
1- </b><pre>Talvez o baiano, em mais uma de suas hibernações, tenha caído da rede, quebrado a cabeça e morrido.</pre>
<b>2- </b><pre>Possivelmente o criador tenha desativado a source por uso indevido.</pre>

<b>Chame a ambulância em @Codipyt.</b>""","html")

		#CASO RETORNE  "FALSE", SIGNIFICA QUE O USUÁRIO NÃO ESTÁ NA LISTA DE LOTTERS (NÃO SIGNIFICA QUE ELE NÃO SEJA)
		if resultado == "True":
			#ENVIA UMA MENSAGEM PARA O CANAL DO CRIADOR, NÃO REMOVA
			levanta_baiano.sendMessage(POST_CANAL, f"""<b>☠🚨UM LOTTER ENTROU NO GRUPO @{user_grupo}!🚨☠

┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>O usuário foi encontrado na lista de lotters, é altamente remove-lo. Medidas cabíveis serão tomadas pelo próprio bot em alguns instantes, caso o mesmo possua permissão de banir usuários!</pre>

<b>❤️‍🔥GRUPO VIGIADO POR X9 DE LOTTERS❤️‍🔥


GRUPO: @pythoncodegroup_encode
CRÉDITOS DA DB: @GRUPO_TCOL
CANAL: @pythoncode_encode
CRIADOR: @Codipyt


┌USERNAME DO TERROR☠❤️‍🔥
└@TERRORDOSLOTTERS

┌CANAL ANT-LOTTER☠❤️‍🔥
└@todoscontraoslotters</b>""", "html")
			#ENVIA MENSAGEM DE ALERTA PARA O GRUPO (ALERTA: CONTÉM CRÉDITOS, NÃO REMOVA)
			update.message.reply_text(f"""<b>☠🚨ALERTA, UM LOTTER ENTROU NO GRUPO🚨☠

┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>O usuário foi encontrado na lista de lotters, é altamente remove-lo. Medidas cabíveis serão tomadas pelo próprio bot em alguns instantes, caso o mesmo possua permissão de banir usuários!</pre>

<b>❤️‍🔥GRUPO VIGIADO POR X9 DE LOTTERS❤️‍🔥


GRUPO: @pythoncodegroup_encode
CRÉDITOS DA DB: @GRUPO_TCOL
CANAL: @pythoncode_encode
CRIADOR: @Codipyt


┌USERNAME DO TERROR☠❤️‍🔥
└@TERRORDOSLOTTERS

┌CANAL ANT-LOTTER☠❤️‍🔥
└@todoscontraoslotters</b>""","html")
		#TENTA BANIR O BAIANO (LOTTER)
			try:
				levanta_baiano.ban_chat_member(user_id=user_id, chat_id=grupo)
				#ENVIA MENSAGEM DE BAN BEM SUCEDIDO
				update.message.reply_text(f"""<b>TAQUEI O BAN NO BAIANO (LOTTER BANIDO)

Sequência de capa, capa, capa!❤️‍🔥

┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>O usuário foi encontrado na lista de lotters. O bot baniu o usuário conforme a escolha do dono ao dar permissão para o bot banir lotters!</pre>

<b>❤️‍🔥GRUPO VIGIADO POR X9 DE LOTTERS❤️‍🔥


GRUPO: @pythoncodegroup_encode
CRÉDITOS DA DB: @GRUPO_TCOL
CANAL: @pythoncode_encode
CRIADOR: @Codipyt


┌USERNAME DO TERROR☠❤️‍🔥
└@TERRORDOSLOTTERS

┌CANAL ANT-LOTTER☠❤️‍🔥
└@todoscontraoslotters</b>""","html")
				#ENVIA UM AUDIO ENGRAÇADO PARA TRUE BAN
				levanta_baiano.send_audio(chat_id=grupo, audio=open("banido.mp3", 'rb'))
				#ENVIA UMA MENSAGEM PARA O CANAL DO CRIADOR (NÃO REMOVA)
				levanta_baiano.sendMessage(POST_CANAL, f"""<b>LOTTER BANIDO NO GRUPO @{user_grupo}!

Sequência de capa, capa, capa!❤️‍🔥

┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>O usuário foi encontrado na lista de lotters. O bot baniu o usuário conforme a escolha do dono ao dar permissão para o bot banir lotters!</pre>

<b>❤️‍🔥GRUPO VIGIADO POR X9 DE LOTTERS❤️‍🔥


GRUPO: @pythoncodegroup_encode
CRÉDITOS DA DB: @GRUPO_TCOL
CANAL: @pythoncode_encode
CRIADOR: @Codipyt


┌USERNAME DO TERROR☠❤️‍🔥
└@TERRORDOSLOTTERS

┌CANAL ANT-LOTTER☠❤️‍🔥
└@todoscontraoslotters</b>""", "html")
				#MENDIGA PERMISSÃO DE BAN
			except telegram.error.BadRequest:
				#MENSAGEM DE BAN MAU SUCEDIDO
				update.message.reply_text(f"""<b>🔻FALHA AO BANIR🔻</b>

<b>┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>Qual foi admin? Vai papar a kill mesmo? Me dê permissão para banir usuários. Não se esqueça de banir o lotter!😒</pre>

<b>❤️‍🔥GRUPO VIGIADO POR X9 DE LOTTERS❤️‍🔥


GRUPO: @pythoncodegroup_encode
CRÉDITOS DA DB: @GRUPO_TCOL
CANAL: @pythoncode_encode
CRIADOR: @Codipyt


┌USERNAME DO TERROR☠❤️‍🔥
└@TERRORDOSLOTTERS

┌CANAL ANT-LOTTER☠❤️‍🔥
└@todoscontraoslotters</b>""","html")
				#ENVIA UM ÁUDIO ENGRAÇADO PARA FALSE BAN
				levanta_baiano.send_audio(chat_id=grupo, audio=open("papa_kill.mp3", 'rb'))


#AQUI ESTÁ O HANDLER DO MÓDULO 1: COMANDO /FALE
def fale(update: Update, context) -> None:
	#SEPARA O TEXTO
	texto = (fatmsg(update))
	#PEGA O ID DO USUÁRIO
	id = f"{update.message.from_user.id}"
	#REMOVE TRAÇOS DO ID PARA EVITAR ERROS
	audio = id.replace("-","")
	#CONDIÇÃO: SE O TEXTO FOR IGUAL A "/FALE" SIGNIFICA QUE O USUÁRIO DIGITOU UM COMANDO VAZIO
	if update.message.text == "/fale":
		#ENVIA MENSAGEM AVISANDO QUE O COMANDO ESTÁ VAZIO
		update.message.reply_text(f"<b>👩‍💻-Sei falar, mas, não sou profeta. Que tal digitar o comando com o texto que deseja que eu fale?</b>","html")
	#CASO O COMANDO NÃO ESTEJA VAZIO...
	else:
		#PEGA O ID DO CHAT RECORRENTE (GRUPO/PRIVADO)
		chat_id = update.message.chat.id
		#RECEBE AS INSTRUÇÕES
		tts = gTTS(text=f"{texto}", lang='pt-br')
		#SALVA O AUDIO
		tts.save(f"{audio}.ogg")
		#ENVIA O AUDIO AO USUÁRIO
		levanta_baiano.send_audio(chat_id=chat_id, audio=open(f"{audio}.ogg", 'rb'))
		#APAGA O AUDIO PARA REDUZIR O USO DE MEMÓRIA
		os.system(f"rm {audio}.ogg")


#AQUI ESTÁ O HANDLER DO MÓDULO 1: COMANDO /PY3
def python3(update: Update, context) -> None:
	#IGNORA O COMANDO E PEGA SOMENTE O TEXTO
	texto = (fatmsg(update))
	#SE O TEXTO FOR IGUAL A "/py3" SIGNIFICA QUE O COMANDO ESTÁ VAZIO
	if update.message.text.lower() == "/py3":
		#ENVIA UMA MENSAGEM INFORMATIVA PARA O COMANDO VAZIO
		update.message.reply_text("<b>👩‍💻-Que tal me informar o código que deseja eu execute?</b>","html")
	#SE NÃO ESTIVER VAZIO...
	else:
		#FAZ REQUESIÇÃO À API QUE VAI EXECUTAR O CÓDIGO
		saida = requests.get(f"https://pythonencode-api1.herokuapp.com/python3run.py?source_id={source_id}&codigo={texto}").text
		#ENVIA A RESPOSTA PARA O USUÁRIO
		update.message.reply_text(f"<b>SAÍDA: </b><pre>{saida}</pre>","html")


#AQUI ESTÁ O HANDLER DO MÓDULO 1: COMANDO DE ID
def info(update: Update, context) -> None:
		#PEGA O ID DO USUÁRIO
		id = update.message.from_user.id
		#PEGA O USERNAME DO USUÁRIO
		username = f"@{update.message.from_user.username}".replace("@None","SEM NOME DE USUÁRIO")
		#PEGA O NOME DO USUÁRIO
		name = update.message.from_user.first_name
		#ENVIA OS DADOS SOLICITADOS
		update.message.reply_text(f"""<b>👾CERTIFICADO DE BAIANO👾</b>

<b>┌👩‍💻-USERNAME
└{username}</b>

<b>┌👣-ID
└</b><pre>{id}</pre>

<b>┌🗣-NOME
└</b><pre>{name}</pre>

<b>👾CERTIFICADO DE BAIANO👾</b>""","html")



#FILTRO PARA O CHECKER LOTTER
corda_da.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, chk_lotter))

#COMANDO DE START
corda_da.dispatcher.add_handler(CommandHandler("start", start))

#COMANDO DE PING
corda_da.dispatcher.add_handler(CommandHandler("ping", ping))

#COMANDO DE FALA
corda_da.dispatcher.add_handler(CommandHandler("fale", fale))

#COMANDO DE EXECUÇÃO DE CÓDIGO PYTHON3
corda_da.dispatcher.add_handler(CommandHandler("py3", python3))

#COMANDO DE INFO/ID
corda_da.dispatcher.add_handler(CommandHandler("id", info))
corda_da.dispatcher.add_handler(CommandHandler("info", info))

#INICIA O LOOP
corda_da.start_polling()
corda_da.idle()
