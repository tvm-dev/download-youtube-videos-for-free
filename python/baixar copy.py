import os
import subprocess
import re
from tqdm import tqdm

# Caminho da pasta onde os vídeos serão salvos
download_dir = 'Downloaded'

# Verifica se a pasta 'Downloaded' existe, caso contrário, cria
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
    print("Pasta 'Downloaded' criada.")

def download_video(url, format_option):
    # Caminho para a pasta onde o ffmpeg está instalado (mesma pasta do script)
    ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ffmpeg.exe')

    command = [
        'yt-dlp',
        *format_option,  # Descompacta a lista de opções
        '--ffmpeg-location', os.path.dirname(ffmpeg_path),  # Adiciona o diretório do ffmpeg
        '-o',
        os.path.join(download_dir, '%(title)s.%(ext)s'),  # Formato de saída
        url
    ]

    # Executa o comando no shell e captura a saída
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Exibe a barra de progresso
    with tqdm(total=100, desc='Download Progress', unit='%', bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} - {elapsed}') as pbar:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
                # Verifica se a saída contém o progresso do download
                match = re.search(r'Downloading video (\d+)%', output)
                if match:
                    percent = int(match.group(1))
                    pbar.n = percent
                    pbar.refresh()  # Atualiza a barra de progresso

    # Aguarda o processo terminar e captura os erros
    _, error = process.communicate()
    if process.returncode == 0:
        print(f"\nDownload concluído com sucesso na pasta: {download_dir}")
    else:
        print(f"\nErro ao baixar vídeo: {error.strip()}")

def ask_for_options():
    url = input("Digite a URL do vídeo do YouTube: ")
    
    # Opção de Download
    print("Deseja baixar:")
    print("1) Vídeo")
    print("2) Apenas Áudio")
    choice = input("Digite 1 ou 2 (padrão é 1): ") or '1'

    if choice == '1':
        # Qualidade padrão é 720
        print("Escolha a qualidade:")
        print("1) 720p (padrão)")
        print("2) 1080p")
        print("3) Melhor qualidade")
        quality_choice = input("Digite 1, 2 ou 3 (padrão é 1): ") or '1'

        if quality_choice == '1':
            quality = '720'
        elif quality_choice == '2':
            quality = '1080'
        else:
            quality = 'best'

        # Define as opções para garantir que o arquivo de saída seja MKV
        format_option = [
            f'-f bestvideo[height<={quality}]+bestaudio/best',
            '--merge-output-format', 'mkv'  # Garantir que a saída seja no formato MKV
        ]
        download_video(url, format_option)

    elif choice == '2':
        # Baixar apenas o áudio em mp3
        format_option = ['-x', '--audio-format', 'mp3']  # Baixar apenas áudio em mp3
        download_video(url, format_option)
    else:
        print("Opção inválida. Tente novamente.")
        ask_for_options()  # Reinicia a pergunta

# Inicia o processo
ask_for_options()
