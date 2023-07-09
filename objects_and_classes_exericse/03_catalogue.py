class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # first_letter = []
        # for product in self.products:
        #     if product.startswith(first_letter):
        #         first_letter.append(product)
        # return first_letter
        return [product for product in self.products if product.startswith(first_letter)]

    def __str__(self):
        info = f"Items in the {self.name} catalogue:\n"
        self.products.sort()
        info += "\n".join(self.products)
        return info


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
