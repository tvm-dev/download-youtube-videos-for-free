Aqui está o passo a passo que você pode inserir no arquivo `README.md` do GitHub, explicando como baixar e executar o programa. Segui uma estrutura clara para que qualquer pessoa possa facilmente configurar e rodar o aplicativo.

```markdown
# Video Downloader

Este é um programa que permite baixar vídeos e áudios do YouTube, com opção de escolher a resolução do vídeo. Ele utiliza `yt-dlp` para o download e `ffmpeg` para processar os arquivos.

## Requisitos

Antes de começar, certifique-se de que você possui os seguintes requisitos instalados no seu sistema:

1. Python 3.x
2. [yt-dlp](https://github.com/yt-dlp/yt-dlp) (uma alternativa ao youtube-dl)
3. [ffmpeg](https://ffmpeg.org/download.html)

### Passo 1: Clonando o Repositório

Primeiro, clone o repositório do GitHub para o seu computador:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Passo 2: Instalando as Dependências

Você precisará instalar as dependências do Python para rodar a interface gráfica. O principal pacote necessário é o `tkinter` (que já vem com a maioria das distribuições do Python), mas também será usado o `ttk` para a barra de progresso. Adicionalmente, o `yt-dlp` e `ffmpeg` são necessários.

#### Para instalar `yt-dlp`:

No terminal, execute o comando:

```bash
pip install yt-dlp
```

#### Adicionar o Caminho do `ffmpeg` ao Sistema

Baixe o `ffmpeg` [neste link](https://ffmpeg.org/download.html) e extraia-o em uma pasta no seu computador. Depois, adicione o caminho do `ffmpeg.exe` nas variáveis de ambiente do sistema ou mantenha o arquivo `ffmpeg.exe` na mesma pasta que o script.

### Passo 3: Executando o Programa

Você pode rodar o programa diretamente no terminal com Python:

```bash
python script.py
```

### Passo 4: Criando um Executável (Opcional)

Caso queira transformar o programa em um executável (.exe) para distribuir para outros usuários, siga os passos abaixo.

#### Instalando o PyInstaller

Você precisará do `PyInstaller` para gerar o executável. Para instalar, use o comando:

```bash
pip install pyinstaller
```

#### Criando o Executável

Na mesma pasta onde o arquivo `script.py` está, execute o seguinte comando para gerar o executável:

```bash
pyinstaller --onefile --add-binary "ffmpeg.exe:." script.py
```

Esse comando irá gerar um executável na pasta `dist/`.

### Passo 5: Executando o Arquivo Executável

Após gerar o executável, você pode rodá-lo diretamente, sem precisar instalar o Python ou qualquer dependência. O arquivo estará localizado na pasta `dist` dentro do diretório do projeto.

Para executar o programa no Windows:

1. Navegue até a pasta `dist`.
2. Execute o arquivo `script.exe`.

### Passo 6: Usando o Programa

1. **Digite a URL do vídeo** do YouTube no campo fornecido.
2. **Escolha se deseja baixar vídeo ou áudio**.
3. **Selecione a resolução** do vídeo (se estiver baixando vídeo).
4. Clique em **Baixar** e o progresso será mostrado na barra de progresso.

Ao final do download, você será notificado sobre a conclusão.

### Contribuições

Se encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
```

### Estrutura do Arquivo

- **Requisitos:** Descreve as ferramentas que precisam ser instaladas antes de executar o programa.
- **Passos para Clonar e Configurar:** Mostra como baixar o código e instalar as dependências.
- **Criando um Executável (Opcional):** Para quem deseja gerar um executável para distribuição.
- **Instruções de Uso:** Orienta sobre o uso do programa diretamente na interface gráfica.

Esse formato vai guiar qualquer pessoa a rodar o projeto corretamente.