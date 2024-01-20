from pytube import YouTube
import os
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

def progress(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progressbar['value'] = percent
    root.update_idletasks()

def download_video():
    link = url_entry.get()
    yt = YouTube(link, on_progress_callback=progress)
    audio_ou_video = var.get()

    if audio_ou_video == 1:
        pasta_para_video = os.path.expanduser("~\\Videos")
        video = yt.streams.get_highest_resolution()
        video.download(output_path=pasta_para_video)
        messagebox.showinfo("Sucesso", f"Seu vídeo foi salvo em {pasta_para_video}. Uma janela do explorador de arquivos será aberta na pasta")
        os.startfile(pasta_para_video)
        
    elif audio_ou_video == 2:
        pasta_para_audio = os.path.expanduser("~\\Music")
        audio = yt.streams.get_audio_only()
        audio.download(output_path=pasta_para_audio)
        messagebox.showinfo("Sucesso", f"Sua música foi salva em {pasta_para_audio}. Uma janela do explorador de arquivos será aberta na pasta")
        os.startfile(pasta_para_audio)

root = tk.Tk()
root.geometry("800x600")

var = tk.IntVar()

url_label = tk.Label(root, text="URL do vídeo:", font=("Arial", 14))
url_label.pack()

url_entry = tk.Entry(root, width=70, fg="orange", font=("Arial", 14))
url_entry.pack()

video_button = tk.Radiobutton(root, text="Baixar vídeo", variable=var, value=1, font=("Arial", 14))
video_button.pack()

audio_button = tk.Radiobutton(root, text="Baixar áudio", variable=var, value=2, font=("Arial", 14))
audio_button.pack()

download_button = tk.Button(root, text="Baixar", command=download_video, font=("Arial", 14))
download_button.pack()

progressbar = ttk.Progressbar(root, length=300, mode='determinate')
progressbar.pack()

root.mainloop()
