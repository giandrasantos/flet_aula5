import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a opção correta!", color="#fafa02", size=20)
    resposta_correta = "Mickey"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Miska, Muska, PARABÉNS, VOCÊ ARCETOU!!"
        else:
            mensagem.value = "Resposta errada"
        page.update()

    page.title = "Game: Adivinhe o personagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#660505"

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe o personagem",
                    size=24,
                    weight="bold",
                    color="#fafa02"
                ),
                ft.Image(
                    src="images/mickey.jpg",
                    height=200,
                    border_radius=15
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Pateta",
                            on_click=verificar_resposta,
                            bgcolor="#fa0217",
                            color="#fafa02"
                        ),
                        ft.Button(
                            content="Mickey",
                            on_click=verificar_resposta,
                            bgcolor="#fa0217",
                            color="#fafa02"
                        ),
                        ft.Button(
                            content="Minnie",
                            on_click=verificar_resposta,
                            bgcolor="#fa0217",
                            color="#fafa02"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                mensagem
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)