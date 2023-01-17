from flet import *
from flet import colors,icons

section = Container(
    margin=margin.only(top=60,left=10),
    content=Column([
        Text("Top Picks For You",size=30,weight="bold"),
        Row([
            Container(
                margin=margin.only(top=10),
                border_radius=30,
                padding=10,
                bgcolor="#41AF62",
                ink=True,
                on_click=lambda e:print("badge test"),
                border=border.all(2,"#E1E1E1"),
                content=Text("All",size=13,color="white")
            ),
            Container(
                margin=margin.only(top=10),
                border_radius=30,
                padding=10,
                ink=True,
                on_click=lambda e:print("badge test"),
                border=border.all(2,"#E1E1E1"),
                content=Text("Mexican",size=13,color="black")
            ),
            Container(
                margin=margin.only(top=10),
                border_radius=30,
                padding=10,
                ink=True,
                on_click=lambda e:print("badge test"),
                border=border.all(2,"#E1E1E1"),
                content=Text("Chinese",size=13,color="black")
            ),
            Container(
                margin=margin.only(top=10),
                border_radius=30,
                padding=10,
                ink=True,
                on_click=lambda e:print("badge test"),
                border=border.all(2,"#E1E1E1"),
                content=Text("Pasta",size=13,color="black")
            ),
        ],alignment="spaceAround"),
        Container(
            margin=margin.only(bottom=40),
            content=Row([
                Card(
                    elevation=30,
                    content=Container(
                        bgcolor="white",
                        padding=10,
                        content=Column([
                            Image(
                                src="https://i0.wp.com/acordesdevino.com/wp-content/uploads/2021/01/sush-y-sashimi.jpg?fit=600%2C400&ssl=1",
                                fit="contain",
                                width=300,
                                height=220,
                            ),
                            Text("Sushi Zen",size=20,weight="bold"),
                            Text(
                                "Rollo de arroz envuelto en alga; por dentro\n aguacate, remolacha...",
                                size=15, 
                                color="grey",
                            )
                        ])
                    )
                ),
                Card(
                    elevation=30,
                    content=Container(
                        bgcolor="white",
                        padding=10,
                        content=Column([
                            Image(
                                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr9vhPNWKJ0aDRd-tePeR3bW-fYhupentLUAUSPEm8QCoskTJ-IOj3Znm05KeZLpxC5Lc&usqp=CAU",
                                fit="contain",
                                width=300,
                                height=220,
                            ),
                            Text("Ay Carmela",size=20,weight="bold"),
                            Text(
                                "Rollo de arroz envuelto en alga; por dentro\n aguacate, remolacha...",
                                size=15, 
                                color="grey",
                            )
                        ])
                    )
                ),
                Card(
                    elevation=30,
                    content=Container(
                        bgcolor="white",
                        padding=10,
                        content=Column([
                            Image(
                                src="https://i0.wp.com/acordesdevino.com/wp-content/uploads/2021/01/sush-y-sashimi.jpg?fit=600%2C400&ssl=1",
                                fit="contain",
                                width=300,
                                height=220,
                            ),
                            Text("Sushi Zen",size=20,weight="bold"),
                            Text(
                                "Rollo de arroz envuelto en alga; por dentro\n aguacate, remolacha...",
                                size=15, 
                                color="grey",
                            )
                        ])
                    )
                ),
                Card(
                    elevation=30,
                    content=Container(
                        bgcolor="white",
                        padding=10,
                        content=Column([
                            Image(
                                src="https://i0.wp.com/acordesdevino.com/wp-content/uploads/2021/01/sush-y-sashimi.jpg?fit=600%2C400&ssl=1",
                                fit="contain",
                                width=300,
                                height=220,
                            ),
                            Text("Sushi Zen",size=20,weight="bold"),
                            Text(
                                "Rollo de arroz envuelto en alga; por dentro\n aguacate, remolacha...",
                                size=15, 
                                color="grey",
                            )
                        ])
                    )
                ),
                Card(
                    elevation=30,
                    content=Container(
                        bgcolor="white",
                        padding=10,
                        content=Column([
                            Image(
                                src="https://i0.wp.com/acordesdevino.com/wp-content/uploads/2021/01/sush-y-sashimi.jpg?fit=600%2C400&ssl=1",
                                fit="contain",
                                width=300,
                                height=220,
                            ),
                            Text("Sushi Zen",size=20,weight="bold"),
                            Text(
                                "Rollo de arroz envuelto en alga; por dentro\n aguacate, remolacha...",
                                size=15, 
                                color="grey",
                            )
                        ])
                    )
                ),
                Card(
                    elevation=30,
                    content=Container(
                        bgcolor="white",
                        padding=10,
                        content=Column([
                            Image(
                                src="https://i0.wp.com/acordesdevino.com/wp-content/uploads/2021/01/sush-y-sashimi.jpg?fit=600%2C400&ssl=1",
                                fit="contain",
                                width=300,
                                height=220,
                            ),
                            Text("Sushi Zen",size=20,weight="bold"),
                            Text(
                                "Rollo de arroz envuelto en alga; por dentro\n aguacate, remolacha...",
                                size=15, 
                                color="grey",
                            )
                        ])
                    )
                ),
            ], scroll="always")
        )
    ])
)