from bygning import Bygning

bygning1 = Bygning("Problemveien 2", "Thomas", 10)
bygning1.skrivInfo()
bygning1.nyEier("Ole")
bygning1.flyttUt(120, minthreshold=0)
print()
bygning1.skrivInfo()
