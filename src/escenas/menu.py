from __future__ import annotations
import arcade
from arcade import XYWH
from arcade.gui import UIManager, UIFlatButton, UILabel, UIAnchorLayout, UIBoxLayout

COLOR_FONDO = (28, 66, 66)          # verde petróleo suave
COLOR_CARD = (70, 97, 105, 180)     # panel translúcido
COLOR_TEXTO = arcade.color.WHITE

BTN_W, BTN_H = 260, 48

class Menu(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self.ui: UIManager | None = None
        self.anchor: UIAnchorLayout | None = None

    def on_show_view(self) -> None:
        arcade.set_background_color(COLOR_FONDO)

        # Inicializar UI
        self.ui = UIManager()
        self.ui.enable()

        self.anchor = UIAnchorLayout()
        self.ui.add(self.anchor)

        # Título
        titulo = UILabel(
            text='Menú principal',
            text_color=COLOR_TEXTO,
            font_size=34,
            bold=True,
        )

        # Fábrica de botones
        def make_btn(texto: str, on_click):
            btn = UIFlatButton(
                text=texto,
                width=BTN_W,
                height=BTN_H,
            )
            btn.on_click = on_click
            return btn

        btn_jugar = make_btn('Nueva partida', self._on_nueva_partida)
        btn_opc   = make_btn('Opciones', self._on_opciones)
        btn_salir = make_btn('Salir', self._on_salir)

        # Layout vertical
        vbox = UIBoxLayout(space_between=12)
        vbox.add(titulo.with_space_around(bottom=18))
        vbox.add(btn_jugar)
        vbox.add(btn_opc)
        vbox.add(btn_salir)

        # Anclar al centro
        self.anchor.add(child=vbox, anchor_x='center', anchor_y='center')

    def on_hide_view(self) -> None:
        if self.ui:
            self.ui.disable()

    def on_draw(self) -> None:
        self.clear()
        w, h = self.window.width, self.window.height

        # Panel translúcido
        card = XYWH(x=w/2 - 360/2, y=h/2 - 280/2, width=360, height=280)
        arcade.draw_rect_filled(card, COLOR_CARD)
        arcade.draw_rect_outline(card, arcade.color.WHITE, border_width=2)

        # Detalle decorativo
        arcade.draw_line(w*0.15, h*0.78, w*0.85, h*0.78, arcade.color.WHITE, 1)

        # Footer
        arcade.draw_text('Codiando — v0.1', 16, 12, (220, 230, 230), 12)
        if self.ui:
            self.ui.draw()

    # Callbacks
    def _on_nueva_partida(self, _event) -> None:
        # Placeholder: reproducimos un sonido y volvemos a Intro por ahora
        try:
            arcade.play_sound(arcade.load_sound(':resources:sounds/upgrade5.wav'))
        except Exception:
            pass
        from .intro import Intro
        self.window.show_view(Intro())

    def _on_opciones(self, _event) -> None:
        try:
            arcade.play_sound(arcade.load_sound(':resources:sounds/secret4.wav'))
        except Exception:
            pass

    def _on_salir(self, _event) -> None:
        arcade.exit()
