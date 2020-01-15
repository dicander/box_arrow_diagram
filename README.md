# Låd- och Pildiagram

Syftet med ett låd- och pildiagram är att förstå kopplingen mellan variablers
namn, typer och värden i datorns minne. Mer specifikt handlar det om de variabler som du skapar själv under programmets gång och deras resa genom funktioner och
metoder som du har skrivit själv. Vi delar in digagrammet i 3 delar: Den globala

## Det globala scopet.

Konstanter hör hemma i den globala lådan. Programmet blir onödigt
svårläst om varje funktion behövde ta in konstanter och alla sina funktioner som parametrar. Därför existerar en global låda.
Det är den första vi ritar och den innehåller alla namn som är tillgängliga överallt i programmet. Om du skapar en variabel utanför funktioner, klasser och metoder så hamnar den här.
Tyvärr är den överanvänd, särskilt i grundkurser. Om alla variabler i ett program är globala så blir programmet mindre överblickbart och svårare att dela upp i små, automatiskt testbara delar. Det är därför projektet har som krav att inte ha några globala variabler.

### Globalt men inte i diagrammet
I minnet finns några saker som vi inte har med i låd- och pildiagrammet:

* När du startar ett Pythonprogram så finns redan ett antal variabler i minnet. Exempelvis är konstanten ```__name__``` satt till ```'__main__'``` om programmet körs
som ett script.
* Pythons inbyggda funktioner som abs eller print ligger globalt.
* Funktioner som du definierar i koden ligger globalt.
* Klasser som int, float och list har ett objekt som representerar själva klassen och alla objekt av denna typ pekar på det.

Det är fel att rita ut dessa i era låd- och pildiagram eftersom de
begraver den fakta vi faktiskt söker: förhållandet mellan de namn som ditt
program skapat och dess värden. Ovanstående fakta abstraheras bort. Om du ritar med något av ovanstående så kommer diagrammet att vara på fel abstraktionsnivå.


## Det lokala scopet - en stackframe

När det procedurella paradigmet föddes så förde det med sig idén om ett lokalt scope. Istället för att ha ett stort blåvalsprogram med mängder av kod och variabler så delar vi in koden i lagom stora funktioner med få, överblickbara
variabler. Varje gång en funktion anropas så skapas en ny låda som kallas
en stackframe. Stackframen är scope för alla parameternamn och lokala variabelnamn. För att skilja dessa lokala scope åt så märker man dem med funktionsanropets plats i koden. Det lokala scopet innehåller parameternamn och namn på lokala variabler som är bundna till värden i datorns minne.

Observera att det är en stackframe per anrop och inte per funktion.

Om det utförs ett funktionsanrop inifrån ett funktionsanrop så staplas alla
stackframes ovanpå varandra i en stack (ordet stack används nu i sin engelska
betydelse som är "stapel".)

Exempelkod:
Rita låd- och pildiagram när körningen når den sista printsatsen i varje funktion. Rita också ett diagram då vi har lämnat main på slutet.
```python
def f(v, i):
    v.append(1)
    i += 2
    print("f", locals())


def g(v, i):
    v.append(2)
    i += 3
    f(v, i)
    print("g",locals())


def main():
    v = []
    i = 0
    g(v, i)
    print("main", locals())


if __name__ == '__main__':
    main()
```
[Facit](stackfacit.md)

Om du anropar en metod på en klass så läggs metodanropet på stacken, precis som med funktioner. Self pekar på objektet vars metod har anropats. Exempelkod följer. Rita ett diagram då programmet når den kommenterade raden.
```python
class A:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1
        # Diagram här innan vi återvänder


def main():
    a = A()
    a.inc()


if __name__ == '__main__':
    main()
```
[Facit](objektfacit.md)

Exempelfråga:
Rita ett låd- och pildiagram då koden nedan når den kommenterade raden:
```python
left = 1000
right = 2000
middle = left
# Den kommenterade raden
right = left
left = middle
```
[Facit](middlefacit.md)

Kuggfråga:
Rita låd- och pildiagram då programmet når den kommenterade raden.

```python
def f(n):
    v = []
    v.append(n)


# Den kommenterade raden
```
[Facit](kuggfraga.md)

Rita ett låd- och pildiagram då programmet når den kommenterade raden _för andra gången_:
```python
def f(n):
    v = []
    v.append(n)
    # Den kommenterade raden
    return


f(1)
f(2)
```
[Facit](andragangen.md)
## Datatyper

Datatyper används för att beskriva vilken typ av data som lagras och hur objekt av denna
typ kan skapas, läsas, förändras och kombineras med andra objekt av denna typ eller eventuellt andra typer. Datatypen anges i låd- och pildiagram genom att
typens namn skrivs överst på varje utpekat objekt. Typen utelämnas alltid på
variabelnamn, stackframes och på lådan med det globala scopet.

### Datatypen list

Datatypen list är oftast den första muterbara datatypen som ni möter i kursen. Muterbara datatyper innebär att själva objektet kan förändras oberoende av vad som pekar på den. Förändringsbarhet är bra i vissa lägen, till exempel när vi har en lista med nästan en miljon element och vill lägga till ett extra. Då vore det besvärligt att behöva skapa en ny enorm lista. Tyvärr ger det också upphov till några andra, mer förvirrande situationer som vi täcker nedan.

När vi adderar två listor med varandra så skapas en ny lista. Den nya listan pekar ut samma objekt som de gamla listorna pekade ut. Den nya listan (v3 i exemplet nedan) är alltså en grund kopia.
```Python
>>> v1 = [1, 2]
>>> v2 = [3, 4, 5]
>>> v3 = v1 + v2
>>> v1, v2, v3
([1, 2], [3, 4, 5], [1, 2, 3, 4, 5])
>>>
```
![Addition av listor](listaddition.png)


När vi slice:ar en lista
```Python
>>> v1 = [1, 2, 3, 4]
>>> v2 = v1[:2]
>>> v1, v2
([1, 2, 3, 4], [1, 2])
>>>
```
så skapas en grund kopia av (delar av) listan. Den nya listan v2 pekar på samma objekt som den gamla listan. Detta gäller även när hela listan kopieras.

![Slicead lista](sliced1.png)

```Python
>>> v1 = [1, 2]
>>> v2 = v1[:]
>>> v1, v2
([1, 2], [1, 2])
>>> v2[1] = 3
>>> v1, v2
([1, 2], [1, 3])
>>>
```

Fler exempel finns på [Pythons hemsida](https://docs.python.org/3/tutorial/datastructures.html).

## Aliasing

Program behöver hög prestanda och de behöver vara begripliga så att de är lätta att förstå och felsöka. Python låter ibland bli att kopiera objekt där programmerare skulle förvänta sig en kopia. Det gäller även
förändringsbara objekt. Den prestandaökningen
sker på bekostnad av begripligheten eftersom vi ofta hamnar i situationer där
flera namn pekar på samma förändringsbara objekt och det kan leda till att
en variabel förändras via en variabel men att förändringen syns av en annan
variabel.

Exempel där detta används internt av Python syns här:
```python
>>> import random
>>> v = [1, 2, 3, 4, 5]
>>> random.shuffle(v)
>>> v
[3, 5, 2, 1, 4]
>>>
```
I detta exempel skickades listan som v är bunden till med till random.shuffle
som kastade om värdena direkt i listan (in place).

Ett exempel på motsatsen är pythons inbyggda funktion sorted som returnerar
en grund kopia av en sorterad lista:
```python
>>> v = [1000, 4000, 2000, 3000, 5000, 7000, 6000]
>>> fixed = sorted(v)
>>> fixed
[1000, 2000, 3000, 4000, 5000, 6000, 7000]
>>> v
[1000, 4000, 2000, 3000, 5000, 7000, 6000]
>>>
```

Särskilt klurigt blir det när egna funktionsanrop använder ett helt annat parameternamn men ändå förändrar listan:
```python
import random


def f(victims):
    while victims:
        target = random.choice(victims)
        victims.remove(target)
        print(target)


v = "1000 2000 3000 4000 5000".split()
print("before", v)
f(v)
print("after", v)
```
Om vi kör detta kodexempel så är ett möjligt resultat:
```python
$ python3 aliasing.py
before ['1000', '2000', '3000', '4000', '5000']
1000
4000
2000
3000
5000
after []
$
```

### Tentatal från 2018

Vad skriver följande Python3-program ut?
```python
def mystery(v, n):
    n = n + 1
    v[1] = n


def main():
    v = [1, 2]
    n = 4
    mystery(v, n)
    print(v, n)


main()
```
Tillägg från tentan: Rita ett låd- och pildiagram för hur det ser ut innan mystery returnerar.
[Facit](tentatal2018.md)

Ett annat namn för aliasing är sharing.


## Referensräkning

Varje objekt i Python har en referensräkning som anger hur många andra lådor
i diagrammet som pekar på det. Referensräkningen används för att avgöra
när ett objekt inte behövs i minnet längre. Vi gör referensräkning genom att skriva ett tal nere i högra hörnet på varje objekt som ligger utanför stacken.

## Exempel på tentatal
Rita en minnesbild med låd- och pildiagram för programmet nedan då det når denkommenterade raden.
```python
left = 1000
right = left
# Den kommenterade raden
```

Inspirerat av ett tentatal: Rita låd- och pil-diagram för hur det kan se ut i minnet då programmet når sista raden i main-funktionen.
```python
class Node:
    def __init__(self, value, following):
        self.value = value
        self.following = following


def print_values(first):
    temp = first
    while temp:
        print(temp.value)
        temp = temp.following


def create_list(size):
    first = Node(size, None)
    for i in range(size-1, 0, -1):
        first = Node(i, first)
    return first


def destroy_element(first, index):
    """returns the first element where index has been destroyed"""
    if index == 0:
        return first.following
    answer = first #we will change this variable
    for i in range(index-1):
        first = first.following
    following_following = first.following.following
    first.following = following_following
    return answer


def main():
    first = create_list(4)
    print_values(first)
    first = destroy_element(first, 2)
    print_values(first)


if __name__ == '__main__':
    main()
```

[Facit](facit.md)

1. Fler exempel finns i [exempeltentan](https://github.com/dicander/training_exam).
2. Den [första tentan på det nya formatet](https://gits-15.sys.kth.se/dicander/gruprog_tenta_2019-10-18)
har ännu fler exempel.
3. [Fx-kompletteringen](https://gits-15.sys.kth.se/dicander/Fxkomplettering20191202) har fler exempel.
4. [Omtentan](https://gits-15.sys.kth.se/dicander/gruprogtenta2019-12-17) med facit.
5. Theo Ingelstam har förberett [övningar med facit här](https://github.com/Theo-Ing/public-work/tree/master/BoxAndArrowDiagrams).
