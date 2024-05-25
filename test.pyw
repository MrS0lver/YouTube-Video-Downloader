# from pytube import YouTube
# from tkinter import *
# from tkinter import messagebox
# import threading
# from PIL import Image, ImageTk

# class Main:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("500x300")
#         root.resizable(False, True)
#         self.root.title("Magic YT")

#         # Open and resize the image
#         image = Image.open("twitter.png")
#         resized_image = image.resize((50, 50), Image.LANCZOS)  # Resize image to 50x50 pixels
#         self.twitter_img = ImageTk.PhotoImage(resized_image)  # Keep a reference to the resized image

#         # Create the button with the resized image
#         self.button = Button(root, image=self.twitter_img, text="Click Me", compound=TOP, bd=19)
#         self.button.pack(pady=20)

#         # Entry widget for the YouTube link
#         self.link_var = StringVar()
#         self.link_entry = Entry(root, textvariable=self.link_var, width=50)
#         self.link_entry.pack(pady=10)

#         # Button to confirm the link and show quality options
#         self.confirm_button = Button(root, text="Confirm Link", command=self.show_quality_options)
#         self.confirm_button.pack(pady=5)

#         # Frame for quality options
#         self.quality_frame = Frame(root)
#         self.quality_var = StringVar(value="720p")  # Default quality

#     def show_quality_options(self):
#         # Extend the frame
#         self.root.geometry("500x400")

#         # Add radio buttons for quality selection
#         Radiobutton(self.quality_frame, text="720p", variable=self.quality_var, value="720p").pack(anchor=W)
#         Radiobutton(self.quality_frame, text="480p", variable=self.quality_var, value="480p").pack(anchor=W)
#         Radiobutton(self.quality_frame, text="360p", variable=self.quality_var, value="360p").pack(anchor=W)

#         # Button to start download
#         download_button = Button(self.quality_frame, text="Download", command=self.start_download)
#         download_button.pack(pady=10)

#         self.quality_frame.pack(pady=10)

#     def start_download(self):
#         # Get the link and selected quality
#         link = self.link_var.get()
#         quality = self.quality_var.get()

#         # Validate the link
#         if not link:
#             messagebox.showerror("Error", "Please enter a YouTube link")
#             return

#         # Start the download in a separate thread
#         threading.Thread(target=self.download_video, args=(link, quality)).start()

#     def download_video(self, link, quality):
#         try:
#             yt = YouTube(link)
#             stream = yt.streams.filter(res=quality, file_extension='mp4').first()

#             if not stream:
#                 messagebox.showerror("Error", f"No stream available for {quality}")
#                 return

#             # Download the video
#             stream.download()
#             messagebox.showinfo("Success", f"Video downloaded in {quality} quality")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to download video: {str(e)}")

# if __name__ == "__main__":
#     win = Tk()
#     obj = Main(win)
#     win.mainloop()























from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import threading
from PIL import Image, ImageTk

class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x300")
        root.resizable(False, True)
        self.root.title("Magic YT")

        # Open and resize the image
        image = Image.open("twitter.png")
        resized_image = image.resize((50, 50), Image.LANCZOS)  # Resize image to 50x50 pixels
        self.twitter_img = ImageTk.PhotoImage(resized_image)  # Keep a reference to the resized image

        # Create the button with the resized image
        self.button = Button(root, image=self.twitter_img, text="Click Me", compound=TOP, bd=19)
        self.button.pack(pady=20)

        # Entry widget for the YouTube link
        self.link_var = StringVar()
        self.link_entry = Entry(root, textvariable=self.link_var, width=50)
        self.link_entry.pack(pady=10)

        # Button to confirm the link and show quality options
        self.confirm_button = Button(root, text="Confirm Link", command=self.show_quality_options)
        self.confirm_button.pack(pady=5)

        # Frame for quality options
        self.quality_frame = Frame(root)

    def show_quality_options(self):
        # Extend the fram

        # Add Combobox for quality selection
        self.quality_label = Label(self.quality_frame, text="Select Quality:")
        self.quality_label.pack(anchor=W, pady=5)
        
        self.quality_var = StringVar()
        self.quality_combobox = Combobox(self.quality_frame, textvariable=self.quality_var)
        self.quality_combobox['values'] = ("720p", "480p", "360p")
        self.quality_combobox.current(0)  # Set default value
        self.quality_combobox.pack(anchor=W, pady=5)

        # Button to start download
        download_button = Button(self.quality_frame, text="Download", command=self.start_download)
        download_button.pack(pady=10)

        self.quality_frame.pack(pady=10)

    def start_download(self):
        # Get the link and selected quality
        link = self.link_var.get()
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

            # Download the video
            stream.download()
            messagebox.showinfo("Success", f"Video downloaded in {quality} quality")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {str(e)}")

if __name__ == "__main__":
    win = Tk()
    obj = Main(win)
    win.mainloop()
