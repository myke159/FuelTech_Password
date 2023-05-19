import pyautogui
from time import sleep



class Broken():

    def __init__(self):
        pass





    def rec(self, novon):
        if pyautogui.locateCenterOnScreen('abrir_da_injecao.png', confidence=0.9):
            qdd = pyautogui.locateCenterOnScreen('abrir_da_injecao.png', confidence=0.9)
            pyautogui.moveTo(qdd.x, qdd.y)
            pyautogui.click()
            sleep(0.25)
            pyautogui.write(novon)
            sleep(0.25)
            pyautogui.press("enter")
            sleep(0.25)
            if pyautogui.locateCenterOnScreen('senha_invalida.png', confidence=0.9):
                print(f"SENHA ERRADA: {novon}")
                self.adicionar(novon)
                pyautogui.press("enter")
            else:
                print(f"SENHA CORRETA: {novon}")
                self.adicionar(f"{novon} ----- SENHA CORRETA -----")
                self.senha_correta(f"{novon} ----- SENHA CORRETA -----")
                return True




    #todas as possibilidades
    def possibilidades(self):
        for numero in range(1351, 10000):
            novon = self.conversor(numero)
            self.rec(novon)
            if self.rec == True:
                print("STOP")
                break

    #converte o numero até mil, para se adaptar a senha
    def conversor(self, numero):
        numero = str(numero)
        tamanho = len(numero)

        if tamanho == 1:
            return "000"+numero
        if tamanho == 2:
            return "00"+numero
        if tamanho == 3:
            return "0"+numero
        if tamanho == 4:
            return numero

    #adiciona o numero na relação
    def adicionar(self, novon):
        senhas = open("senhas.txt", "a")
        senhas.write(f"\n{novon}")
        senhas.close()


    def senha_correta(self, novon):
        senhas = open("senha_correta.txt", "a")
        senhas.write(f"\n{novon}")
        senhas.close()



if __name__ == "__main__":

    Broken().possibilidades()
    sleep(0.5)