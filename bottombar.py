from flet import *
from flet import colors,icons

bottombar=Container(
    margin=3,
    border_radius=50,
    content=Card(
        elevation=30,
        content=Container(
            bgcolor="white",
            content=Row([
                Container(
                    padding=10,
                    content=Column([
                        CircleAvatar(
                            content=Icon(icons.MOTORCYCLE,
                                size=20,
                                color="white"
                            ),
                            bgcolor="#00A911"
                        ),
                        Text("GoRide",weight="bold",color="grey", size=20),
                    ],alignment="center",horizontal_alignment="center")
                ),
                Container(
                    padding=10,
                    content=Column([
                        CircleAvatar(
                            content=Icon(icons.DEPARTURE_BOARD,
                                size=20,
                                color="white"
                            ),
                            bgcolor="ligthblue"
                        ),
                        Text("GoShop",weight="bold",color="grey", size=20),
                    ],alignment="center",horizontal_alignment="center")
                ),
                Container(
                    padding=10,
                    content=Column([
                        CircleAvatar(
                            content=Icon(icons.RESTAURANT,
                                size=20,
                                color="white"
                            ),
                            bgcolor="orange"
                        ),
                        Text("GoCar",weight="bold",color="grey", size=20),
                    ],alignment="center",horizontal_alignment="center")
                )
            ],alignment="spaceAround")
        )
    )
)