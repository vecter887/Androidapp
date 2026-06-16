main.py
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window


class FloatingControlPanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint = (None, None)
        self.size = (300, 350)

        self.pos = (100, 100)

        self.drag_btn = Button(
            text="::: HOLD & MOVE :::",
            background_color=(0.1, 0.5, 0.9, 1),
            size_hint_y=None,
            height=50
        )

        self.drag_btn.bind(
            on_touch_down=self.start_drag,
            on_touch_move=self.drag_panel
        )

        self.add_widget(self.drag_btn)

        self.pull_down_value = 70

        self.value_label = Label(
            text=f"Pull Down Speed: {self.pull_down_value}",
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.value_label)

        self.slider = Slider(
            min=10,
            max=200,
            value=70,
            step=5
        )

        self.slider.bind(value=self.on_slider_change)
        self.add_widget(self.slider)

        self.action_btn = Button(
            text="START CONTROL",
            background_color=(0, 0.8, 0.2, 1)
        )

        self.action_btn.bind(on_press=self.toggle_recoil)
        self.add_widget(self.action_btn)

        self.is_active = False
        self.dragging = False

    def start_drag(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.dragging = True
            return True

    def drag_panel(self, instance, touch):
        if self.dragging and touch.grab_current is None:
            self.pos = (
                touch.x - self.width / 2,
                touch.y - self.height / 2
            )
            return True

    def on_slider_change(self, instance, value):
        self.pull_down_value = int(value)
        self.value_label.text = (
            f"Pull Down Speed: {self.pull_down_value}"
        )

    def toggle_recoil(self, instance):
        self.is_active = not self.is_active

        if self.is_active:
            self.action_btn.text = "STOP CONTROL"
            self.action_btn.background_color = (0.9, 0.1, 0.1, 1)
        else:
            self.action_btn.text = "START CONTROL"
            self.action_btn.background_color = (0, 0.8, 0.2, 1)


class RecoilApp(App):
    def build(self):
        Window.clearcolor = (0.15, 0.15, 0.15, 1)

        root = FloatLayout()

        panel = FloatingControlPanel()
        root.add_widget(panel)

        return root


if __name__ == "__main__":
    RecoilApp().run()