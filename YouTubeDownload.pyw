from pytube import YouTube
from tkinter import *
import threading 
from tkinter import messagebox,ttk
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import webbrowser


class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        root.resizable(False, "600")
        self.root.title("Magic YT")
        self.root.configure(bg="lightblue")
        #self.root.iconbitmap("icon.ico")
        self.root.bind("<Return>",self.show_quality_options)

        self.frame = Frame(self.root, bg ="lightgrey",relief=RIDGE)
        self.frame.pack(fill=BOTH,pady=5,padx=5)
        self.link = Entry(self.frame,font="consolas 15",width=45)
        self.link.pack(pady=10,padx=15)
        
        #########################################################################################
        image = Image.open("download.png")
        resized_image = image.resize((170, 80), Image.LANCZOS)
        self.download_img = ImageTk.PhotoImage(resized_image)
        self.down = Button(self.root,image=self.download_img,bg="lightblue",activebackground="lightblue", text="Download", font="consolas 20",bd = 0,command=self.start_download)
        self.down.pack()
        #########################################################################################

        self.quality_var = StringVar(value="720p")

        self.frame_social = Frame(self.root, bg="lightcyan",relief=RAISED)
        self.frame_social.pack(fill=BOTH,side=BOTTOM)

        self.promo = Label(self.frame_social,text="Follow Us On: ",font="Dungeon 16",bg="lightcyan")
        self.promo.grid(column=0,row=1,padx = 5, pady=5)
        ################################################################
        #Twitter
        image = Image.open("twitter.png")
        resized_image0 = image.resize((50, 50), Image.LANCZOS)  # Resize image to 50x50 pixels
        self.twitter_img = ImageTk.PhotoImage(resized_image0)  # Keep a reference to the resized image
        
        self.twitter = Button(self.frame_social,text="Twitter",image=self.twitter_img,bg="lightcyan",bd=0,command=lambda: webbrowser.open("https://x.com/Mrs0lver"))
        self.twitter.grid(column=1,row=1,padx=20,pady=10)
        ############################################################
        ############################################################
        #YouTube
        image = Image.open("youtube.png")
        resized_image1 = image.resize((50, 50), Image.LANCZOS)  # Resize image to 50x50 pixels
        self.youtube_img = ImageTk.PhotoImage(resized_image1)  # Keep a reference to the resized image
        
        self.youtube = Button(self.frame_social,text="YouTube",image=self.youtube_img,bg="lightcyan",bd=0,command=lambda: webbrowser.open("https://www.youtube.com/@Mrs0lver"))
        self.youtube.grid(column=2,row=1,padx=20,pady=10)
        #############################################################
        #############################################################
        #GitHub
        image = Image.open("github.png")
        resized_image2 = image.resize((60, 60), Image.LANCZOS)  # Resize image to 50x50 pixels
        self.github_img = ImageTk.PhotoImage(resized_image2)  # Keep a reference to the resized image
        
        self.github = Button(self.frame_social,text="GitHub",image=self.github_img,bg="lightcyan",activebackground="lightcyan",bd=0,command=lambda: webbrowser.open("https://github.com/MrS0lver"))
        self.github.grid(column=3,row=1,padx=20,pady=10)
    
    def show_quality_options(self,event):
        self.quality_label = Label(self.frame, text="Select Quality:",font="16")
        self.quality_label.pack(pady=5)
        
        self.quality_var = StringVar()
        self.quality_combobox = Combobox(self.frame, textvariable=self.quality_var)
        self.quality_combobox['values'] = ("720p", "480p", "360p")
        self.quality_combobox.current(0)  # default value
        self.quality_combobox.pack(pady=5)
        self.frame.pack(pady=10)

    def start_download(self):
        link = self.link.get()
        quality = self.quality_var.get()

        # Validate the link
        if not link:
            messagebox.showerror("Error", "Please enter a YouTube link")
            return

        # Start the download in a separate thread
        threading.Thread(target=self.download_video, args=(link, quality)).start()

    def download_video(self, link, quality):
        try:
            yt = YouTube(link)
            stream = yt.streams.filter(res=quality, file_extension='mp4').first()

            if not stream:
                messagebox.showerror("Error", f"No stream available for {quality}")
                return

            # Download video
            stream.download()
            messagebox.showinfo("Success", f"Video downloaded in {quality} quality")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {str(e)}")

if __name__ == "__main__":
    win = Tk()
    obj = Main(win)
    win.mainloop()
