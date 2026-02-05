var = {'blue', 'green'}
var2 = {'blue','yellow'}

commoncolur = var.intersection(var2)

unique_colour = var.symmetric_difference(var2)


print(unique_colour)  # Output: {'green', 'yellow'}
