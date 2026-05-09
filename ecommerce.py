#ecommerce gestion de panier

class Product:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.title}| {self.quantity}, Prix total : {self.price * self.quantity}  "


class Panier:
    def __init__(self):
        self.products = []
    

    def ajouter(self, produit):
        self.products.append(produit)
        print(f"Vous venez d'ajouté {produit.title} à votre panier !")

    def afficher(self):
        if not self.products:
            print(f" votre panier est vide !")
        else:
            for produit in self.products:
                print(produit)
    
    def totaol_article(self):
        total = sum(p.total_price() for p in self.products)
        print(f"le total de votre panier est {total}")

article1 = Product("Sac à dos", 24.99, 1)
article2 = Product("Veste en cuire à dos", 70.99, 1)
article3 = Product("Chaussure Nike", 80.99, 2)

p = Panier()

p.ajouter(article1)
p.ajouter(article2)
p.ajouter(article3)
p.afficher()
p.totaol_article()