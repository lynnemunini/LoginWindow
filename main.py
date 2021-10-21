from tkinter import *
# from PIL import Image
# Changing the resolution of our image using pillow
# Open the image by specifying the image path.
# image_path = "bg1.png"
# image_file = Image.open(image_path)
# size = (700, 450)
# r_img = image_file.resize(size)
# # the default
# r_img.save("bg2.png", quality=25)

GREY = "#FFC947"


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x450")
        self.title("LogIn Page")
        # To prevent user from resizing GUI
        self.resizable(False, False)

    # def label(self):
    #     self.backgroundImage = PhotoImage(file="bg2.png")
    #     self.backgroundImageLabel = Label(self, image=self.backgroundImage)
    #     self.backgroundImageLabel.place(x=0, y=0)

    def label(self):
        self.background = Canvas(self, bg=GREY, width=700, height=450)
        self.background.place(x=0, y=0)

        self.canvas = Canvas(self, width=400, height=330, bg=GREY, highlightthickness=0)
        self.canvas.place(x=150, y=50)
        # Login Image
        self.image_canvas = Canvas(width=100, height=100, bg=GREY, highlightthickness=0)
        self.title_image = PhotoImage(file="login2.png")
        self.image_canvas.create_image(50, 50, image=self.title_image)
        self.image_canvas.place(x=300, y=50)

        self.username_label = Label(self, bg=GREY, text="Username", font=8)
        self.username_label.place(x=200, y=150)
        self.password_label = Label(self, bg=GREY, text="Password", font=8)
        self.password_label.place(x=200, y=200)

    def entry(self):
        self.username = Text(self, borderwidth=0, highlightthickness=0, width=22, height=2)
        self.username.place(x=320, y=155)

        self.password = Entry(self, bg="white", borderwidth=0, show="*", highlightthickness=0)
        self.password.place(x=320, y=205, width=175, height=20)

    def button(self):
        # Login
        self.login_image = PhotoImage(file="user-interface.png")
        self.login_image_button = Button(self, image=self.login_image, bg=GREY, highlightthickness=0, command=self.login
                                         , border=0)
        self.login_image_button.place(x=290, y=230)

        # Social Media Buttons
        # LinkedIn
        self.linkedin_image = PhotoImage(file="LinkedIN.png")
        self.linkedin_button = Button(self, image=self.linkedin_image, bg=GREY, highlightthickness=0,
                                      command=self.login, border=0)
        self.linkedin_button.place(x=230, y=340)
        # Twitter
        self.twitter_image = PhotoImage(file="twitter.png")
        self.twitter_button = Button(self, image=self.twitter_image, bg=GREY, highlightthickness=0, command=self.login,
                                     border=0)
        self.twitter_button.place(x=290, y=340)

        # github
        self.github_image = PhotoImage(file="github.png")
        self.github_button = Button(self, image=self.github_image, bg=GREY, highlightthickness=0, command=self.login,
                                    border=0)
        self.github_button.place(x=350, y=340)

        # reddit
        self.reddit_image = PhotoImage(file="reddit.png")
        self.reddit_image_button = Button(self, image=self.reddit_image, bg=GREY, highlightthickness=0,
                                          command=self.login,
                                          border=0)
        self.reddit_image_button.place(x=410, y=340)

    def login(self):
        print("You clicked me!")


if __name__ == "__main__":
    Login = Login()
    Login.label()
    Login.entry()
    Login.button()
    Login.mainloop()
