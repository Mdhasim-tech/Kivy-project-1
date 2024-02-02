from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import random

class SnakeWaterGunApp(App):
    def build(self):
        self.options = ['s', 'w', 'g']

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        label = Label(text="Select your choice:")
        layout.add_widget(label)

        button_snake = Button(text="Snake", on_press=lambda instance: self.play_game('s'))
        layout.add_widget(button_snake)

        button_water = Button(text="Water", on_press=lambda instance: self.play_game('w'))
        layout.add_widget(button_water)

        button_gun = Button(text="Gun", on_press=lambda instance: self.play_game('g'))
        layout.add_widget(button_gun)

        return layout

    def play_game(self, user_choice):
        computer_choice = random.choice(self.options)
        result = self.determine_winner(user_choice, computer_choice)

        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text=result))
        popup = Popup(title="Result", content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        elif (
            (user_choice == 's' and computer_choice == 'g') or
            (user_choice == 'w' and computer_choice == 's') or
            (user_choice == 'g' and computer_choice == 'w')
        ):
            return "Computer wins!"
        else:
            return "You win!"

if __name__ == '__main__':
    SnakeWaterGunApp().run()
