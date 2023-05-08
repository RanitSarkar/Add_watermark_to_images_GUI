# library import
from tkinter import *
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter import filedialog

filename=""
txt=""

# customization
heading = ('Times New Roman', 30, 'bold')
new_size = (650, 400)

# funcations
def upload_file():
    global img, panel, filename
    f_types = [('Jpg Files', '*.jpg'),('PNG files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    print(filename)
    img = Image.open(filename)
    # Resize the image to a new size
    resized_image = img.resize(new_size)
    # Convert the resized image to a PhotoImage object
    photo_image = ImageTk.PhotoImage(resized_image)
    panel.config(image=photo_image)
    panel.image = photo_image


def imagefile():
    # get an image
    global filename, heading
    watermark_text=watermark_text_entry.get()
    with Image.open(filename).convert("RGBA") as base:
            fnt = ImageFont.truetype("font_files/Bruno_Ace/BrunoAce-Regular.ttf", size=32)
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            # get a drawing context
            d = ImageDraw.Draw(txt)
            # draw text, half opacity
            d.text((102, 50), watermark_text,font=fnt, fill=(255, 255, 255, 128))
            # draw text, full opacity
            out = Image.alpha_composite(base, txt)
            resized_image = out.resize(new_size)
            photo_image = ImageTk.PhotoImage(resized_image)
            panel.config(image=photo_image)
            panel.image = photo_image
    def saveit():
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        out.save(file_path)
    save_button=Button(text="save",activebackground="green",pady=10,fg="white", bg="black", padx=40, command=saveit)
    save_button.grid(row=3, column=2)


# base window creation
root = Tk()
root.geometry("680x580")
root.resizable(False, True)
root.title("Watermark images")
root.config(bg="black", padx=12,)

# components
header = Label(text="Lets watermark it..!!", font=heading, bg="black", fg="white")
frame = Frame(root,bg="black", highlightthickness=0)
upload_button = Button(text="Upload image", fg="white", bg="black", pady=10, padx=40, command= upload_file, activebackground="green")
add_watermark_button = Button(text="add watermark", fg="white", bg="black", pady=10, padx=40,command= imagefile, activebackground='green')
watermark_text_entry = Entry(font=('calibre',20,'normal'),width=20)
quit_button = Button(root, text="Quit", fg='white', bg="black", pady=10, padx=40,activebackground="red", command=root.quit)


#image component
img = Image.open("images/base_image.png")
# Resize the image to a new size
resized_image = img.resize(new_size)
# Convert the resized image to a PhotoImage object
photo_image = ImageTk.PhotoImage(resized_image)
panel = Label(frame, image=photo_image)


# placement of components
header.grid(row=0, column=1, columnspan=3)
frame.grid(row=1, column=1, columnspan=3)
panel.grid(row=0, column=0)
upload_button.grid(row=3, column=1, pady=10)
watermark_text_entry.grid(row=2,column=1,columnspan=1, pady=10)
watermark_text_entry.insert(0, "@Copyright")
add_watermark_button.grid(row=2,column=3,pady=10)
quit_button.grid(row=3, column=3, pady=10)


root.mainloop()