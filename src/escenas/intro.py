from __future__ import annotations
import arcade
from arcade import XYWH

COLOR_FONDO = arcade.color.DARK_MIDNIGHT_BLUE
COLOR_PANEL = arcade.color.BABY_BLUE
COLOR_BORDE = arcade.color.WHITE

class Intro(arcade.View):
    def on_show_view(self) -> None:
        arcade.set_background_color(COLOR_FONDO)

    def on_draw(self) -> None:
        self.clear()
        w, h = self.window.width, self.window.height

        panel = XYWH(x=(w-520)/2, y=(h-240)/2, width=520, height=240)
        arcade.draw_rect_filled(panel, COLOR_PANEL)
        arcade.draw_rect_outline(panel, COLOR_BORDE, border_width=2)

        arcade.draw_text("¡Codiando!", w/2, h/2+60, arcade.color.BLACK, 28, anchor_x="center")
        arcade.draw_text("ENTER → Menú", w/2, h/2-10, arcade.color.BLACK, 16, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.ENTER:
            from .menu import Menu
            self.window.show_view(Menu())
