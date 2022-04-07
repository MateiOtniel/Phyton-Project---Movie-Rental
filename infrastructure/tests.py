from lab7_9_teste.domain.objects import Film, Client
from lab7_9_teste.infrastructure.validation import Validator_film, Validator_client, ValidationError
from lab7_9_teste.infrastructure.services import Service_filme, Service_clienti, Service_inchirieri
from lab7_9_teste.repository.repo import Depozit_film, Depozit_client, Depozit_inchirieri
import unittest
class Testari(unittest.TestCase):

    def run_teste(self):
        print("Am inceput testele")
        self.__test_creeaza_film()
        self.__test_valideaza_film()
        self.__test_adauga_film()
        self.__test_valideaza_id()
        self.__test_valideaza_del_film_in_lista()
        self.__test_creeaza_client()
        self.__test_valideaza_client()
        self.__test_adauga_client()
        self.__test_sterge_client()
        self.__test_inchiriaza_returneaza_film()
        self.__test_valideaza_rapoarte()
        print("Am terminat testele")

    def __test_creeaza_film(self):
        id_film = 15
        titlu = "Alba ca zapada"
        descriere = "Film bun"
        gen = "animatie"
        film = Film(id_film, titlu, descriere, gen)
        self.assertTrue(film.get_id() == id_film)
        self.assertTrue(film.get_titlu() == titlu)
        self.assertTrue(film.get_descriere() == descriere)
        self.assertTrue(film.get_gen() == gen)

    def __test_valideaza_film(self):
        id_film = 15
        titlu = "Alba ca zapada"
        descriere = "Film bun"
        gen = "animatie"
        id_film_inv = -2
        titlu_inv = ""
        descriere_inv = ""
        gen_inv = "muste"
        valid_film = Validator_film()

        film = Film(id_film, titlu, descriere, gen)
        self.assertTrue(ValidationError, valid_film.valideaza(film))

        film = Film(id_film_inv, titlu_inv, descriere, gen)
        self.assertRaises(ValidationError, lambda: valid_film.valideaza(film))

        film = Film(id_film, titlu, descriere_inv, gen_inv)
        self.assertRaises(ValidationError, lambda: valid_film.valideaza(film))

    def __test_adauga_film(self):
        id_film = 15
        titlu = "Alba ca zapada"
        descriere = "Film bun"
        gen = "animatie"
        film = Film(id_film, titlu, descriere, gen)
        repo_filme = Depozit_film()
        valid_film = Validator_film()
        srv_film = Service_filme(valid_film, repo_filme)
        srv_film.srv_adauga_film(film)
        self.assertTrue(repo_filme.get_len() == 1)

    def __test_valideaza_id(self):
        valid_film = Validator_film()
        self.assertRaises(ValidationError, lambda: valid_film.valideaza_id(-2))

    def __test_valideaza_del_film_in_lista(self):
        repo_filme = Depozit_film()
        id= 3
        repo_filme.del_film_in_lista(id)
        self.assertTrue(repo_filme.get_len() == 0)
        repo_filme.del_film_in_lista(id)
        self.assertTrue(repo_filme.get_len() == 0)

    def __test_creeaza_client(self):
        id = 15
        nume_valid = "Matei"
        prenume_valid = "Otniel"
        client = Client(id, nume_valid, prenume_valid)
        self.assertTrue(client.get_id() == id)
        self.assertTrue(client.get_nume() == nume_valid)
        self.assertTrue(client.get_prenume() == prenume_valid)

    def __test_valideaza_client(self):
        id_valid = 15
        nume_valid = "Matei"
        prenume_valid = "Otniel"
        id_inv = "asd"
        nume_inv = "6oti"
        prenume_inv = ""
        valid_client = Validator_client()

        client = Client(id_valid, nume_valid, prenume_valid)
        self.assertTrue(ValidationError, lambda: valid_client.valideaza(client))


        client = Client(id_inv, nume_inv, prenume_valid)
        self.assertRaises(ValidationError, lambda: valid_client.valideaza(client))

        client = Client(id_valid, nume_valid, prenume_inv)
        self.assertRaises(ValidationError, lambda: valid_client.valideaza(client))

    def __test_adauga_client(self):
        id_valid = 15
        nume_valid = "Matei"
        prenume_valid = "Otniel"
        client = Client(id_valid, nume_valid, prenume_valid)

        repo_client = Depozit_client()
        repo_client.add_client_in_lista(client)

        self.assertTrue(repo_client.get_len() == 1)
        repo_client.add_client_in_lista(client)
        self.assertTrue(repo_client.get_len() == 1)

    def __test_sterge_client(self):
        id = 2
        repo_client = Depozit_client()

        repo_client.del_client(id)
        self.assertTrue(repo_client.get_len() == 0)

        repo_client.del_client(id)
        self.assertTrue(repo_client.get_len() == 0)

    def __test_inchiriaza_returneaza_film(self):
        repo_inchirieri = Depozit_inchirieri()
        repo_client = Depozit_client()
        repo_filme = Depozit_film()
        srv_inchirieri = Service_inchirieri(repo_filme, repo_client, repo_inchirieri)

        id_valid = 15
        nume_valid = "Matei"
        prenume_valid = "Otniel"
        client = Client(id_valid, nume_valid, prenume_valid)
        repo_client.add_client_in_lista(client)

        id_film = 15
        titlu = "Alba ca zapada"
        descriere = "Film bun"
        gen = "animatie"
        film = Film(id_film, titlu, descriere, gen)
        repo_filme.add_film_in_lista(film)

        srv_inchirieri.adauga_inchiriere(film.get_id(), client.get_id())
        self.assertTrue(repo_inchirieri.get_len() == 1)
        self.assertTrue(film.get_nr_inchirieri() == 2)
        self.assertTrue(client.get_nr_filme_inchiriate() == 2)

        film.set_id(14)
        srv_inchirieri.adauga_inchiriere(film.get_id(), client.get_id())
        self.assertTrue(repo_inchirieri.get_len() == 1)
        self.assertFalse(film.get_nr_inchirieri() == 1)
        self.assertFalse(client.get_nr_filme_inchiriate() == 1)

        id_inchiriere = 0
        srv_inchirieri.sterge_inchiriere(id_inchiriere)
        self.assertTrue(repo_inchirieri.get_len() == 0)
        self.assertFalse(film.get_nr_inchirieri() == 0)
        self.assertFalse(client.get_nr_filme_inchiriate() == 0)

        srv_inchirieri.sterge_inchiriere(id_inchiriere)
        self.assertTrue(repo_inchirieri.get_len() == 0)
        self.assertFalse(film.get_nr_inchirieri() == 0)
        self.assertFalse(client.get_nr_filme_inchiriate() == 0)

    def __test_valideaza_rapoarte(self):
        repo_inchirieri = Depozit_inchirieri()
        repo_client = Depozit_client()
        repo_filme = Depozit_film()
        srv_inchirieri = Service_inchirieri(repo_filme, repo_client, repo_inchirieri)

        id_valid = 15
        nume_valid = "Matei"
        prenume_valid = "Otniel"
        client = Client(id_valid, nume_valid, prenume_valid)
        repo_client.add_client_in_lista(client)

        id_valid = 1
        nume_valid = "Matei"
        prenume_valid = "Otniel"
        client = Client(id_valid, nume_valid, prenume_valid)
        repo_client.add_client_in_lista(client)

        id_film = 15
        titlu = "Alba ca zapada"
        descriere = "Film bun"
        gen = "animatie"
        film = Film(id_film, titlu, descriere, gen)
        repo_filme.add_film_in_lista(film)

        id_film = 1
        titlu = "Alba"
        descriere = "Film bun"
        gen = "animatie"
        film = Film(id_film, titlu, descriere, gen)
        repo_filme.add_film_in_lista(film)

        id_film = 2
        titlu = "Alb"
        descriere = "Film bun"
        gen = "animatie"
        film = Film(id_film, titlu, descriere, gen)
        repo_filme.add_film_in_lista(film)

        id_film = 3
        titlu = "Alb"
        descriere = "Film bun"
        gen = "animatie"
        film = Film(id_film, titlu, descriere, gen)
        repo_filme.add_film_in_lista(film)

        srv_inchirieri.adauga_inchiriere(15, 15)
        srv_inchirieri.adauga_inchiriere(1, 15)
        srv_inchirieri.adauga_inchiriere(1, 1)
        srv_inchirieri.adauga_inchiriere(2, 15)

        self.assertTrue(srv_inchirieri.rapoarte(1,"orice") == "Id client: 1 Nume si prenume client: Matei Otniel Numar filme inchiriate: 2\nId client: 15 Nume si prenume client: Matei Otniel Numar filme inchiriate: 6\n")
        self.assertFalse(srv_inchirieri.rapoarte(2, "orice") == "ID film: 1 Titlu film: Alba Descriere film: Film bun Gen film: animatie Numar inchirieri: 2\nID film: 15 Titlu film: Alba ca zapada Descriere film: Film bun Gen film: animatie Numar inchirieri: 1\nID film: 2 Titlu film: Alb Descriere film: Film bun Gen film: animatie Numar inchirieri: 1\n")
        self.assertTrue(srv_inchirieri.rapoarte(3, "orice") == "Matei Otniel are 6 filme inchiriate!\n")
        self.assertTrue(srv_inchirieri.rapoarte(4, "Alb") == "ID film: 2 Titlu film: Alb Descriere film: Film bun Gen film: animatie Numar inchirieri: 2\n")