def imaplib():
    import imaplib
    import email

    SRV = "imap.gmail.com"
    USER = "conciliacao.cartao@supernosso.com.br"
    PASS = "oatrac.oacailicnoc"

    mail = imaplib.IMAP4_SSL(SRV)
    mail.login(USER, PASS)

    (mail.list())
    (mail.select(mailbox="INFOCARDS")) #ALTERAR MARCADOR
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
for _, _, arquivo in os.walk(r'C:\TESTE'):
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
            ssh.connect(r'kenia.supernosso.intra', username="desenvolvimento", password="@SuperNosso.2017")
            sftp = ssh.open_sftp()
            localpath = "C:\\TESTE\\"+file
            remotepath = r'/u02/oradata/orcl/testebolivia/'+file
            sftp.put(localpath, remotepath)
            sftp.close()
            ssh.close()
            source = "C:\\TESTE\\"+file
            destination = "C:\\DESTINO\\"+file
            os.rename(source, destination)
except IndexError:
    pass        
else:
    sys.exit()