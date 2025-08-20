class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles.copy()

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def __repr__(self):
        return f"Author('{self.name}')"


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles.copy()

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles]

    def __repr__(self):
        return f"Magazine('{self.name}', '{self.category}')"


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if len(title) == 0:
            raise ValueError("title must be non-empty")

        self._author = author
        self._magazine = magazine
        self._title = title

        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return f"Article('{self.title}', {self.author.name}, {self.magazine.name})"


# Create Author instances
author1 = Author("Alice Munro")
author2 = Author("James Baldwin")
author3 = Author("Chimamanda Adichie")

# Create Magazine instances
mag1 = Magazine("Writers Weekly", "Literature")
mag2 = Magazine("Tech Today", "Technology")
mag3 = Magazine("Global Voices", "Culture")

# Create Article instances using `add_article`
article1 = author1.add_article(mag1, "The Power of Storytelling")
article2 = author2.add_article(mag1, "Identity and Expression")
article3 = author2.add_article(mag2, "The Digital Divide")
article4 = author3.add_article(mag3, "Bridging Cultures")
article5 = author1.add_article(mag3, "Language and Belonging")

# DEMONSTRATE Author Methods
print("Author1 Articles:", author1.articles())
print("Author1 Magazines:", author1.magazines())

print("Author2 Articles:", author2.articles())
print("Author2 Magazines:", author2.magazines())

# DEMONSTRATE Magazine Methods
print("Mag1 Articles:", mag1.articles())
print("Mag1 Contributors:", mag1.contributors())
print("Mag1 Titles:", mag1.article_titles())

print("Mag3 Articles:", mag3.articles())
print("Mag3 Contributors:", mag3.contributors())

# Article details
print("All Articles:")
for a in [article1, article2, article3, article4, article5]:
    print(a)
