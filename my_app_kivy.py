# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

# Глобальные настройки
Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "ver 1.0"

class MyApp(App):



	def __init__(self):
		super().__init__()
		self.label = Label(text='Конвертер')


		def callback(instance):
			print('<%s>' % instance.text)
			self.label.text ='%s' % instance.text


		self.button = Button(text='1')
		self.button.bind(on_press=callback)
		self.button1 = Button(text='2')
		self.button1.bind(on_press=callback)
		self.button2 = Button(text='3')
		self.button2.bind(on_press=callback)

	def build(self):
		box = BoxLayout(orientation='vertical')
		box.add_widget(self.label)
		box.add_widget(self.button)
		box.add_widget(self.button1)
		box.add_widget(self.button2)


		return box



# Запуск проекта
if __name__ == "__main__":
	MyApp().run()