class Service_filme(object):

    def __init__(self, valid_film, repo_filme):
        self.__valid_film = valid_film
        self.__repo_filme = repo_filme

    def srv_adauga_film(self, film):
        """
        Functia trimite clasa film spre repository pentru a fi adaugat in lista.
        Input: film
        :param film:
        :return:
        """
        self.__repo_filme.add_film_in_lista(film)

    def srv_sterge_film(self, id):
        """
         Functia trimite id-ul unui film spre repository pentru a fi sters(daca se poate) din lista.
        Input: id
        :param id:
        :return:
        """
        self.__repo_filme.del_film_in_lista(id)

    def srv_modifica_film(self, film, id):
        """
        Functia trimite clasa film, impreuna cu un id spre repository pentru a fi modificat(daca se poate).
        Input: film, id
        :param film:
        :return:
        """
        self.__repo_filme.modifica_film(film, id)

    def srv_caut_film(self, id):
        """
        Functia primeste id-ul si cauta in repo_film filmul dupa id.
        :param id:
        :return:
        """
        self.__repo_filme.cauta_film(id)

class Service_clienti(object):

    def __init__(self, valid_client, repo_clienti):
        self.__valid_client = valid_client
        self.__repo_clienti = repo_clienti

    def srv_adauga_client(self, client):
        """
        Functia trimite clasa client spre repository pentru a fi adaugat in lista.
        Input: client
        :param client:
        :return:
        """
        self.__repo_clienti.add_client_in_lista(client)

    def srv_sterge_client(self, id):
        """
        Functia trimite id-ul unui client spre repository pentru a fi sters(daca se poate) din lista.
        Input: id
        :param id:
        :return:
        """
        self.__repo_clienti.del_client(id)

    def srv_modifica_client(self, client, id):
        """
        Functia trimite clasa client, impreuna cu un id spre repository pentru a fi modificat(daca se poate).
        Input: client, id
        :param client:
        :return:
        """
        self.__repo_clienti.modifica_client(client, id)

    def srv_caut_client(self, id):
        """
        Functia primeste id-ul clientului si cauta in repo_client clientul dupa id.
        :param id:
        :return:
        """
        self.__repo_clienti.cauta_client(id)

class Service_inchirieri(object):

    def __init__(self, repo_filme, repo_clienti, repo_inchirieri):
        self.__repo_filme = repo_filme
        self.__repo_clienti = repo_clienti
        self.__repo_inchirieri = repo_inchirieri

    def adauga_inchiriere(self, idfilm, idclient):

        client = self.__repo_clienti.verificare_client_in_lista_inchiriere(idclient)
        client.set_nr_filme_inchiriate(client.get_nr_filme_inchiriate() + 1)
        self.__repo_clienti.modifica_client(client, client.get_id())

        film = self.__repo_filme.verificare_film_in_lista_inchiriere(idfilm)
        film.set_nr_inchirieri(film.get_nr_inchirieri() + 1)
        self.__repo_filme.modifica_film(film, film.get_id())

        self.__repo_inchirieri.adauga_inchiriere(idfilm, idclient, self.__repo_filme, self.__repo_clienti)

    def sterge_inchiriere(self, id_inchiriere):
        self.__repo_inchirieri.sterge_inchiriere(id_inchiriere, self.__repo_filme, self.__repo_clienti)
        
    def rapoarte(self, cerinta, prefix):
        if cerinta == 1:
            return self.subcerinta1()
        elif cerinta == 2:
            return self.subcerinta2()
        elif cerinta == 3:
            return self.subcerinta3()
        elif cerinta == 4:
            return self.subcerinta4(prefix)

    def subcerinta1(self):
        """
        Functia sorteaza dupa nume si id lista de clienti, si ii afiseaza in ordine crescatoare pe acei clienti care au filme inchiriate.
        :return:
        """
        lista = self.__repo_clienti.get_all()
        copie_lista = [None]*len(lista)
        self.sortare_lista_merge(lista, copie_lista, 0, len(copie_lista) - 1, key = lambda x: (x.get_nume(), x.get_nr_filme_inchiriate()), cmp = lambda x, y: (x <= y))
        return self.creare_rez_subcerinta_1(lista)

    def subcerinta2(self):
        """
        Functia sorteaza descrescator filmele cu cele mai multe inchirieri si returneaza 3 filme, cele mai inchiriate.
        :return:
        """
        lista = self.__repo_filme.get_all()
        copie_lista = lista[:]
        self.bingo_sort(copie_lista, 0, -1, key = lambda x : x.get_nr_inchirieri(), cmp = lambda x,y: (x > y))
        return self.creare_rez_subcerinta_2(copie_lista)

    def subcerinta3(self):
        """
        Functia sorteaza descrescator clientii cu cele mai multe filme inchiriate si ii returneaza pe primii 30%.
        :return:
        """
        lista = self.__repo_clienti.get_all()
        for ind1 in range(len(lista) - 1):
            for ind2 in range(ind1 + 1, len(lista)):
                client1 = lista[ind1]
                client2 = lista[ind2]
                if client1.get_nr_filme_inchiriate() < client2.get_nr_filme_inchiriate():
                    lista[ind1], lista[ind2] = lista[ind2], lista[ind1]
        return self.creare_rez_subcerinta_3(lista)

    def creare_rez_subcerinta_1(self, lista):
        """
        Functia creaza rezultatul pentru subcerinta 1.
        :param lista:
        :return:
        """
        rez = ""
        for client in lista:
            if client.get_nr_filme_inchiriate():
                rez += str(client) + "\n"
        if rez:
            return rez
        else:
            return "Nu exista clienti de ordonat."

    def creare_rez_subcerinta_2(self, lista):
        """
        Functia creaza rezultatul pentru subcerinta 2.
        :param lista:
        :return:
        """
        rez = ""
        for film in lista[:3]:
            if film.get_nr_inchirieri():
                rez += str(film) + "\n"
        if rez:
            return rez
        else:
            return "Nu exista filme inchiriate."

    def creare_rez_subcerinta_3(self, lista):
        """
        Functia creaza rezultatul pentru subcerinta 2.
        :param lista:
        :return:
        """
        rez = ""
        length = int(max(1, (30 * len(lista)//100)))
        for ind in range(length):
            client = lista[ind]
            rez += client.get_nume() + " " + client.get_prenume() + " are " + str(client.get_nr_filme_inchiriate())  + " filme inchiriate!"+ "\n"
        if rez:
            return rez
        else:
            return "Nu exista clienti de ordonat."

    def subcerinta4(self, prefix):
        """
        Functia sorteaza lista descrescator dupa numarul de inchirieri.
        :param prefix:
        :return:
        """
        listafilme = self.__repo_filme.get_all()
        for ind1 in range(len(listafilme) - 1):
            for ind2 in range(ind1 + 1, len(listafilme)):
                film1 = listafilme[ind1]
                film2 = listafilme[ind2]
                if film1.get_nr_inchirieri() > film2.get_nr_inchirieri() or (film1.get_nr_inchirieri() == film2.get_nr_inchirieri() and film1.get_titlu() > film2.get_titlu()):
                    listafilme[ind1], listafilme[ind2] = listafilme[ind2], listafilme[ind1]
        return self.creare_rez_subcerinta_4(listafilme, prefix)

    def creare_rez_subcerinta_4(self, listafilme, prefix):
        rez = ""
        jumatate = len(listafilme)//2
        for film in listafilme:
            if not jumatate:
                break
            if self.verificare_film_prefix(film.get_titlu(), prefix):
                rez += str(film) + "\n"
                jumatate -= 1
        if rez == "":
            rez = "Nu exista filme care sa corespunda cerintei."
        return rez

    def verificare_film_prefix(self, titlufilm, prefix):
        if len(titlufilm) < len(prefix):
            return 0
        for ind in range(len(prefix)):
            if titlufilm[ind] != prefix[ind]:
                return 0
        return 1

    def sortare_lista_merge(self, lista, copie_lista, st, dr, key, cmp):
        """
        Functioa sorteaza lista cu modalitatea merge sort, folosind recursivitatea si interclasarea.
        :param copie_lista:
        :param st:
        :param dr:
        :return:
        """
        if st >= dr:
            return
        mijloc = (st + dr) // 2
        self.sortare_lista_merge(lista, copie_lista, st, mijloc, key, cmp)
        self.sortare_lista_merge(lista, copie_lista, mijloc + 1, dr, key, cmp)
        ind1, ind2, k = st, mijloc +1, -1
        while ind1 <= mijloc and ind2 <= dr:
            if cmp(key(lista[ind1]), key(lista[ind2])):
                k = k + 1
                copie_lista[k] = lista[ind1]
                ind1 += 1
            else:
                k = k + 1
                copie_lista[k] = lista[ind2]
                ind2 += 1
        while ind1 <= mijloc:
            k = k + 1
            copie_lista[k] = lista[ind1]
            ind1 += 1
        while ind2 <= dr:
            k = k + 1
            copie_lista[k] = lista[ind2]
            ind2 += 1
        lista[st :dr + 1] = copie_lista[:dr - st + 1]

    def bingo_sort(self, copie_lista, start, max_val, key, cmp):
        """
        Functia realizeaza sortarea dupa metoda bingo sort, parcurgand de 2 ori lista, unul pentru a afla valoare maxima curenta, iar celalalta pentru
        a muta valoarea/valorile maxime curente in pozitia corespunzatoare.
        :param copie_lista:
        :param start:
        :param max_val:
        :return:
        """
        if start >= len(copie_lista) - 1:
            return

        for ind in range(start, len(copie_lista) - 1):
            film = copie_lista[ind]
            if cmp(key(film), max_val):
                max_val = film.get_nr_inchirieri()

        nr_val_max = 0
        for ind in range(start, len(copie_lista) - 1):
            film = copie_lista[ind]
            if key(film) == max_val:
                copie_lista[start + nr_val_max], copie_lista[ind] = copie_lista[ind], copie_lista[start + nr_val_max]
                nr_val_max += 1

        start = start + nr_val_max
        self.bingo_sort(copie_lista, start, -1, key, cmp)