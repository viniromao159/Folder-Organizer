import os
from pathlib import Path

caminho = input("Digite o caminho da pasta: ").replace('\\', '/')

lista_arquivo = os.listdir(caminho)

arq_tipo = { 
        'Imagem':['.png', '.jpg', '.jpeg'],
        'Executavel':['.exe'],    
        'PDF':['.pdf'],
        'Arquivo de texto':['.txt'],
        'Audios':['.mp3','.mp4'],
        'Compactados':['.rar','.zip'],
        'Arquivos ISO':['.iso'],
        'Office':['.docx', '.ppsx','.xltx'],
        'DLL':['.dll'],
        'Outros':['outros']
    }

filtro = []

# Loop em cada item do dicionario
for nome_pasta, extensoes in arq_tipo.items():
    #pega o valor de cada chave do dicionario, neste caso o array de extenções
    for extensao in extensoes:
        
        for arquivo in lista_arquivo:
            
            # retorna um array filtrado com o nome dos arquivos de acordo com a extenção
            if extensao in arquivo:
                filtro.append(arquivo)
                
        #Se o filtro tiver algum arquivo
        if len(filtro) > 0:
            
            for arq in filtro:
                #verifica a extensão do arquivo e cria a pasta (se necessario), e move o arquivo
                if extensao in arq:
                    Path(f'{caminho}/{nome_pasta}').mkdir(exist_ok=True)
                    os.rename(f'{caminho}/{arq}', f'{caminho}/{nome_pasta}/{arq}')
                    
        
                

    


                    
                
    
    