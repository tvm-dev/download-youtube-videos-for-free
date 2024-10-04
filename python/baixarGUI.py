import os
import subprocess
import re
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from tqdm import tqdm

# Caminho padrão para o local de download
download_dir = os.getcwd()  # Diretório atual como padrão

# Função para baixar vídeo e mesclar manualmente
def download_video(url, format_option):
    # Pegando o caminho completo do ffmpeg.exe
    ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ffmpeg.exe')

    # Comando para o yt-dlp, baixando diretamente em MKV
    video_output = os.path.join(download_dir, '%(title)s.%(ext)s')
    command = [
        'yt-dlp',
        *format_option,
        '--ffmpeg-location', ffmpeg_path,  # Passando o caminho absoluto do ffmpeg
        '-o', video_output,  # Nome do arquivo de saída
        url
    ]

    # Executa o processo yt-dlp
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Exibe a barra de progresso
    with tqdm(total=100, desc='Download Progress', unit='%', bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} - {elapsed}') as pbar:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
                match = re.search(r'(\d+.\d+)% of', output)  # Capturando a porcentagem corretamente
                if match:
                    percent = float(match.group(1))
                    pbar.n = percent
                    pbar.refresh()  # Atualiza a barra de progresso

    # Finaliza o processo de download
    _, error = process.communicate()

    # Verifica se o download foi bem sucedido
    if process.returncode == 0:
        messagebox.showinfo("Sucesso", f"Download concluído com sucesso na pasta: {download_dir}")
    else:
        messagebox.showerror("Erro", f"Erro ao baixar vídeo: {error.strip()}")

# Função para iniciar o download
def start_download():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Atenção", "Por favor, insira a URL do vídeo.")
        return

    format_option = []
    
    if download_type.get() == "Audio":
        format_option = ['-x', '--audio-format', 'mp3']
    else:
        quality = resolution_combobox.get()
        # Mudança no formato para MKV
        format_option = [f'-f bestvideo[height<={quality}]+bestaudio/best', '--merge-output-format', 'mkv']

    download_video(url, format_option)

# Função para escolher o local de download
def choose_directory():
    global download_dir
    download_dir = filedialog.askdirectory()
    if download_dir:
        directory_label.config(text=f"Local de Download: {download_dir}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Downloader de Vídeo")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Label para URL
url_label = tk.Label(root, text="Digite a URL do vídeo do YouTube:", bg="#f0f0f0")
url_label.pack(pady=10)

# Entrada para URL
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Opções de download
download_type = tk.StringVar(value="Video")  # Padrão para vídeo
video_radio = tk.Radiobutton(root, text="Vídeo", variable=download_type, value="Video", bg="#f0f0f0")
audio_radio = tk.Radiobutton(root, text="Áudio", variable=download_type, value="Audio", bg="#f0f0f0")
video_radio.pack(anchor=tk.W, padx=10)
audio_radio.pack(anchor=tk.W, padx=10)

# Combobox para seleção de resolução
resolution_label = tk.Label(root, text="Selecione a Resolução do Vídeo:", bg="#f0f0f0")
resolution_label.pack(pady=10)

resolution_combobox = ttk.Combobox(root, values=["144", "240", "360", "480", "720", "1080"], state="readonly")
resolution_combobox.set("720")  # Padrão para 720p
resolution_combobox.pack(pady=10)

# Botão para escolher o local de download
choose_button = tk.Button(root, text="Escolher Local de Download", command=choose_directory)
choose_button.pack(pady=10)

# Label para mostrar o local de download escolhido
directory_label = tk.Label(root, text=f"Local de Download: {os.getcwd()}", bg="#f0f0f0")
directory_label.pack(pady=10)

# Botão de Download
download_button = tk.Button(root, text="Baixar", command=start_download, bg="#4CAF50", fg="white")
download_button.pack(pady=20)

# Iniciar a aplicação
root.mainloop()
