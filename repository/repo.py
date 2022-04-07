from lab7_9_teste.domain.objects import Film, Client

"""-----------------------------------------------------------------------------------------------REPO----------------------------------------------------------------------------------------------"""


class Depozit_film(object):

    def __init__(self):
        self.__listafilme = []

    def add_film_in_lista(self, film):
        """
        Functia adauga un film in lista, daca acesta trece de validator.
        Input: film - class
        :param film:
        :return:
        """
        try:
            self.__verificare_film_nou(film)
            self.__listafilme.append(film)
            print("Film adaugat cu succes!")
        except ValueError as ve:
            print(str(ve))

    def del_film_in_lista(self, id):
        """
        Functia sterge un film din lista dupa id, daca acesta trece de validator.
        Input: id - int
        :param id:
        :return:
        """
        try:
            ind = self.verificare_film_in_lista(id)
            self.__listafilme.pop(ind)
            print("Film sters cu succes!")
        except ValueError as ve:
            print(str(ve))

    def modifica_film(self, film, id):
        """
        Functia modifica un film din lista dupa id, daca acesta trece de validator.
        Input: film - class, id - int
        :param film:
        :param id:
        :return:
        """
        try:
            ind = self.verificare_film_in_lista(id)
            self.__listafilme[ind] = film
            print("Film modificat cu succes!")
        except ValueError as ve:
            print(str(ve))

    def modifica_film_inchirieri(self, film, id):
        """
        Functia modifica un film din lista dupa id, daca acesta trece de validator.
        Input: film - class, id - int
        :param film:
        :param id:
        :return:
        """
        try:
            ind = self.verificare_film_in_lista(id)
            self.__listafilme[ind] = film
        except ValueError as ve:
            print(str(ve))

    def get_len(self):
        return len(self.__listafilme)

    def get_lista_id(self, ind):
        film = self.__listafilme[ind]
        return film.get_id()

    def get_lista_titlu(self, ind):
        film = self.__listafilme[ind]
        return film.get_titlu()

    def get_lista_descriere(self, ind):
        film = self.__listafilme[ind]
        return film.get_descriere()

    def get_lista_gen(self, ind):
        film = self.__listafilme[ind]
        return film.get_gen()

    def get_all(self):
        return self.__listafilme

    def __verificare_film_nou(self, film):
        """
        Functia verifica daca filmul este unul nou. In caz contrar, arunca o exceptie.
        Input: id
        :param film:
        :return:
        """
        eroare = ""
        for ind in range(self.get_len()):
            if film.get_id() == self.get_lista_id(ind):
                if eroare:
                    eroare += "\n"
                eroare += "id deja existent"
                break
            if film.get_titlu() == self.get_lista_titlu(ind) and film.get_gen() == self.get_lista_gen(ind):
                if eroare:
                    eroare += "\n"
                eroare += "film deja existent"
                break
        if eroare:
            raise ValueError(str(eroare))

    def verificare_film_in_lista(self, id):
        """
        Functia verifica daca filmul exista deja in lista pentru a-l putea sterge/modifica.
        Input: id -int
        Output: (daca exista) ind - indicele la care se afla filmul
        :param id:
        :return:
        """
        gasit = 0
        for ind in range(self.get_len()):
            if id == self.get_lista_id(ind):
                return ind
        if not gasit:
            raise ValueError("nu exista film cu acest id")

    def verificare_film_in_lista_inchiriere(self, id):
        """
        Functia verifica daca filmul exista deja in lista pentru a-l putea sterge/modifica.
        Input: id -int
        Output: (daca exista) ind - indicele la care se afla filmul
        :param id:
        :return:
        """
        gasit = 0
        for ind in range(self.get_len()):
            if id == self.get_lista_id(ind):
                return self.__listafilme[ind]
        if not gasit:
            raise ValueError("nu exista film cu acest id")

    def cauta_film(self, id):
        """
        Functia cauta filmul dupa id, si afiseaza filmul, altfel aruca exceptie.
        :param id:
        :return:
        """
        try:
            ind = self.verificare_film_in_lista(id)
            rez = "Id film: " + str(self.get_lista_id(ind)) + "\nTitlu film: " + str(
                self.get_lista_titlu(ind)) + "\nDescriere: " + str(
                self.get_lista_descriere(ind)) + "\nGen film: " + str(self.get_lista_gen(ind))
            print(rez)
        except ValueError as ve:
            print(ve)


class Depozit_client(object):

    def __init__(self):
        self.__listaclienti = []

    def get_len(self):
        return len(self.__listaclienti)

    def get_id(self, ind):
        client = self.__listaclienti[ind]
        return client.get_id()

    def get_nume(self, ind):
        client = self.__listaclienti[ind]
        return client.get_nume()

    def get_prenume(self, ind):
        client = self.__listaclienti[ind]
        return client.get_prenume()

    def get_nr_filme_inchiriate(self, ind):
        client = self.__listaclienti[ind]
        return client.get_nr_filme_inchiriate()

    def get_all(self):
        return self.__listaclienti

    def add_client_in_lista(self, client):
        """
        Functia adauga un client in lista daca trece de validator.
        Input: id -int
        :param client:
        :return:
        """
        try:
            self.verificare_client_nou(client)
            self.__listaclienti.append(client)
            print("Client adaugat cu succes! Numar filme inchiriate: 0")
        except ValueError as ve:
            print(str(ve))

    def verificare_client_nou(self, client):
        """
        Functia verifica daca clientul este unul nou.
        Input: client - class
        :param client:
        :return:
        """
        eroare = ""
        id = int(client.get_id())
        for ind in range(self.get_len()):
            if id == self.get_id(ind):
                eroare += "id deja existent"
                break
        nume = client.get_nume()
        prenume = client.get_prenume()
        for ind in range(self.get_len()):
            if nume == self.get_nume(ind) and prenume == self.get_prenume(ind) and id == self.get_id(ind):
                if eroare:
                    eroare += "\n"
                eroare += "client deja existent"
        if eroare:
            raise ValueError(str(eroare))

    def del_client(self, id):
        """
        Functia sterge un client dupa id din lista daca trece de validator.
        Input: id - int
        :param id:
        :return:
        """
        try:
            ind = self.verificare_client_in_lista(id)
            self.__listaclienti.pop(ind)
            print("Client sters cu succes!")
        except ValueError as ve:
            print(str(ve))

    def verificare_client_in_lista(self, id):
        """
        Functia verifica un client daca este in lista.
        Input: id - int
        :param id:
        :return:
        """
        gasit = 0
        for ind in range(self.get_len()):
            if id == self.get_id(ind):
                return ind
        if not gasit:
            raise ValueError("nu exista client cu acest id")

    def verificare_client_in_lista_inchiriere(self, id):
        """
        Functia verifica un client daca este in lista.
        Input: id - int
        :param id:
        :return:
        """
        gasit = 0
        for ind in range(self.get_len()):
            if id == self.get_id(ind):
                return self.__listaclienti[ind]
        if not gasit:
            raise ValueError("nu exista client cu acest id")

    def modifica_client(self, client, id):
        """
        Functia modifica client dupa id daca acesta trece de validator.
        Input: client - class
               id - int
        :param client:
        :param id:
        :return:
        """
        try:
            ind = self.verificare_client_in_lista(id)
            self.__listaclienti[ind] = client
            print("Client modificat cu succes!")
        except ValueError as ve:
            print(str(ve))

    def modifica_client_inchirieri(self, client, id):
        """
        Functia modifica client dupa id daca acesta trece de validator.
        Input: client - class
               id - int
        :param client:
        :param id:
        :return:
        """
        try:
            ind = self.verificare_client_in_lista(id)
            self.__listaclienti[ind] = client
        except ValueError as ve:
            print(str(ve))

    def cauta_client(self, id):
        """
        Functia cauta client dupa id si il afiseaza daca il gaseste, in caz contrar, semnaleaza eroarea.
        :param id:
        :return:
        """
        try:
            ind = self.verificare_client_in_lista(id)
            rez = "Id client: " + str(self.get_id(ind)) + "\nNume client: " + str(
                self.get_nume(ind)) + "\nPrenume: " + str(self.get_prenume(ind))
            print(rez)
        except ValueError as ve:
            print(str(ve))


class Depozit_inchirieri(object):

    def __init__(self):
        self.__listainchirieri = []

    def get_len(self):
        return len(self.__listainchirieri)

    def get_film(self, ind):
        return self.__listainchirieri[ind][0]

    def get_client(self, ind):
        return self.__listainchirieri[ind][1]

    def adauga_inchiriere(self, idfilm, idclient, repo_filme, repo_clienti):
        """
        Functia primeste idul filmului, idul clientului si depozitele celor 2, iar daca se gasesc filmul si clientul dupa id, creeaza inchirierea si modifica datele necesare in repo.client si repo.film.
        :param idfilm:
        :param idclient:
        :param repo_filme:
        :param repo_clienti:
        :return:
        """
        try:
            film = repo_filme.verificare_film_in_lista_inchiriere(idfilm)
            client = repo_clienti.verificare_client_in_lista_inchiriere(idclient)
            self.__verifica_inchiriere_noua(idfilm, idclient)

            film.set_nr_inchirieri(film.get_nr_inchirieri() + 1)
            client.set_nr_filme_inchiriate(client.get_nr_filme_inchiriate() + 1)

            repo_filme.modifica_film_inchirieri(film, film.get_id())
            repo_clienti.modifica_client_inchirieri(client, client.get_id())

            self.__listainchirieri.append([film, client, self.get_len()])
            print("Inchiriere realizata cu succes!")
        except ValueError:
            print("film/ client inexistent")
        except AttributeError as ae:
            print(str(ae))

    def sterge_inchiriere(self, idinchiriere, repo_filme, repo_clienti):
        """
        Functia primeste id-ul inchirierii si depozitele filmului si clientului aferent inchirierii, iar daca se gaseste inchirierea, aceasta se sterge, modificandu-se datele necesare in repo_film, repo_client.
        :param idinchiriere:
        :param repo_filme:
        :param repo_clienti:
        :return:
        """
        try:
            ind = self.__verifica_inchiriere_existenta(idinchiriere)
            film = self.__listainchirieri[ind][0]
            client = self.__listainchirieri[ind][1]

            film.set_nr_inchirieri(film.get_nr_inchirieri() - 1)
            client.set_nr_filme_inchiriate(client.get_nr_filme_inchiriate() - 1)

            repo_filme.modifica_film_inchirieri(film, film.get_id())
            repo_clienti.modifica_client_inchirieri(client, client.get_id())

            self.__listainchirieri.pop(ind)
            print("Returnare realizata cu succes!")
        except ValueError as ve:
            print(str(ve))

    def __verifica_inchiriere_noua(self, idfilm, idclient):
        """
        Se verifica daca aceasta inchiriere nu a mai fost realizata. Arunca exceptie in caz contrar.
        :param idfilm:
        :param idclient:
        :return:
        """
        erori = ""
        for ind in range(self.get_len()):
            filmcurent = self.__listainchirieri[ind][0]
            clientcurent = self.__listainchirieri[ind][1]
            if idfilm == filmcurent.get_id() and idclient == clientcurent.get_id():
                erori = "inchiriere deja existenta"
                break
        if erori:
            raise AttributeError(str(erori))

    def __verifica_inchiriere_existenta(self, idinchiriere):
        """
        Se verifica daca inchirierea data dupa id s-a realizat. Arunca exceptie in caz contrar.
        :param idinchiriere:
        :return:
        """
        gasit = 0
        for ind in range(self.get_len()):
            idcurent = self.__listainchirieri[ind][2]
            if idcurent == idinchiriere:
                return ind
        if not gasit:
            raise ValueError("Nu exista inchiriere cu acest id!")


"""----------------------------------------------------------------------------------------FILE REPO----------------------------------------------------------------------------------------------------"""


class Depozit_DTO(object):

    def __init__(self, repo_filme, repo_clienti):
        self.__repo_filme = repo_filme
        self.__repo_clienti = repo_clienti

    def get_all_filme(self):
        return self.__repo_filme

    def get_all_clienti(self):
        return self.__repo_clienti

    def set_all_filme(self, other):
        self.__repo_filme = other

    def set_all_clienti(self, other):
        self.__repo_clienti = other


class Depozit_inchirieri_File(object):

    def __init__(self, filename):
        self._filename = filename
        self.__listainchirieri = self.load_from_file()

    def get_len(self):
        return len(self.__listainchirieri)

    def get_film(self, ind):
        return self.__listainchirieri[ind][0]

    def get_client(self, ind):
        return self.__listainchirieri[ind][1]

    def get_id(self, ind):
        return self.__listainchirieri[ind][2]

    def adauga_inchiriere(self, idfilm, idclient, repo_filme, repo_clienti):
        """
        Functia primeste idul filmului, idul clientului si depozitele celor 2, iar daca se gasesc filmul si clientul dupa id, creeaza inchirierea si modifica datele necesare in repo.client si repo.film.
        :param idfilm:
        :param idclient:
        :param repo_filme:
        :param repo_clienti:
        :return:
        """
        try:
            film = repo_filme.verificare_film_in_lista_inchiriere(idfilm)
            client = repo_clienti.verificare_client_in_lista_inchiriere(idclient)
            self.__verifica_inchiriere_noua(idfilm, idclient)
            self.__listainchirieri.append([film, client, self.get_len()])
            print("Inchiriere realizata cu succes!")
        except ValueError:
            print("film/ client inexistent")
        except AttributeError as ae:
            print(str(ae))
        self.__save_to_file(self.__listainchirieri)

    def sterge_inchiriere(self, idinchiriere, repo_filme, repo_clienti):
        """
        Functia primeste id-ul inchirierii si depozitele filmului si clientului aferent inchirierii, iar daca se gaseste inchirierea, aceasta se sterge, modificandu-se datele necesare in repo_film, repo_client.
        :param idinchiriere:
        :param repo_filme:
        :param repo_clienti:
        :return:
        """
        try:
            ind = self.__verifica_inchiriere_existenta(idinchiriere)
            film = self.__listainchirieri[ind][0]
            client = self.__listainchirieri[ind][1]

            film.set_nr_inchirieri(film.get_nr_inchirieri() - 1)
            client.set_nr_filme_inchiriate(client.get_nr_filme_inchiriate() - 1)

            self.__listainchirieri.pop(ind)
            print("Returnare realizata cu succes!")
        except ValueError as ve:
            print(str(ve))
        self.__save_to_file(self.__listainchirieri)

    def __verifica_inchiriere_noua(self, idfilm, idclient):
        """
        Se verifica daca aceasta inchiriere nu a mai fost realizata. Arunca exceptie in caz contrar.
        :param idfilm:
        :param idclient:
        :return:
        """
        erori = ""
        for ind in range(self.get_len()):
            filmcurent = self.__listainchirieri[ind][0]
            clientcurent = self.__listainchirieri[ind][1]
            if idfilm == filmcurent.get_id() and idclient == clientcurent.get_id():
                erori = "inchiriere deja existenta"
                break
        if erori:
            raise AttributeError(str(erori))

    def __verifica_inchiriere_existenta(self, idinchiriere):
        """
        Se verifica daca inchirierea data dupa id s-a realizat. Arunca exceptie in caz contrar.
        :param idinchiriere:
        :return:
        """
        gasit = 0
        for ind in range(self.get_len()):
            idcurent = self.__listainchirieri[ind][2]
            if idcurent == idinchiriere:
                return ind
        if not gasit:
            raise ValueError("Nu exista inchiriere cu acest id!")

    def load_from_file(self):
        try:
            f = open(self._filename, "r")
        except IOError:
            raise WrongFileError()

        listainchirieri = []
        lines = f.readlines()
        for line in lines:
            entitati = line.split("/")
            film = entitati[0]
            client = entitati[1]
            idinchiriere = int(entitati[2])
            idfilm, titlu, descriere, gen, nrinchirieri = [token.strip() for token in film.split(";")]
            idclient, nume, prenume, nrfilmeinchiriate = [token.strip() for token in client.split(";")]
            film = Film(idfilm, titlu, descriere, gen)
            film.set_nr_inchirieri(nrinchirieri)
            client = Client(idclient, nume, prenume)
            client.set_nr_filme_inchiriate(nrfilmeinchiriate)
            listainchirieri.append([film, client, idinchiriere])
        f.close()
        return listainchirieri

    def load_from_file1(self):
        try:
            f = open(self._filename, "r")
        except IOError:
            raise WrongFileError

        listainchirieri = []
        while True:
            idfilm = f.readline().strip()
            if not idfilm:
                break
            titlu = f.readline().strip()
            descriere = f.readline().strip()
            gen = f.readline().strip()
            nrinchirieri = f.readline().strip()

            idclient = f.readline().strip()
            nume = f.readline().strip()
            prenume = f.readline().strip()
            nrfilmeinchiriate = f.readline().strip()
            idinchiriere = f.readline().strip()

            film = Film(idfilm, titlu, descriere, gen)
            film.set_nr_inchirieri(nrinchirieri)

            client = Client(idclient, nume, prenume)
            client.set_nr_filme_inchiriate(nrfilmeinchiriate)

            listainchirieri.append([film, client, idinchiriere])

        f.close()
        return listainchirieri

    def __save_to_file(self, listainchirieri):
        with open(self._filename, "w") as f:
            for inchiriere in listainchirieri:
                film = inchiriere[0]
                client = inchiriere[1]
                idinchiriere = inchiriere[2]
                inchirerestring = f"{film.get_id()};{film.get_titlu()};{film.get_descriere()};{film.get_gen()};{film.get_nr_inchirieri()}/{client.get_id()};{client.get_nume()};{client.get_prenume()};{client.get_nr_filme_inchiriate()}/{idinchiriere}\n"
                f.write(inchirerestring)


class Depozit_film_File(Depozit_inchirieri_File):

    def __init__(self, filename):
        self.__filename = filename
        self.__listafilme = self.loadfile()
        for film in self.__listafilme:
            print(str(film))
        Depozit_inchirieri_File.__init__(self,
                                         "C:\\Users\\OTI\\OneDrive\\Desktop\\Facultate\\Probleme Pycharm\\lab7_9_teste\\Datas\\inchrieri.txt")

    def get_len(self):
        return len(self.__listafilme)

    def get_lista_id(self, ind):
        film = self.__listafilme[ind]
        return film.get_id()

    def get_lista_titlu(self, ind):
        film = self.__listafilme[ind]
        return film.get_titlu()

    def get_lista_descriere(self, ind):
        film = self.__listafilme[ind]
        return film.get_descriere()

    def get_lista_gen(self, ind):
        film = self.__listafilme[ind]
        return film.get_gen()

    def get_all(self):
        return self.__listafilme

    def loadfile(self):
        try:
            f = open(self.__filename, "r")
        except IOError:
            raise WrongFileError()

        listafilme = []
        lines = f.readlines()
        for line in lines:
            film_id, film_titlu, film_descriere, film_gen, film_nr_inchirieri = [token.strip() for token in
                                                                                 line.split(";")]
            film = Film(film_id, film_titlu, film_descriere, film_gen)
            film.set_nr_inchirieri(film_nr_inchirieri)
            listafilme.append(film)

        f.close()
        return listafilme

    def add_film_in_lista(self, film):
        """
               Functia adauga un film in lista, daca acesta trece de validator.
               Input: film - class
               :param film:
               :return:
               """
        try:
            self.__verificare_film_nou(film)
            self.__listafilme.append(film)
            print("Film adaugat cu succes!")
        except ValueError as ve:
            print(str(ve))
        self.save_to_file(self.__listafilme)

    def del_film_in_lista(self, id):
        """
        Functia sterge un film din lista dupa id, daca acesta trece de validator.
        Input: id - int
        :param id:
        :return:
        """
        try:
            ind = self.verificare_film_in_lista_recursiv(id, 0)
            film = self.__listafilme[ind]
            self.__listafilme.pop(ind)
            # self.stergere_film_inchirieri(film)
            print("Film sters cu succes!")
        except ValueError as ve:
            print(str(ve))
        self.save_to_file(self.__listafilme)

    def modifica_film(self, film, id):
        """
        Functia modifica un film din lista dupa id, daca acesta trece de validator.
        Input: film - class, id - int
        :param film:
        :param id:
        :return:
        """
        try:
            ind = self.verificare_film_in_lista_recursiv(id, 0)
            self.__listafilme[ind] = film
            # self.modifica_film_inchirieri(film)
            print("Film modificat cu succes!")
        except ValueError as ve:
            print(str(ve))
        self.save_to_file(self.__listafilme)

    def verificare_film_in_lista_recursiv(self, id, ind):
        """
        Functia verifica daca filmul exista deja in lista pentru a-l putea sterge/modifica.
        Input: id -int
        Output: (daca exista) ind - indicele la care se afla filmul
        :param id:
        :return:
        """
        if ind >= self.get_len():
            raise ValueError("nu exista client cu acest id")
        elif id == self.get_lista_id(ind):
            return ind
        else:
            return self.verificare_film_in_lista_recursiv(id, ind + 1)

    def verificare_film_in_lista_inchiriere(self, id):
        """
        Functia verifica daca filmul exista deja in lista pentru a-l putea sterge/modifica.
        Input: id -int
        Output: (daca exista) ind - indicele la care se afla filmul
        :param id:
        :return:
        """
        gasit = 0
        for ind in range(self.get_len()):
            if id == self.get_lista_id(ind):
                return self.__listafilme[ind]
        if not gasit:
            raise ValueError("nu exista film cu acest id")

    def save_to_file(self, listafilme):

        with open(self.__filename, "w") as f:
            for film in listafilme:
                filmstring = str(film.get_id()) + ";" + str(film.get_titlu()) + ";" + str(
                    film.get_descriere()) + ";" + str(film.get_gen()) + ";" + str(film.get_nr_inchirieri()) + "\n"
                f.write(filmstring)

    def __verificare_film_nou(self, film):
        """
        Functia verifica daca filmul este unul nou. In caz contrar, arunca o exceptie.
        Input: id
        :param film:
        :return:
        """
        eroare = ""
        for ind in range(self.get_len()):
            if film.get_id() == self.get_lista_id(ind):
                if eroare:
                    eroare += "\n"
                eroare += "id deja existent"
                break
            if film.get_titlu() == self.get_lista_titlu(ind) and film.get_gen() == self.get_lista_gen(ind):
                if eroare:
                    eroare += "\n"
                eroare += "film deja existent"
                break
        if eroare:
            raise ValueError(str(eroare))

    def loadfile1(self):
        try:
            f = open(self.__filename, "r")
        except IOError:
            raise WrongFileError
        listafilme = []
        while True:
            idfilm = f.readline().strip()
            if not idfilm:
                break
            titlu = f.readline().strip()
            descriere = f.readline().strip()
            gen = f.readline().strip()
            nrinchirieri = f.readline().strip()

            film = Film(idfilm, titlu, descriere, gen)
            film.set_nr_inchirieri(nrinchirieri)

            listafilme.append(film)

        f.close()
        return listafilme


class Depozit_client_File(Depozit_inchirieri_File):

    def __init__(self, filename):
        self.__filename = filename
        self.__listaclienti = self.__loadfile()
        Depozit_inchirieri_File.__init__(self,
                                         "C:\\Users\\OTI\\OneDrive\\Desktop\\Facultate\\Probleme Pycharm\\lab7_9_teste\\Datas\\inchrieri.txt")

    def get_len(self):
        return len(self.__listaclienti)

    def get_id(self, ind):
        client = self.__listaclienti[ind]
        return client.get_id()

    def get_nume(self, ind):
        client = self.__listaclienti[ind]
        return client.get_nume()

    def get_prenume(self, ind):
        client = self.__listaclienti[ind]
        return client.get_prenume()

    def get_nr_filme_inchiriate(self, ind):
        client = self.__listaclienti[ind]
        return client.get_nr_filme_inchiriate()

    def get_all(self):
        return self.__listaclienti

    def add_client_in_lista(self, client):
        """
        Functia adauga un client in lista daca trece de validator.
        Input: id -int
        :param client:
        :return:
        """
        try:
            self.verificare_client_nou(client)
            self.__listaclienti.append(client)
            print("Client adaugat cu succes! Numar filme inchiriate: 0")
        except ValueError as ve:
            print(str(ve))
        self.__save_to_file(self.__listaclienti)

    def verificare_client_nou(self, client):
        """
        Functia verifica daca clientul este unul nou.
        Input: client - class
        :param client:
        :return:
        """
        eroare = ""
        id = int(client.get_id())
        for ind in range(self.get_len()):
            if id == self.get_id(ind):
                eroare += "id deja existent"
                break
        nume = client.get_nume()
        prenume = client.get_prenume()
        for ind in range(self.get_len()):
            if nume == self.get_nume(ind) and prenume == self.get_prenume(ind) and id == self.get_id(ind):
                if eroare:
                    eroare += "\n"
                eroare += "client deja existent"
        if eroare:
            raise ValueError(str(eroare))

    def del_client(self, id):
        """
        Functia sterge un client dupa id din lista daca trece de validator.
        Input: id - int
        :param id:
        :return:
        """
        try:
            ind = self.verificare_client_in_lista_recursiv(id, 0)
            self.__listaclienti.pop(ind)
            # self.stergere_client_inchirieri(client, repo_filme)
            print("Client sters cu succes!")
        except ValueError as ve:
            print(str(ve))
        self.__save_to_file(self.__listaclienti)

    def verificare_client_in_lista_recursiv(self, id, ind):
        """
        Functia verifica un client daca este in lista.
        Input: id - int
        :param id:
        :return:
        """
        if ind >= self.get_len():
            raise ValueError("nu exista client cu acest id")
        elif id == self.get_id(ind):
            return ind
        else:
            return self.verificare_client_in_lista_recursiv(id, ind + 1)

    def verificare_client_in_lista_inchiriere(self, id):
        """
        Functia verifica un client daca este in lista.
        Input: id - int
        :param id:
        :return:
        """
        gasit = 0
        for ind in range(self.get_len()):
            if id == self.get_id(ind):
                return self.__listaclienti[ind]
        if not gasit:
            raise ValueError("nu exista client cu acest id")

    def modifica_client(self, client, id):
        """
        Functia modifica client dupa id daca acesta trece de validator.
        Input: client - class
               id - int
        :param client:
        :param id:
        :return:
        """
        try:
            ind = self.verificare_client_in_lista_recursiv(id, 0)
            self.__listaclienti[ind] = client
            # self.modifica_client_inchirieri(client)
            print("Client modificat cu succes!")
        except ValueError as ve:
            print(str(ve))
        self.__save_to_file(self.__listaclienti)

    def cauta_client(self, id):
        """
        Functia cauta client dupa id si il afiseaza daca il gaseste, in caz contrar, semnaleaza eroarea.
        :param id:
        :return:
        """
        try:
            ind = self.verificare_client_in_lista_recursiv(id, 0)
            rez = "Id client: " + str(self.get_id(ind)) + "\nNume client: " + str(
                self.get_nume(ind)) + "\nPrenume: " + str(self.get_prenume(ind))
            print(rez)
        except ValueError as ve:
            print(str(ve))

    def __loadfile(self):
        try:
            f = open(self.__filename, "r")
        except IOError:
            raise WrongFileError()

        listaclienti = []
        lines = f.readlines()
        for line in lines:
            client_id, client_nume, client_prenume, client_nr_filme_inchiriate = [token.strip() for token in
                                                                                  line.split(";")]
            client = Client(client_id, client_nume, client_prenume)
            client.set_nr_filme_inchiriate(client_nr_filme_inchiriate)
            listaclienti.append(client)
        f.close()
        return listaclienti

    def loadfile1(self):
        try:
            f = open(self.__filename, "r")
        except IOError:
            raise WrongFileError
        listaclienti = []
        while True:
            idclient = f.readline().strip()
            if not idclient:
                break

            nume = f.readline().strip()
            prenume = f.readline().strip()
            nrfilmeinchiriate = f.readline().strip()

            client = Client(idclient, nume, prenume)
            client.set_nr_filme_inchiriate(nrfilmeinchiriate)

            listaclienti.append(client)

        f.close()
        return listaclienti

    def __save_to_file(self, listaclienti):

        with open(self.__filename, "w") as f:
            for client in listaclienti:
                clientstring = f"{client.get_id()};{client.get_nume()};{client.get_prenume()};{client.get_nr_filme_inchiriate()}\n"
                f.write(clientstring)


class WrongFileError(Exception):
    pass
