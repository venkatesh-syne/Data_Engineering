class Movie:

    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def display_info(self):
        print(f"Title: {self.title}, Director: {self.director}, Rating: {self.rating}")


# Example usage
movie1 = Movie("OG", "Sujeeth", 10)

movie1.display_info()