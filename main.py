import youtube_dl
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, Checkbutton


def download_media():
    global link_entry, resolution_var, save_as_mp3_var

    link = link_entry.get()
    resolution = resolution_var.get()
    save_as_mp3 = save_as_mp3_var.get()

    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]' if not save_as_mp3 else 'bestaudio/best',
        'outtmpl': './DOWNLOADED/%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def create_interface():
    global link_entry, resolution_var, save_as_mp3_var

    interface = Tk()
    interface.title("YouTube Video İndirme Arayüzü")

    link_label = Label(interface, text="YouTube Bağlantısı:")
    link_label.grid(row=0, column=0, padx=10, pady=10)

    link_entry = Entry(interface, width=40)
    link_entry.grid(row=0, column=1, padx=10, pady=10)

    resolution_label = Label(interface, text="Çözünürlük:")
    resolution_label.grid(row=1, column=0, padx=10, pady=10)

    resolutions = ["1080", "720", "480", "360"]
    resolution_var = StringVar(interface)
    resolution_var.set(resolutions[0])

    resolution_menu = OptionMenu(interface, resolution_var, *resolutions)
    resolution_menu.grid(row=1, column=1, padx=10, pady=10)

    save_as_mp3_var = StringVar()
    save_as_mp3_checkbox = Checkbutton(interface, text="MP3 Olarak Kaydet", variable=save_as_mp3_var)
    save_as_mp3_checkbox.grid(row=2, columnspan=2, padx=10, pady=10)

    download_button = Button(interface, text="İndir", command=download_media)
    download_button.grid(row=3, columnspan=2, padx=10, pady=10)

    interface.mainloop()


if __name__ == "__main__":
    create_interface()
