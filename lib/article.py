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

        # Add this article to author's and magazine's list
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


author1 = Author("Alice Munro")
mag1 = Magazine("Writers Weekly", "Literature")

# Create article (this adds it to both author and magazine)
article1 = author1.add_article(mag1, "The Power of Storytelling")

print(author1.articles())       # [Article('The Power of Storytelling', Alice Munro, Writers Weekly)]
print(author1.magazines())      # [Magazine('Writers Weekly', 'Literature')]

print(mag1.articles())          # [Article('The Power of Storytelling', Alice Munro, Writers Weekly)]
print(mag1.contributors())      # [Author('Alice Munro')]
