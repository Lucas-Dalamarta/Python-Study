class Movie:

    def __init__(self,name,release,duration):
        self.name     =   name
        self.release  =   release
        self.duration =   duration


class   Series:

    def __init__(self,name,release,seasons):
        self.name     =   name
        self.release  =   release
        self.seasons  =   seasons



naruto = Movie("naruto Road to Boruto",2018,120)

print(naruto.name)

