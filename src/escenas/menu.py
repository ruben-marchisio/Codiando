from __future__ import annotations
import arcade
from arcade import XYWH

class Menu(arcade.View):
    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

    def on_draw(self) -> None:
        self.clear()
        w, h = self.window.width, self.window.height

        arcade.draw_text("Menú principal", w/2, h-80, arcade.color.WHITE, 28, anchor_x="center")

        tarjeta = XYWH(x=w/2-150, y=h/2-60, width=300, height=120)
        arcade.draw_rect_filled(tarjeta, arcade.color.CADET)
        arcade.draw_rect_outline(tarjeta, arcade.color.WHITE, border_width=2)
        arcade.draw_text("Base lista (Arcade 3.3.3)", w/2, h/2, arcade.color.WHITE, 16, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.ESCAPE:
            from .intro import Intro
            self.window.show_view(Intro())
