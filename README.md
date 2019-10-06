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

Ett annat namn för aliasing är sharing.

## Referensräkning

Varje objekt i Python har en referensräkning som anger hur många andra lådor
i diagrammet som pekar på det. Referensräkningen används för att avgöra
när ett objekt inte behövs i minnet längre. Vi gör referensräkning genom att skriva ett tal nere i högra hörnet på varje objekt som ligger utanför stacken.
