from lab8 import lab8c as c
from lab8 import cal_ui as ui

ui.create("Jayne")
ui.book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
ui.book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
ui.show("Jayne", 20, "sep")

c.remove("Jayne", 20, "sep", "15:00")

ui.book("Jayne", 20, "sep", "15:00", "16:00", "Return loot")

ui.show("Jayne", 20, "sep")