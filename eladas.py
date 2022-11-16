# Faragó Csaba                  1. A forráskód elején írja megjegyzésbe saját nevét, csoportját és az aktuális dátumot.
# SZOFT I_1_E
# 2022-11-17

from jarmu import Jarmu         # 3. Importálja a jarmu.py állományból a Jarmu osztályt.

class App:
    def __init__(self):
        self.jarmuLista = []

    def readFile(self):
        fp = open('jarmu.txt', 'r', encoding='UTF-8')   # 4. Az App osztályban a readFile() metódust írja át, hogy a jarmu.txt állományt nyissa meg.
        lines = fp.readlines()

        for line in lines[1:]:
            line = line.rstrip()
            (az, rendszam, szin, marka, ar) = line.split(':')
            jarmu = Jarmu(az, rendszam, szin, marka, int(ar))
            self.jarmuLista.append(jarmu)
        fp.close()
    
    def feher(self):
        feherek = 0
        for jarmu in self.jarmuLista:
            if jarmu.szin == 'fehér':   # 6. Az App osztályon belül írja át a feher() nevű metódust, hogy a fehér színű járműveket számolja meg.
                feherek += 1            # 8. A feher() nevű metódus minden fehér járművet kétszer számol egy helyett. Írja át.
        print('Fehérek', feherek)       # 7. A feher() nevű metódusban javítsa ki, hogy fehérek darabszáma előtt a következő szöveg jelenjen meg: „Fehérek: ”

    def olcso(self):
        print('Olcsók:')
        for jarmu in self.jarmuLista:
            if jarmu.ar < 1000000:      # 9. Az olcso() nevű metódus az 1 milliónál drágább járművek adatait írja ki a 1 milliónál olcsóbbak helyett. Javítsa.
                print('{} {}'.format(
                    jarmu.rendszam,
                    jarmu.szin,
                    jarmu.marka         # 10. Az olcso() nevű metódusban írassa ki a járművek márkáját is.
                    ))

    def feherOlcso(self):
        print('Fehér olcsók')
        fp = open('feherOlcso.txt', 'w', encoding='UTF-8')  # 11. A feherOlcso() nevű metódust írja át, hogy a feherOlcso.txt állományt nyissa meg. 12. A feherOlcso() metódus olvasásra nyitja meg az állományt írás helyett. Javítsa
        for jarmu in self.jarmuLista:
            if jarmu.ar < 1000000 and jarmu.szin == 'fehér':    # A feherOlcso() metódus a piros és olcsó járműveket írja ki fehér és olcsó helyett. Javítsa.
                line = jarmu.az + ':' + jarmu.rendszam + ':' + jarmu.szin + ':' + jarmu.marka + ':' + str(jarmu.ar) + '\n'
                print(jarmu.rendszam, jarmu.szin, jarmu.ar)     # 14. A feherOlcso() metódust javítsa, hogy a járművek árait is írja a képernyőre.

                fp.write(line)
        fp.close()  # 15. A feherOlcso() metódusban nincs lezárva a megnyitott fájl. Javítsa.


    def about(self):        # 16. Írjon egy about metódust, ami kiírja a nevét, csoportját és az aktuális dátumot.
        print("Faragó Csaba")
        print("SZOFT I_1_E")
        print("2022-11-17")
        
app = App()             # 2. Hozzon létre egy app nevű objektumot az App osztály példányaként.
app.readFile()          # 17. Az app nevű objektumon hívja meg a readFile(), feher(), olcso(), feherOlcso() és about() metódust, ebben sorrendben.
app.feher()
app.olcso()
app.feherOlcso()
app.about()