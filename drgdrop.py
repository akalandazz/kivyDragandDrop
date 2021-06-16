from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import DragBehavior
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.properties import ObjectProperty

class ItemsBox(BoxLayout):
	active_button = ObjectProperty()
	def on_touch_up(self, touch):
		act_btn = ItemsBox.active_button
		passive_buttons = [item for item in self.children if act_btn != item]
		for pas_btn in passive_buttons:
			if pas_btn.collide_widget(act_btn):
				left = self.children.index(act_btn)
				right = self.children.index(pas_btn)
				self.children[left], self.children[right] = self.children[right],self.children[left]
				break
		return super().on_touch_up(touch)




	



class DragButton(DragBehavior, Button):
	def on_touch_down(self, touch):
		ItemsBox.active_button = self
		return super().on_touch_down(touch)

	def on_release(self):
		print(self.text)
		return super().on_release()


class MyApp(App):
	def build(self):
		return ItemsBox()

MyApp().run()