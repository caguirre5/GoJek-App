from flet import *
from flet import colors,icons

appmenu= ResponsiveRow([
    Column(
        col={"sm":12,"md":12,"lg":12},
        controls=[
            Container(
                padding=10,
                bgcolor="#DEDEDE",
                content=Row([
                    Image(
                        src="https://lh3.googleusercontent.com/VfxOAPkn2bm0WcRUTu73h1_8EQEFclcJHmkhcMsmLssT2TdgVH-boOO_E2UgI1wiZ0cJS_ARzOeR_dMKGukdw4pVMUxBSlzZInap_AK-Cr8WFzZBMlY",
                        fit="contain",
                        width=130,
                        height=60,
                    ),
                    CircleAvatar(
                        foreground_image_url="https://www.autokims.com.mx/imagenes/profile3.png",

                    ),
                ],alignment="spaceBetween")
            )
        ]
    )
])