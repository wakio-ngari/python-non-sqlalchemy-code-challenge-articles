class Author:
    def __init__(self, name):
        #Ensures that  the name is a non empty string
        if not isinstance (name,str) or len (name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name# stores name as an attribute
        self._articles = []#initializes emptylist to store articles that are wtitten 

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):#verifies inputs and creates an article instance
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):#it generates a special list of all the magazines categories the author 
        #has written for
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    _all_magazines = []# list that keeps an eye  on all magazine instances

    def __init__(self, name, category):#confirms and verifies the inputs and kickstarts magazine attributes
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []#to store the articles that have been published in the magazine
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            return  
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            return
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
#Helps us return a list of the authors who have written more than two articles fot this  magazine
    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        #This helps us to return the magazine with the most articles
        #or  none if there is no magazines
        if not cls._all_magazines or not any(magazine.articles() for magazine in cls._all_magazines):
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()))


class Article:
    all = [] 

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        magazine.articles().append(self)
        author.articles().append(self)
        Article.all.append(self)  # includes a  new article to the class-level list

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        self._magazine = value