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





#FILTRO PARA O CHECKER LOTTER
corda_da.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, chk_lotter))

#COMANDO DE START
corda_da.dispatcher.add_handler(CommandHandler("start", start))

#COMANDO DE PING
corda_da.dispatcher.add_handler(CommandHandler("ping", ping))

#INICIA O LOOP
corda_da.start_polling()
corda_da.idle()
