class Validator_film(object):

    def valideaza(self, film):
        """
        Functia valideaza id-ul, titlul, descrierea si genul filmului.
        Daca gaseste erori, ridica exceptia ValidationError.
        :param film:
        :return:
        """
        eroare = ""
        try:
            id = film.get_id()
            id = int(id)
            if id < 0:
                if eroare:
                    eroare += "\n"
                eroare += "id invalid"
        except ValueError:
            if eroare:
                eroare += "\n"
            eroare += "id invalid"
        if film.get_titlu() == "":
            if eroare:
                eroare += "\n"
            eroare += "titlu invalid"
        if film.get_descriere() == "":
            if eroare:
                eroare += "\n"
            eroare += "descriere invalida"
        if film.get_gen() != "romanta" and film.get_gen() != "animatie" and film.get_gen() != "SF" and film.get_gen() != "horror" and film.get_gen() != "actiune" and film.get_gen() != "drama" and film.get_gen() != "comedie":
            if eroare:
                eroare += "\n"
            eroare += "gen invalid"
        if len(eroare) > 0:
            raise ValidationError(str(eroare))

    def valideaza_id(self, id):
        """
        Functia valideaza id-ul filmului.
        Daca gaseste erori, ridica eroarea ValueError.
        :param id:
        :return:
        """
        eroare = ""
        try:
            id = int(id)
            if id < 0:
                eroare = "id invalid"
        except ValueError:
            eroare = "id invalid"
        if eroare:
            raise ValidationError(str(eroare))

    def valideaza_titlu(self, titlu):
        erori = ""
        if titlu == "":
            erori = "titlu invalid"
        if len(erori) > 0:
            raise ValidationError(str(erori))


class Validator_client(object):

    def valideaza(self, client):
        """
        Functia valideaza id-ul, numele si prenumele unui nou client.
        Daca gaseste erori, ridica exceptia ValidationError.
        :param client:
        :return:
        """
        erori = ""
        try:
            id = client.get_id()
            id = int(id)
            if id < 0:
                if erori:
                    erori += "\n"
                erori += "id invalid"
        except ValueError:
            if erori:
                erori += "\n"
            erori += "id invalid"

        nume = client.get_nume()
        if not nume or nume[0].islower() or nume[0].isdigit():
            if erori:
                erori += "\n"
            erori += "nume invalid"
        else:
            for ind in range(1, len(nume)):
                if nume[ind].isdigit():
                    if erori:
                        erori += "\n"
                    erori += "nume invalid"
                    break

        prenume = client.get_prenume()
        if not prenume or prenume[0].islower() or prenume[0].isdigit():
            if erori:
                erori += "\n"
            erori += "prenume invalid"
        else:
            for ind in range(1, len(prenume)):
                if prenume[ind].isdigit():
                    if erori:
                        erori += "\n"
                    erori += "prenume invalid"
                    break
        if erori:
            raise ValidationError(str(erori))

    def valideaza_id(self, id):
        """
        Functia valideaza id-ul clientului.
        Daca gaseste erori, ridica eroarea ValueError.
        :param id:
        :return:
        """
        try:
            id = int(id)
            if id < 0:
                raise ValueError("id invalid")
        except ValueError:
            raise ValueError("id invalid")

class ValidationError(Exception):
    pass