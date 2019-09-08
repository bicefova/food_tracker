from Food.models import Food

foods = Food.objects.all()
food_1 = Food.objects.get(id=1)
food_bread = Food.objects.filter(name__iexact="Bread") # case insensitive
food_bread_exact = Food.objects.filter(name__exact="Bread") # case insensitive
food_bread