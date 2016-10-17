# -*-coding:Utf-8 -*

class ExceptionChargement(Exception):
    def __init__(self,raison):
        self.raison=raison

    def __str__(self):
        return self.raison


def chargement():
    reponse=False
    while reponse==False:
        question_chargement=input("Êtes-vous chargé : pas du tout, un peu, beaucoup ?")
        if question_chargement!="un peu" and question_chargement!="pas du tout" and question_chargement!="beaucoup":
            raise ExceptionChargement("Vous n'avez pas répondu proprement à la question...")
        else:
            reponse=True
            return question_chargement
