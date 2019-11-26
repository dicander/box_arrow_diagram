# Låd- och Pildiagram

Syftet med ett låd- och pildiagram är att förstå kopplingen mellan variablers
namn, typer och värden i datorns minne. Mer specifikt handlar det om de variabler som du skapar själv under programmets gång och deras resa genom funktioner och
metoder som du har skrivit själv.

## Det globala scopet.

Konstanter och funktioner hör hemma i det globala scopet. Programmet blir onödigt
svårläst om varje funktion behövde ta in konstanter och alla sina funktioner som parametrar. Därför existerar ett globalt scope.
Den första låda vi ritar representerar det globala scopet. Det globala scopet innehåller alla namn som är tillgängliga överallt i programmet. Om du skapar en variabel utanför funktioner, klasser och metoder så hamnar den här.
Tyvärr är det globala scopet överanvänt, särskilt i grundkurser. Om alla variabler i ett program är globala så blir programmet mindre överblickbart och svårare att dela upp i små, automatiskt testbara delar. Det är därför projektet har som krav att inte ha några globala variabler.

### Globalt men inte i diagrammet

När du startar ett Pythonprogram så finns redan ett antal variabler i minnet. Exempelvis är konstanten ```__name__``` satt till ```'__main__'``` om programmet körs
som ett script. Dessutom finns Pythons inbyggda funktioner här så att de kan anropas. Det är fel att rita ut dessa i era låd- och pildiagram eftersom de
begraver den fakta vi faktiskt söker: förhållandet mellan de namn som ditt
program skapat och dess värden. Låd- och pildiagram är med andra ord en abstrakt
representation av datorns minne.

## Det lokala scopet - en stackframe

När det procedurella paradigmet föddes så förde det med sig idén om ett lokalt scope. Istället för att ha ett stort blåvalsprogram med mängder av kod och variabler så delar vi in koden i lagom stora funktioner med få, överblickbara
variabler. Varje gång en funktion anropas så skapas en ny låda som kallas
en stackframe. Stackframen är scope för alla parameternamn och lokala variabelnamn. För att skilja dessa lokala scope åt så märker man dem med funktionsanropets plats i koden. Det lokala scopet innehåller parameternamn och namn på lokala variabler som är bundna till värden i datorns minne.

Observera att det är ett lokalt scope per anrop och inte per funktion.

## Datatyper

Datatyper används för att beskriva vilken typ av data som lagras och hur objekt av denna
typ kan skapas, läsas, förändras och kombineras med andra objekt av denna typ eller eventuellt andra typer. Datatypen anges i låd- och pildiagram genom att
typens namn skrivs överst på varje utpekat objekt. Typen utelämnas alltid på
variabelnamn, stackframes och på lådan med det globala scopet.

### Datatypen list

Datatypen list är oftast den första muterbara datatypen som ni möter i kursen. Muterbara datatyper innebär att själva objektet kan förändras oberoende av vad som pekar på den. Förändringsbarhet är bra i vissa lägen, till exempel när vi har en lista med nästan en miljon element och vill lägga till ett extra. Då vore det besvärligt att behöva skapa en ny enorm lista. Tyvärr ger det också upphov till några andra, mer förvirrande situationer som vi täcker härnäst.

## Aliasing

Program behöver hög prestanda och de behöver vara begripliga så att de är lätta att förstå och felsöka. Python låter ibland bli att kopiera objekt där programmerare skulle förvänta sig en kopia. Det gäller även
förändringsbara objekt. Den prestandaökningen
sker på bekostnad av begripligheten eftersom vi ofta hamnar i situationer där
flera namn pekar på samma förändringsbara objekt och det kan leda till att
en variabel förändras via en variabel men att förändringen syns av en annan
variabel.

Exempel där detta används internt av Python syns här:
```
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
```
>>> v = [1000, 4000, 2000, 3000, 5000, 7000, 6000]
>>> fixed = sorted(v)
>>> fixed
[1000, 2000, 3000, 4000, 5000, 6000, 7000]
>>> v
[1000, 4000, 2000, 3000, 5000, 7000, 6000]
>>>
```

Särskilt klurigt blir det när egna funktionsanrop använder ett helt annat parameternamn men ändå förändrar listan:
```
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
```
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
```
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

Ett annat namn för aliasing är sharing.

## Referensräkning

Varje objekt i Python har en referensräkning som anger hur många andra lådor
i diagrammet som pekar på det. Referensräkningen används för att avgöra
när ett objekt inte behövs i minnet längre. Vi gör referensräkning genom att skriva ett tal nere i högra hörnet på varje objekt som ligger utanför stacken.

## Exempel på tentatal
Rita en minnesbild med låd- och pildiagram för programmet nedan då det når denkommenterade raden.
```
left = 1000
right = left
# Den kommenterade raden
```

Inspirerat av ett tentatal: Rita låd- och pil-diagram för hur det kan se ut i minnet då programmet når sista raden i main-funktionen.
```
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
3. Theo Ingelstam, assistent från och med Gruprog19 har förberett [övningar med facit här](https://github.com/Theo-Ing/public-work/tree/master/BoxAndArrowDiagrams).
