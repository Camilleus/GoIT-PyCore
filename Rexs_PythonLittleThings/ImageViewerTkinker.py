import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("1000x800")

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=5)

        self.load_button = tk.Button(
            root, text="Load Image", command=self.load_image)
        self.load_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm")])
        if file_path:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo


def main():
    root = tk.Tk()
    ImageViewerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
