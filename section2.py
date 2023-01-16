from flet import *
from flet import colors,icons

section = ResponsiveRow([
    Container(
        bgcolor='#FFFFFF',
        border_radius=border_radius.only(topLeft=30,topRight=30),
        padding=0,
        margin=margin.symmetric(vertical=-30),
        content=Column(
            col={"sm":12,"md":12,"lg":12},
            controls=[
                Container(
                    bgcolor="#FCFCFC",
                    border_radius = 30,
                    padding=padding.only(left=10,right=10),
                    content=Row([
                        TextField(
                            border="none",
                            prefix_icon=icons.SEARCH,
                            label="Search Lunch?"
                        ),
                        IconButton(
                            icon=icons.ACCOUNT_CIRCLE,
                            icon_color="#F7293D",
                            icon_size=30,
                        ),

                    ],alignment="spaceBetween")
                ),
                Card(
                    margin=margin.only(left=10,right=10),
                    elevation=30,
                    content=Container(
                        padding=padding.only(left=10,right=30),
                        border_radius=30,
                        bgcolor="#F7293D",
                        content=Row([
                            Image(
                                src="https://kutv.com/resources/media2/16x9/full/1015/center/80/6b7a7c7c-3c44-489c-9880-4a17508cdc6d-large16x9_Postworkout_meal.jpg",
                                fit="contain",
                                width=130,
                                height=70,
                                border_radius=border_radius.all(20),
                            ),
                            Container(
                                margin=10,
                                height=80,
                                padding=10,
                                width=120,
                                border_radius=10,
                                content=Column([
                                    Text("Basic Meal",color="White",weight="bold",size=15),
                                    Text("Q. 30.50",color="White",weight="bold",size=17),
                                    Text("Tap for details...",color="White",size=11),
                                ],alignment="center", horizontal_alignment="center",spacing=0)
                            ),
                            Column([
                                Icon(name="shopping_bag",color="white",size=30),
                                Text("Order",color="White",size=15,weight="bold")
                            ],horizontal_alignment="center"
                            )
                        ],alignment="spaceEvenly")
                    )
                )
            ]
        )
    )
])