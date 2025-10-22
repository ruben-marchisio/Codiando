import arcade
from .escenas.intro import Intro

TITULO = "Codiando — base mínima"
ANCHO, ALTO = 960, 540

def main() -> None:
    ventana = arcade.Window(width=ANCHO, height=ALTO, title=TITULO)
    ventana.show_view(Intro())
    arcade.run()

if __name__ == "__main__":
    main()
