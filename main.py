from os import listdir

arquivos = input(r'Digite o caminho da pasta -> exemplo (C:\Users\Nome\Downloads): ').replace("\\", "/")
arq_lista = listdir(arquivos)
arq_ext = []
pasta = []
outros_ext = []
arq_tipo = {
    '.png':'Imagem','.jpg':'Imagem','.jpeg':'Imagem',
    '.exe':'Executavel',
    '.pdf':'PDF',
    '.txt':'Arquivo de texto',
    '.mp4':'Audios','.mp4':'Audios',
    '.rar':'Compactados', '.zip':'Compactados',
    '.iso':'Arquivos ISO',
    '.docx':'Office', '.ppsx':'Office','.xltx' :'Office',
    'outros':'Outros',
    }


#separação dos itens da pasta
for arq in arq_lista:
    
    if '.' in arq:
        ponto = arq.rfind(".")
        extensao = arq[ponto:]   
        
        if extensao in arq_tipo and extensao not in arq_ext:
            arq_ext.append(extensao)
            
        elif extensao not in arq_tipo:
            outros_ext.append(extensao)
            
            if "outros" not in arq_ext:
                arq_ext.append("outros")
    
    else:
        pasta.append(arq)

if len(arq_ext) > 0: #Verifica se tem arquivo nas pastas
    
    for ext in arq_ext: #Criação das pastas
        #criapasta
        
else:
    print("Não movimentação a ser feita nesta pasta!")

    

        