def imaplib():
    import imaplib
    import email

    SRV = "servidor.email.com"
    USER = "email@email.com"
    PASS = "senha.email"

    mail = imaplib.IMAP4_SSL(SRV)
    mail.login(USER, PASS)

    (mail.list())
    (mail.select(mailbox="MARCADOR DE EMAIL")) #ALTERAR MARCADOR
    respostas,IdDosEmails = mail.search(None,"UnSeen")

    for i in IdDosEmails[0].split():
        resultado,dados = mail.fetch(i, "(RFC822)")
        textoDoEmail = dados[0][1]
        textoDoEmail = textoDoEmail.decode("latin-1") #ALTERAR FORMATO DE CRIPTOGRAFIA
        textoDoEmail = email.message_from_string(textoDoEmail)
        for part in textoDoEmail.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") is None:
                continue
            filename = part.get_filename()
            if filename is None: continue
            arquivo = open(filename, "wb")
            arquivo.write(part.get_payload(decode=True))
            arquivo.close
            
    
imaplib()

import os
import sys
import paramiko

pathArquivos=r'DISCO:\Pasta\SubPasta\\'
pathBackup=r'DISCO:\Pasta\SubPasta\\'
pathUnix=r'/Pasta/SubPasta/SubPasta/SubPasta/'
for _, _, arquivo in os.walk(pathArquivos):
    arq=arquivo
    param=0
try:
    if arq is not None:
        total=int(len(arq))
        while total >= 1:
            file=str(arq[param])
            param+=1
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            servidor="servidor"
            usuarioftp="usuario"
            senhaftp="senha"
            portaftp="porta"
            ssh.connect(servidor, portaftp, usuarioftp, senhaftp)
            sftp = ssh.open_sftp()
            localpath = pathArquivos+file
            print(localpath)
            remotepath = pathUnix+file
            sftp.put(localpath, remotepath)
            sftp.close()
            ssh.close()
            source = pathArquivos+file
            destination = pathBackup+file
            os.rename(source, destination)
except IndexError:
    pass        
else:
    sys.exit()
