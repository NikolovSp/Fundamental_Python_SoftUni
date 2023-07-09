class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self,  species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        else:
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        info = ''
        if species == 'mammal':
            info = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            info = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        else:
            info = f"Birds in {self.name}: {', '.join(self.birds)}\n"

        info += f"Total animals: {Zoo.__animals}"
        return info


name = input()
zoo = Zoo(name)
total_animals = int(input())
for animals in range(total_animals):
    species, name = input().split()
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
