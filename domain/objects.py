class Film(object):

    def __init__(self, id_film, titlu, descriere, gen):
        self.__id_film = id_film
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen
        self.__inchirieri = 0

    def get_id(self):
        return int(self.__id_film)

    def get_titlu(self):
        return str(self.__titlu)

    def get_descriere(self):
        return str(self.__descriere)

    def get_gen(self):
        return str(self.__gen)

    def get_nr_inchirieri(self):
        return int(self.__inchirieri)

    def set_id(self, value):
        self.__id_film = value

    def set_titlu(self, value):
        self.__titlu = value

    def set_descriere(self, value):
        self.__descriere = value

    def set_gen(self, value):
        self.__gen = value

    def set_nr_inchirieri(self, value):
        self.__inchirieri = value

    def __str__(self):
        return str("ID film: " + str(self.__id_film) + " Titlu film: " + self.__titlu + " Descriere film: " + self.__descriere + " Gen film: " + self.__gen + " Numar inchirieri: " + str(self.get_nr_inchirieri()))

class Client(object):

    def __init__(self, id, nume, prenume):
        self.__id_client = id
        self.__nume = nume
        self.__prenume = prenume
        self.__nr_filme_inchiriate = 0

    def get_id(self):
        return int(self.__id_client)

    def get_nume(self):
        return str(self.__nume)

    def get_prenume(self):
        return str(self.__prenume)

    def get_nr_filme_inchiriate(self):
        return int(self.__nr_filme_inchiriate)

    def set_id(self, value):
        self.__id_client = value

    def set_nume(self, value):
        self.__nume = value

    def set_prenume(self, value):
        self.__prenume = value

    def set_nr_filme_inchiriate(self, value):
        self.__nr_filme_inchiriate = value

    def __str__(self):
        return str("Id client: " + str(self.get_id()) + " Nume si prenume client: " + self.get_nume() + " " + self.get_prenume() + " Numar filme inchiriate: " + str(self.get_nr_filme_inchiriate()))