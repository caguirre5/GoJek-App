from flet import *
from flet import colors,icons
import mainmenu
import section1
import section2
import section3
import bottombar

def main(page: Page):
    page.padding=0
    page.spacing=0
    page.scroll='auto'
    page.add(
        mainmenu.appmenu,
        section1.section,
        section2.section,
        section3.section,
        bottombar.bottombar
    )

app(target=main)