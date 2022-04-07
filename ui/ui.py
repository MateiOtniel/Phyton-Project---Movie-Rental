import random
from lab7_9_teste.infrastructure.services import Service_filme, Service_clienti, Service_inchirieri
from lab7_9_teste.repository.repo import Depozit_film, Depozit_client, Depozit_inchirieri, Depozit_film_File, Depozit_client_File, Depozit_inchirieri_File, Depozit_DTO
from lab7_9_teste.infrastructure.tests import Testari
from lab7_9_teste.infrastructure.validation import Validator_film, Validator_client, ValidationError
from lab7_9_teste.domain.objects import Film, Client
class Consola(object):

    def __init__(self, srv_film, srv_client, srv_inchirieri):
        self.__srv_film = srv_film
        self.__srv_client = srv_client
        self.__srv_inchirieri = srv_inchirieri

    print("Lista de comenzi:")
    print("add_film - adauga film")
    print("del_film - sterge film dupa id")
    print("mod_film - modifica film dupa id")
    print("add_client - adauga client")
    print("del_client - sterge client dupa id")
    print("mod_client - modifica client dupa id")
    print("caut_film - cauta film dupa id")
    print("caut_client - cauta client dupa id")
    print("gen_clienti - genereaza clienti random")
    print("get_filme - genereaza filme random")
    print("return_film - returnare film")
    print("raports - rapoarte (se filtreaza datele dupa anumite criterii)")

    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                print("Ati iesit din program.")
                return
            elif cmd == "add_film":
                film = self.__ui_citeste_film()
                self.__srv_film.srv_adauga_film(film)
            elif cmd == "del_film":
                id = self.__ui_alege_id_del_film()
                self.__srv_film.srv_sterge_film(int(id))
            elif cmd == "mod_film":
                id = self.__ui_alege_id_mod()
                film = self.__ui_citeste_film()
                self.__srv_film.srv_modifica_film(film, id)
            elif cmd == "add_client":
                client = self.__ui_citeste_client()
                self.__srv_client.srv_adauga_client(client)
            elif cmd == "del_client":
                id = self.__ui_alege_id_del_client()
                self.__srv_client.srv_sterge_client(id)
            elif cmd == "mod_client":
                id = self.__ui_alege_id_mod_client()
                client = self.__ui_citeste_client()
                self.__srv_client.srv_modifica_client(client, id)
            elif cmd == "caut_film":
                id = self.__ui_alege_id_caut_film()
                self.__srv_film.srv_caut_film(id)
            elif cmd == "caut_client":
                id = self.__ui_alege_id_caut_client()
                self.__srv_client.srv_caut_client(id)
            elif cmd == "gen_clienti":
                self.__genereaza_clienti_random()
            elif cmd == "gen_filme":
                self.__genereaza_filme_random()
            elif cmd == "rent_film":
                idfilm = self.__ui_alege_id_caut_film()
                idclient = self.__ui_alege_id_caut_client()
                self.__srv_inchirieri.adauga_inchiriere(idfilm, idclient)
            elif cmd == "return_film":
                id_inchiriere = self.__ui_alege_id_inchiriere()
                self.__srv_inchirieri.sterge_inchiriere(id_inchiriere)
            elif cmd == "raports":
                cerinta = self.__ui_raport()
                prefix = ""
                if cerinta == 4:
                    print("Dati prefixul unui film: ", end="")
                    prefix = input()
                rez = self.__srv_inchirieri.rapoarte(cerinta, prefix)
                print(rez)
            else:
                print("Comanda invalida!")

    def __ui_citeste_film(self):
        while True:
            try:
                print("id: ", end="")
                id = input()
                print("titlu: ", end="")
                titlu = input()
                print("descriere: ", end="")
                descriere = input()
                print("gen: ", end="")
                gen = input()
                return self.__ui_creeaza_film(id, titlu, descriere, gen)
            except ValidationError as ve:
                print(str(ve))

    def __ui_creeaza_film(self, id, titlu, descriere, gen):
        film = Film(id, titlu, descriere, gen)
        valid_film.valideaza(film)
        return film

    def __ui_alege_id_del_film(self):
        while True:
            print("Sterge film dupa id: ", end="")
            try:
                id = input()
                valid_film.valideaza_id(id)
                return id
            except ValidationError as ve:
                print(str(ve))

    def __ui_alege_id_mod(self):
        while True:
            print("Alege film dupa id, apoi adauga informatiile necesare: ", end="")
            try:
                id = int(input())
                valid_film.valideaza_id(id)
                return id
            except ValidationError as ve:
                print(str(ve))
            except ValueError:
                print("id invalid")

    def __ui_citeste_client(self):
        while True:
            try:
                print("id: ", end="")
                id = input()
                print("nume: ", end = "")
                nume = input()
                print("prenume: ", end = "")
                prenume = input()
                return self.__ui_creeaza_client(id, nume, prenume)
            except ValidationError as ve:
                print(str(ve))

    def __ui_creeaza_client(self, id, nume, prenume):
        client = Client(id, nume, prenume)
        valid_client.valideaza(client)
        return client

    def __ui_alege_id_del_client(self):
        while True:
            print("Sterge client dupa id: ", end="")
            try:
                id = input()
                valid_client.valideaza_id(id)
                return int(id)
            except ValueError as ve:
                print(str(ve))

    def __ui_alege_id_mod_client(self):
        while True:
            print("Modifica client dupa id: ", end="")
            try:
                id = input()
                valid_client.valideaza_id(id)
                return int(id)
            except ValueError as ve:
                print(str(ve))

    def __ui_alege_titlu_film(self):
        while True:
            print("Alege titlu film: ", end="")
            try:
                titlu = input()
                valid_film.valideaza_titlu(titlu)
                return titlu
            except ValidationError as ve:
                print(str(ve))

    def __ui_alege_id_caut_film(self):
        while True:
            print("Cauta film dupa id: ", end="")
            try:
                id = input()
                valid_client.valideaza_id(id)
                return int(id)
            except ValueError as ve:
                print(str(ve))

    def __ui_alege_id_caut_client(self):
        while True:
            print("Cauta client dupa id: ", end="")
            try:
                id = input()
                valid_client.valideaza_id(id)
                return int(id)
            except ValueError as ve:
                print(str(ve))

    def __genereaza_clienti_random(self):
        nr = random.randint(1, 10)
        for ind in range(nr):
            id = random.randint(1,100)
            lung = random.randint(1, 20)
            nume = ""
            for litera in range(lung):
                if litera == 0:
                    lit = random.randint(65, 90)
                else:
                    lit = random.randint(97, 122)
                nume += chr(lit)
            prenume = ""
            lung = random.randint(1, 20)
            for litera in range(lung):
                if litera == 0:
                    lit = random.randint(65, 90)
                else:
                    lit = random.randint(97, 122)
                prenume += chr(lit)
            print(str(id) + " " + nume + " " + prenume)
            client = Client(id, nume, prenume)
            srv_client.srv_adauga_client(client)

    def __genereaza_filme_random(self):
        nr = random.randint(1, 10)
        for ind in range(nr):
            id = random.randint(1, 100)
            lung = random.randint(1, 20)
            titlu = ""
            for litera in range(lung):
                if litera == 0:
                    lit = random.randint(65, 90)
                else:
                    lit = random.randint(97, 122)
                titlu += chr(lit)
            descriere = ""
            for litera in range(lung):
                lit = random.randint(97, 122)
                descriere += chr(lit)
            genuri = "romanta animatie SF horror actiune drama comedie"
            gen = genuri.split()
            tip = random.randint(0, 6)
            film = self.__ui_creeaza_film(id, titlu, descriere, gen[tip])
            srv_film.srv_adauga_film(film)
            print(str(id) + " " + titlu + " "+ descriere + " " +gen[tip])

    def __ui_alege_id_inchiriere(self):
        while True:
            print("Cauta inchiriere dupa id: ", end="")
            try:
                id = input()
                valid_client.valideaza_id(id)
                return int(id)
            except ValueError as ve:
                print(str(ve))

    def __ui_raport(self):
        print("Alege una din cerinte: ")
        print("1 - Clienți cu filme închiriate ordonat dupa: nume, după numărul de filme închiriate")
        print("2 - Top 3 cele mai inchiriate filme.")
        print("3 - Primi 30% clienti cu cele mai multe filme (nume client și numărul de filme închiriate)")
        print("4 - Top 50% cele mai putin inchiriate filme care incep cu un string dat, sortate alfabetic dupa nume.")
        while True:
            cmd = input()
            if cmd == "1":
                return 1
            elif cmd == "2":
                return 2
            elif cmd == "3":
                return 3
            elif cmd == "4":
                return 4
            else:
                print("Introduceti o valoare valida!")

if __name__ == '__main__':
    valid_film = Validator_film()
    valid_client = Validator_client()

    repo_filme = Depozit_film_File("Datas/filme.txt")
    #repo_filme = Depozit_film()
    repo_clienti = Depozit_client_File("Datas/clienti.txt")
    #repo_clienti = Depozit_client()
    #repo_inchirieri = Depozit_inchirieri()
    repo_DTO = Depozit_DTO(repo_filme, repo_clienti)
    repo_inchirieri = Depozit_inchirieri_File("Datas/inchrieri.txt")

    srv_film = Service_filme(valid_film, repo_filme)
    srv_client = Service_clienti(valid_client, repo_clienti)
    srv_inchirieri = Service_inchirieri(repo_filme, repo_clienti, repo_inchirieri)

    teste = Testari()
    teste.run_teste()

    ui = Consola(srv_film, srv_client, srv_inchirieri)
    ui.run()