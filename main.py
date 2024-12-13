from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from assets.screens.home_page import HomePage


class InvNaetApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file("./assets/screens/home_page.kv")


if __name__ == "__main__":
    InvNaetApp().run()
