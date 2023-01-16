from flet import *
from flet import colors,icons

#Contenedor con una fila que contiene otro contenedor
section = Container(
    bgcolor='#F7293D',
    padding=20,
    height=100,
    content=Column([
        Row([
            Container(
                ink=True,
                on_click=lambda e: print('test'),
                content=Row([
                    Icon(name='menu',color='White',size=20),
                    Text('Promosi',size=15,color="White")
                ],spacing=1)
            ),
            Container(
                ink=True,
                on_click=lambda e: print('test'),
                content=Row([
                    Icon(name='home',color='White',size=20),
                    Text('Home',size=15,color="White")
                ],spacing=1)
            ),
            Container(
                ink=True,
                on_click=lambda e: print('test'),
                content=Row([
                    Icon(name='message',color='White',size=20),
                    Text('Chat',size=15,color="White")
                ],spacing=1)
            )
        ], alignment='spaceEvenly')
    ],alignment='start')
)