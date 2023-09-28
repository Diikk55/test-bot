### libs ###
from telebot import TeleBot  # pip install telebot ou pip install pytelegrambotapi
from telebot import types  # ^^
import sqlite3
import datetime
from time import sleep
import re  # regex
## config adm ####
##Criador Ofc @DedHack3r Canal @medsermethods

notifica_adm = {"chave": "y"}  # y para ativo n para desligado

adm = {"admin": '6274566513', "user": "@DedHack3r"}

msg_menu_inicial = """Olá Seja Bem vindo!!
‌
Bem vindo a melhor store de logins do telegram 🤩
Faça recargas rapidas pelo bot💰
FACILITE SUAS APROVAÇÕES 💵✔️
⚠️ Acesse pelo navegador 4G 
Todos os loggins com compras aprovadas!
⚠️ 10 min pra acessar e conferir qualquer divergência 
⚠️ Não garanto sua aprovação e nem trampo 
Garantia de loggin antigo com compras aprovada ✅

🆘 Suporte: @DedHack3r
<a href='https://telegra.ph/%F0%9D%96%92-%F0%9D%96%8A-%F0%9D%96%89-%F0%9D%96%98-%F0%9D%96%8A-%F0%9D%96%97-05-12'>.</a> """
msg_bem_vindo_adm = "Ola adm :) !\n Sejam bem vindo a Administração Do bot"

msg_sem_produtos = "Estamos sem estoque :( "
msg_adcionar_saldo = "Para Adicionar Saldo Envia valor acima de 20$.                                                    chave pix: Sua Chave pixxxxxxxxxxxxxxx                       apos isso envie me o comprovante: @DedHack3r"
msg_produtos_admin = " click no botao para adcionar um novo login adm :) "
bot_name = "@userdoseubott"

bt_volta_msg = "🔙 Voltar🔙"

msg_compra_efetuda = " Compra efetuada com sucesso ✔️ "
msg_vc_n_Tem_Saldo = " sem saldo suficiente "
msg_sem_resultado = "Não Encontrado ❎"

usuario_cadastrado_no_bot = " Novo usuario entrou no bot  🥳 \n\n"
saldo_resgatado = " Saldo Resgatado com sucesso ✔️ \n\n"
gift_gerrado = "🏷 GIFT CARD GERADO! "
token_bot = "6094148159:AAGyQOzedn2kGujIs88X4fok0AFMF0QVQUw"  # TOKEN DO SEU BOT

saldo_inical_do_usuario = 10
## config banco , n mwexa em nada aqui ##
usuario_banco_de_dados = sqlite3.connect(
    "usuarios.db", check_same_thread=False)
cursor_usuario = usuario_banco_de_dados.cursor()
### db gift  ###
gift_banco_de_Dados = sqlite3.connect("gift.db", check_same_thread=False)
cursor_gift = gift_banco_de_Dados.cursor()

### config produtos ###
logins_loja = ['Americanas', 'Casas Bahia',
               'Magazine Luiza', 'Kabum', 'Olx']

logins_back = ['Sumup', 'Pagbank']

logins_filmes = ['Spotify Premium', 'Disney', 'Prime vídeo']

outros_login = ["Sympla", "Uol Mail"]

VALORES = {"Americanas": 30, "Casas_Bahia": 25, "Magazine_Luiza": 30,
           "Kabum": 10, "Disney": 10, "Prime_vídeo": 15, "Sympla": 60, "Uol_Mail": 20, "Olx": 20, "Sumup": 100, "Pagbank": 130, "Spotify_Premium": 15}
a = VALORES


msg_produtos = f" \n <b>Americanas</b>: <i> R$ {a['Americanas']}</i>\n<b>Casas Bahia</b>: <i> R$  {a['Casas_Bahia']}</i>\n<b>Magazine Luiza</b>:<i> R$  {a['Magazine_Luiza']}</i>\n<b>Kabum </b>: <i> R$ {a['Kabum']}</i>\n<b>Disney</b>:<i> R$ {a['Disney']}</i>\n<b>Prime vídeo</b>:<i> R$ {a['Prime_vídeo']}</i>\n<b>Sympla</b>:<i> R$ {a['Sympla']}</i>\n<b>Uol Mail</b>:<i> R$ {a['Uol_Mail']}</i>\n<b>Olx</b>: <i> R$ {a['Olx']}</i>\n<b>Sumup</b>: <i> R$ {a['Sumup']}</i>\n<b>Pagbank</b>: <i> R$ {a['Pagbank']}</i>\n<b>Spotify Premium</b>:<i> R$ {a['Spotify_Premium']}</i>"
### 3 PRODUDOS DB #####

# CRIAR TABLE ##
banco_produtos = sqlite3.connect("prudutos.db", check_same_thread=False)
cursor_prudotos = banco_produtos.cursor()


def comprar_produto(id, op):
    saldo = f"SELECT saldo FROM usuario WHERE id ='{id}' "
    infor = cursor_usuario.execute(saldo).fetchall()[0][0]
    if VALORES[op] > int(infor):
        return "n"
    else:

        if int(cursor_prudotos.execute(f"SELECT COUNT(id) FROM {op}").fetchall()[0][0]) > 0:
            pass
        else:
            return "o"
        sql = f"SELECT * FROM {op} WHERE 1 ORDER BY RANDOM() LIMIT 1"
        produto = cursor_prudotos.execute(sql).fetchall()[0][0]

        sql = f"DELETE FROM {op} WHERE id = '{produto}'"
        cursor_prudotos.execute(sql)
        banco_produtos.commit()

        #### tira o valor do usuario ####
        soma = int(infor) - int(VALORES[op])

        sql = f"UPDATE usuario SET saldo='{soma}' WHERE id='{id}'"

        cursor_usuario.execute(sql)
        usuario_banco_de_dados.commit()

        texto = f"{msg_compra_efetuda}<b>\n\n🆔 ID da carteira</b>:{id}\n\n<b>📅 Data da Compra</b>:{datetime.datetime.today()}\n<b>💰 Saldo Anterior</b>:{infor}\n<b>💰 Saldo Atual</b>: {soma}\n<b>Seu Produto</b>:{produto}"

        return texto


def criar_logins(mensagem, op):
    msg = mensagem.text
    op = op.replace('1', "")
    lista = ["y", "Y"]
    if msg in lista:
        x = bot.reply_to(mensagem, " Operação cancelada ")
        sleep(1)
        bot.delete_message(chat_id=mensagem.chat.id, message_id=x.id)
    else:
        sql = f"INSERT INTO {op}(id) VALUES ('{msg}')"
        try:
            cursor_prudotos.execute(sql)
            banco_produtos.commit()
            bot.reply_to(
                mensagem, text=f" Foram adcionado com sucesso \n\n{msg}")
        except:
            bot.reply_to(
                mensagem, text=" Evite aspas ' , evite caractere fodss mmmkkkkk ")


def criar_table_produtos():
    resultado = "resultado\n"
    for nome in logins_loja:
        nome = nome.replace(" ", "_")

        sql = f"CREATE TABLE {nome} (id text primary key)"

        cursor_prudotos.execute(sql)
        resultado = resultado + f"Tabela {nome} ✅\n"

    for nome in logins_back:
        nome = nome.replace(" ", "_")
        sql = f"CREATE TABLE {nome} (id text primary key)"
        cursor_prudotos.execute(sql)
        resultado = resultado + f"Tabela {nome} ✅\n"

    for nome in logins_filmes:
        nome = nome.replace(" ", "_")
        sql = f"CREATE TABLE {nome} (id text primary key)"
        cursor_prudotos.execute(sql)
        resultado = resultado + f"Tabela {nome} ✅\n"

    for nome in outros_login:
        nome = nome.replace(" ", "_")
        sql = f"CREATE TABLE {nome} (id text primary key)"
        cursor_prudotos.execute(sql)
        resultado = resultado + f"Tabela {nome} ✅\n"
    return resultado


def vender_produtos_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    for nome in logins_loja:
        table = nome.replace(" ", "_") + '1'
        nome = nome.upper()

        bt = types.InlineKeyboardButton(
            text=nome, callback_data=table)
        keyboard.add(bt)

    for nome in logins_back:
        table = nome.replace(" ", "_") + '1'
        nome = nome.upper()
        bt = types.InlineKeyboardButton(
            text=nome, callback_data=table)
        keyboard.add(bt)
    for nome in logins_filmes:
        table = nome.replace(" ", "_") + '1'
        nome = nome.upper()
        bt = types.InlineKeyboardButton(
            text=nome, callback_data=table)
        keyboard.add(bt)

    for nome in outros_login:
        table = nome.replace(" ", "_") + '1'
        nome = nome.upper()
        bt = types.InlineKeyboardButton(
            text=nome, callback_data=table)
        keyboard.add(bt)
    return keyboard


def volta_compras_user():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bt0 = types.InlineKeyboardButton(
        text=bt_volta_msg, callback_data="volta_compras")
    keyboard.add(bt0)

    return keyboard


def vender_produtos_keyboard_user():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    bt0 = types.InlineKeyboardButton(
        text='AMERICANAS', callback_data='Americanas')
    bt1 = types.InlineKeyboardButton(
        text='CASAS BAHIA', callback_data='Casas_Bahia')
    bt2 = types.InlineKeyboardButton(
        text='MAGAZINE LUIZA', callback_data='Magazine_Luiza')
    bt3 = types.InlineKeyboardButton(text='KABUM', callback_data='Kabum')
    bt4 = types.InlineKeyboardButton(text='OLX', callback_data='Olx')
    bt5 = types.InlineKeyboardButton(text='SUMUP', callback_data='Sumup')
    bt6 = types.InlineKeyboardButton(text='PAGBANK', callback_data='Pagbank')
    bt7 = types.InlineKeyboardButton(
        text='SPOTIFY PREMIUM', callback_data='Spotify_Premium')
    bt8 = types.InlineKeyboardButton(text='DISNEY', callback_data='Disney')
    bt9 = types.InlineKeyboardButton(
        text='PRIME VÍDEO', callback_data='Prime_vídeo')
    bt10 = types.InlineKeyboardButton(text='SYMPLA', callback_data='Sympla')
    bt11 = types.InlineKeyboardButton(
        text='UOL MAIL', callback_data='Uol_Mail')
    bt12 = types.InlineKeyboardButton(
        text=bt_volta_msg, callback_data="menu_inicial")
    keyboard.add(bt0, bt1, bt2, bt3, bt4, bt5, bt6,
                 bt7, bt8, bt9, bt10, bt11, bt12)
    return keyboard

#### botoes ####


def cadastra_usuario(id):
    sql = f"SELECT * FROM usuario WHERE id ='{id}' "
    infor_user = cursor_usuario.execute(sql).fetchall()
    if infor_user == []:
        hora_de_cadastro = datetime.datetime.today()
        sql = f"INSERT INTO usuario(id,hora,saldo) VALUES ('{id}','{hora_de_cadastro}','{saldo_inical_do_usuario}')"
        cursor_usuario.execute(sql)
        usuario_banco_de_dados.commit()
        return "y"
    else:
        return None
#### usuarios no bot ####


def volta_tela_inicial():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bt0 = types.InlineKeyboardButton(
        text=bt_volta_msg, callback_data="menu_inicial")
    keyboard.add(bt0)
    return keyboard


def msg_usuarios(mensagem):
    msg = mensagem.text
    if mensagem.text == 'y':
        return bot.reply_to(mensagem, " Operaçao cancelada ")
    msgs_enviadas = 0
    msgs_nao_enviadas = 0
    sql = f"SELECT id FROM usuario"
    infor_user = cursor_usuario.execute(sql).fetchall()
    for ids in infor_user:

        users = ids[0]
        try:
            bot.send_message(chat_id=users, text=msg)
            msgs_enviadas = msgs_enviadas + 1
        except:
            msgs_nao_enviadas = +1
    texto = f"Mensagems Recebidas:{msgs_enviadas}✅\n\nMensagens Não Recebidas: {msgs_nao_enviadas} ❌"

    bot.send_message(chat_id=mensagem.chat.id, text=texto)


def keyboard_bem_vindo():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bt0 = types.InlineKeyboardButton(text="🛒 Comprar Logins", callback_data="logins_tab")
    bt1 = types.InlineKeyboardButton(text="👤 Perfil", callback_data="perfil")
    bt2 = types.InlineKeyboardButton(
        text=" 💵 Adicionar Saldo ", callback_data="saldo")
    keyboard.add(bt0, bt1, bt2)
    return keyboard


def keyboard_admin():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    bt0 = types.InlineKeyboardButton(
        text="Enviar mensagem Para todos 📧  ", callback_data="enviar_msg_todos")
    bt1 = types.InlineKeyboardButton(
        text=" ativa / desativa Notificações 🔇/🔊   ", callback_data="notificar")
    bt2 = types.InlineKeyboardButton(
        text="Criar banco de dados  💹  ", callback_data="banco_all")
    bt3 = types.InlineKeyboardButton(
        text="Gerar Gift 🎰 ", callback_data="gerra_gift")
    bt4 = types.InlineKeyboardButton(
        text="Total de Usuarios 📊", callback_data="count_user")
    bt5 = types.InlineKeyboardButton(
        text="Total de gift Gerado  ✅ ", callback_data="count_gift")
    bt6 = types.InlineKeyboardButton(
        text="Criar Tabelas produtos  ✅ ", callback_data="produtos_table")
    bt7 = types.InlineKeyboardButton(
        text="Adcionar os Logins ✅ ", callback_data="add_logins")
    keyboard.add(bt0, bt1, bt2, bt3, bt4, bt5, bt6, bt7)

    return keyboard


def volta_adm():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bt0 = types.InlineKeyboardButton(
        text=bt_volta_msg, callback_data="admin_volta")
    return keyboard.add(bt0)
####### funçoes do bot ########


def ver_saldo_USER(id):
    sql = f"SELECT saldo FROM usuario WHERE id ='{id}' "
    infor = cursor_usuario.execute(sql).fetchall()[0][0]
    VALOR = int(infor)
    return VALOR


def gift_gerar(valor):
    import random
    usada = "0"
    gera_gift = random.choice(range(0, 100000000000))

    sql = f"INSERT INTO gift(id,saldo,usada) VALUES ('{gera_gift}','{valor}','{usada}') "

    #### SALVANDO AS INFOR ####

    cursor_gift.execute(sql)
    gift_banco_de_Dados.commit()

    texto = f"""
    {gift_gerrado} 🤑\n💰 Valor : {valor}\n📥 GIFT: `/gift {gera_gift}`\n🥷 USE NO BOT : {bot_name}
    """
    return texto


def valor_do_gift(mensagem):
    (mensagem)
    valor = mensagem.text
    msg_id = mensagem.message_id
    chat = mensagem.chat.id
    try:
        valor = int(valor)
    except:
        x = bot.reply_to(mensagem, " Digite apenas numero",
                         reply_markup=types.ForceReply())
        return bot.register_next_step_handler(x, valor_do_gift)

    resultado = gift_gerar(valor=valor)

    bot.reply_to(mensagem, text=resultado, parse_mode="MarkDown")


def criar_tabelas_Do_banco():
    ### criar tabela do usuArio ####

    hora_de_cadastro = datetime.datetime.today()
    sql_criar_tabela_user = "CREATE TABLE usuario(id text primary key , hora text , saldo text)"
    sql_criar_tabela_gift = "CREATE TABLE gift(id text primary key , saldo text  , usada text)"
    try:
        cursor_usuario.execute(sql_criar_tabela_user)
        usuario_banco_de_dados.commit()
        ## TABELA GIFT ##
        gift_banco_de_Dados.execute(sql_criar_tabela_gift)
        gift_banco_de_Dados.commit()
        return "CRIADO COM SUCESSO  ✅  \n\n click > /start "
    except:
        return "jA FOI TUDO CRIADO  ❌  "


    ##### CONFIG BOT ###
bot = TeleBot(token=token_bot,parse_mode="html")
####################

### INICIADO O BOT ###


@ bot.message_handler(commands=['start'], chat_types=['private'])
def start_bot(mensagem):
    bot.reply_to(mensagem, text=msg_menu_inicial,
                 reply_markup=keyboard_bem_vindo())
    if cadastra_usuario(id=mensagem.from_user.id) == "y":
        if notifica_adm["chave"] == "y":
            foto_perfil = bot.get_user_profile_photos(
                mensagem.chat.id).photos[0][2].file_id
            id_user = mensagem.chat.id
            infor = bot.get_chat(mensagem.chat.id)
            nome = infor.username
            segundo_name = infor.first_name
            last = infor.last_name
            bio = infor.bio
            link = infor.invite_link
            descriço = infor.description
            if descriço == None:
                descriço = msg_sem_resultado
            if segundo_name == None:
                segundo_name = msg_sem_resultado
            if last == None:
                last = msg_sem_resultado

            if bio == None:
                bio = msg_sem_resultado

            texto = f"{usuario_cadastrado_no_bot}Nome: {nome}\n\nID: {id_user}\n\nPrimeiro Nome: {segundo_name}\n\nSegundo Nome: {last}\n\nBio: {bio}\n\nDescriçao: {descriço}"
            bot.send_photo(chat_id=adm["admin"],
                           photo=foto_perfil, caption=texto)


@ bot.message_handler(commands=['admin'], chat_types=['private'])
def start_adm(mensagem):
    if adm["admin"] == str(mensagem.chat.id):
        pass
    else:
        return None
    bot.reply_to(mensagem, text=msg_bem_vindo_adm,
                 reply_markup=keyboard_admin())
#### 3 gift usuario ######


@ bot.message_handler(commands=['gift'], chat_types=['private'])
def gift_usar(mensagem):
    gift = mensagem.text.split()[1]
    saldo = ver_saldo_USER(id=mensagem.chat.id)

    sql_gift = f"SELECT saldo FROM gift WHERE id ='{gift}' "
    gift_ver = cursor_gift.execute(sql_gift).fetchall()

    if gift_ver == []:
        texto = "Token invalido ❌ , Voce esta tentando algo :( "
        return bot.reply_to(mensagem, text=texto)
    sql_gift = f"SELECT usada FROM gift WHERE id ='{gift}' "
    gift_ver = cursor_gift.execute(sql_gift).fetchall()[0][0]

    if int(gift_ver) == 0:
        sql = f"UPDATE gift SET usada='1' WHERE id='{gift}'"
        cursor_gift.execute(sql)
        gift_banco_de_Dados.commit()

        ##### atualizando o gift #####
        sql_gift = f"SELECT saldo FROM gift WHERE id ='{gift}' "
        gift_ver = cursor_gift.execute(sql_gift).fetchall()[0][0]
        somar = int(gift_ver) + int(saldo)
        sql = f"UPDATE usuario SET saldo='{somar}' WHERE id='{mensagem.chat.id}'"
        cursor_usuario.execute(sql)
        usuario_banco_de_dados.commit()

        texto = saldo_resgatado + \
            f"Valor anterior: {saldo}\nValor adcionado: {gift_ver}\nValor Total: {somar}"

        bot.reply_to(mensagem, text=texto)

    else:
        return bot.reply_to(mensagem, text="Gift ja foi utilizado ")


@ bot.callback_query_handler(func=lambda callback: callback.data)
def callBack_user(call):
    op = call.data

    global notifica_adm
    if call.data == "banco_all":
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=criar_tabelas_Do_banco(), reply_markup=volta_adm())
    elif call.data == "admin_volta":
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=msg_menu_inicial, reply_markup=keyboard_admin())
    elif call.data == "notificar":
        msg = None

        if notifica_adm["chave"] == "n":
            msg = " ativado  🔊  "
            notifica_adm["chave"] = "y"
            return bot.edit_message_text(chat_id=call.message.chat.id,
                                         message_id=call.message.message_id, text=msg, reply_markup=volta_adm())

        else:
            msg = " desativado  🔇   "
            notifica_adm["chave"] = "n"
            return bot.edit_message_text(chat_id=call.message.chat.id,
                                         message_id=call.message.message_id, text=msg, reply_markup=volta_adm())
    elif call.data == "gerra_gift":
        x = bot.reply_to(message=call.message, text="Digite o valor do gift ",
                         reply_markup=types.ForceReply())
        (x.id)
        bot.register_next_step_handler(x, valor_do_gift)

        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text="Digite o valor do gift ", reply_markup=volta_adm())
    elif call.data == "count_user":
        sql = "SELECT COUNT(id) FROM usuario"
        count = cursor_usuario.execute(sql).fetchall()[0][0]
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=f"Total de usuarios cadastrado :  {count}", reply_markup=volta_adm())
    elif call.data == "count_gift":
        sql = "SELECT COUNT(id) FROM gift"
        count = cursor_gift.execute(sql).fetchall()[0][0]
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=f"Total de gift gerados no bot:  {count}", reply_markup=volta_adm())
    elif call.data == "enviar_msg_todos":
        x = bot.reply_to(
            message=call.message, text="Digite Apenas texto: ", reply_markup=types.ForceReply())
        bot.register_next_step_handler(x, msg_usuarios)
        sleep(2)
        bot.delete_message(message_id=x.id, chat_id=call.message.chat.id)

        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=" Digite Apenas textos ", reply_markup=volta_adm())
    elif call.data == "produtos_table":
        try:
            resultado = criar_table_produtos()
        except:
            resultado = " ja foi tudo criado "
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=resultado, reply_markup=volta_adm())
    elif call.data == "perfil":
        infor = cursor_usuario.execute(
            f"SELECT * FROM usuario WHERE id='{call.message.chat.id}'").fetchall()[0]
        ID = infor[0]
        DATA_de_CADASTRO = infor[1]
        SALDO = infor[2]
        texto = f"📛<b>Nome</b>: {call.message.chat.first_name}\n\n<b>📅 Data de cadastro</b>: {DATA_de_CADASTRO}\n\n<b>🆔 ID da carteira </b>: {call.message.chat.id}\n\n<b>💰 Saldo</b>: {SALDO}"
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=texto, reply_markup=volta_tela_inicial(), parse_mode="html")
    elif call.data == "menu_inicial":
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=msg_menu_inicial, reply_markup=keyboard_bem_vindo(), parse_mode="html")
    elif call.data == "add_logins":
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=msg_produtos_admin, reply_markup=vender_produtos_keyboard(), parse_mode="html")
    if re.search("1", op):

        x = bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text=f" Digite as informaçoes para adcionar na tabela {op} \n\nDigite y para cancelar ", reply_markup=volta_adm(), parse_mode="html")

        return bot.register_next_step_handler(x, criar_logins, op)
    if call.data == "logins_tab":
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=msg_produtos, reply_markup=vender_produtos_keyboard_user(), parse_mode="html")

    elif call.data == "volta_compras":
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=msg_produtos, reply_markup=vender_produtos_keyboard_user(), parse_mode="html")
    elif call.data == "saldo":
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=msg_adcionar_saldo, reply_markup=volta_tela_inicial(), parse_mode="html")
    else:

        a = comprar_produto(id=call.message.chat.id, op=op)
        if a == "n":
            return bot.answer_callback_query(callback_query_id=call.id, text=msg_vc_n_Tem_Saldo, show_alert=True)
        elif a == "o":
            return bot.answer_callback_query(callback_query_id=call.id, text=msg_sem_produtos, show_alert=True)
        return bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id, text=f"{a}", reply_markup=volta_compras_user(), parse_mode="html")


        ### run bot ###
bot.infinity_polling()
