from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
import requests, telegram, os
from gtts import gTTS
from dados import BOT_TOKEN, POST_CANAL

#TROQUE POR SEU TOKEN
rede_do_baiano = f"{1978585012:AAH5twyVYxgpKkF1QDMSBbZoJBayLpf9TSs}"
source_id = "0xO01x3701"
corda_da = Updater(f"{rede_do_baiano}")
levanta_baiano = telegram.Bot(token=f"{rede_do_baiano}")

fatmsg = lambda update: update.message.text[update.message.entities[0].length +1:]

def start(update: Update, context) -> None:
	update.message.reply_text("""▫️<b>Olá Amigo seja bem vindo ao Anti Looter aprimorado por @Kevin71, 
me adcione no seu grupo e me de permisões de ADMINISTRADOR para que eu possa banir todos os lotter.</b>""","html")


def ping(update: Update, context) -> None:
	update.message.reply_text(f"<b>Sistema Online = 🟢</b>""","html")

def chk_lotter(update: Update, context) -> None:
	for acao in update.message.new_chat_members:
		user_grupo = update.message.chat.username
		user_id = acao.id
		user_username = acao.username
	    canal = update.message.chat.id
		canal_user = update.message.chat.username
		grupo = update.message.chat.id
		try:
			resultado = requests.get(f"https://pythonencode-api1.herokuapp.com/checklotter.py?user_id={user_id}&source_id={source_id}").json()["status"]
		except:
			update.message.reply_text(f"""<b>Servidores Indisponiveis</b>""","html")
	
		if resultado == "True":
			levanta_baiano.sendMessage(POST_CANAL, f"""<b>☠🚨UM LOTTER ENTROU NO GRUPO @{user_grupo}!🚨☠

┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>O usuário foi encontrado na lista de lotters, e o mesmo foi removido com sucesso!</pre>

<b>❤️‍🔥GRUPO SEGURO - ANTI LOTTER❤️‍🔥

GRUPO: @REVOADA71
""", "html")
			#ENVIA MENSAGEM DE ALERTA PARA O GRUPO (ALERTA: CONTÉM CRÉDITOS, NÃO REMOVA)
			update.message.reply_text(f"""<b>☠🚨UM LOTTER ENTROU NO GRUPO @{user_grupo}!🚨☠

┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>O usuário foi encontrado na lista de lotters, e o mesmo foi removido com sucesso!</pre>

<b>❤️‍🔥GRUPO SEGURO - ANTI LOTTER❤️‍🔥

GRUPO: @REVOADA71
""", "html")

			try:
				levanta_baiano.ban_chat_member(user_id=user_id, chat_id=grupo)
				update.message.reply_text(f"""<b>GRUPO LIMPO (LOTTER BANIDO)

Lotter removido com sucesso!❤️‍🔥

┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>O usuário foi encontrado na lista de lotters. O bot baniu o usuário conforme a escolha do dono ao dar permissão para o bot banir lotters!</pre>

<b>❤️‍🔥GRUPO Seguro❤️‍🔥
""","html")

				levanta_baiano.send_audio(chat_id=grupo, audio=open("banido.mp3", 'rb'))

				
				
			except telegram.error.BadRequest:
				#MENSAGEM DE BAN MAU SUCEDIDO
				update.message.reply_text(f"""<b>🔻FALHA AO BANIR🔻</b>

<b>┌USERNAME┐
┝@{user_username}
┝ID┐
└</b><pre>{user_id}</pre>


<b>👾RESUMO: </b><pre>PERMISSÕES DE ADMINISTRADOR NECESSARIAS""","html")
				levanta_baiano.send_audio(chat_id=grupo, audio=open("papa_kill.mp3", 'rb'))



def fale(update: Update, context) -> None:
	texto = (fatmsg(update))
	id = f"{update.message.from_user.id}"
	if update.message.text == "/fale":
		update.message.reply_text(f"<b>👩‍💻-Sei falar, mas, não sou profeta. Que tal digitar o comando com o texto que deseja que eu fale?</b>","html")
	else:
		chat_id = update.message.chat.id
		tts = gTTS(text=f"{texto}", lang='pt-br')
		tts.save(f"{audio}.ogg")
		levanta_baiano.send_audio(chat_id=chat_id, audio=open(f"{audio}.ogg", 'rb'))
		os.system(f"rm {audio}.ogg")


def python3(update: Update, context) -> None:
	texto = (fatmsg(update))
	if update.message.text.lower() == "/py3":
		update.message.reply_text("<b>👩‍💻-Que tal me informar o código que deseja eu execute?</b>","html")
	else:
		saida = requests.get(f"https://pythonencode-api1.herokuapp.com/python3run.py?source_id={source_id}&codigo={texto}").text
		update.message.reply_text(f"<b>SAÍDA: </b><pre>{saida}</pre>","html")


def info(update: Update, context) -> None:
		id = update.message.from_user.id
		username = f"@{update.message.from_user.username}".replace("@None","SEM NOME DE USUÁRIO")
		name = update.message.from_user.first_name
		update.message.reply_text(f"""<b>👾CERTIFICADO DE BAIANO👾</b>

<b>┌👩‍💻-USERNAME
└{username}</b>

<b>┌👣-ID
└</b><pre>{id}</pre>

<b>┌🗣-NOME
└</b><pre>{name}</pre>

<b>👾CERTIFICADO REVOADA 👾</b>""","html")



corda_da.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, chk_lotter))
corda_da.dispatcher.add_handler(CommandHandler("start", start))
corda_da.dispatcher.add_handler(CommandHandler("ping", ping))
corda_da.dispatcher.add_handler(CommandHandler("fale", fale))
corda_da.dispatcher.add_handler(CommandHandler("py3", python3))
corda_da.dispatcher.add_handler(CommandHandler("id", info))
corda_da.dispatcher.add_handler(CommandHandler("info", info))
corda_da.start_polling()
corda_da.idle()
