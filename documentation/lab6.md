# Todo:
* Fix assignment. Function exists its just a question of how assignemt should work when you have both the value and the variable name. (Might have to do with Variabletables. I dont know.)

* Evaluate binary expression. Variables and function exist but not the logic of the evaluation.

* Start building on the empty functions. All functions should be created and contain a basic docstring.

# Understanding via metaphors 

### 🎭 Anekdot 1: Köket på Grand Hotel

**"Tänk dig två kockar på Grand Hotel..."**

- **Kompilatorn** är som kocken som förbereder en festmiddag i förväg. Han läser hela receptet (programmet), förbereder alla rätter och levererar en färdig buffé som gästerna bara behöver ta från. *Snabbt och effektivt, men om någon ingrediens saknas i början kraschar hela processen.*

- **Interpretatorn** är som kocken som jobbar i à la carte-köket. Han läser en rad i receptet i taget, utför den direkt, sedan nästa rad. *Långsammare men mer flexibel - han kan justera under vägen och om fel uppstår vet han exakt var i receptet det hände.*

### 🌳 Anekdot 2: Trädgårdsmästaren och Trädet

**"En trädgårdsmästare ska beskriva ett träd..."**

- **Abstrakta syntaxträdet (AST)** är som när trädgårdsmästaren ritar upp trädets struktur: "rot, stam, tre huvudgrenar, varje gren har kvistar..." Han beskriver **strukturen** utan att bry sig om exakt hur varje löv ser ut.

- **Konkret syntax** är som att beskriva varje enskilt blad i detalj: "det här bladet är 5 cm långt, ljust grönt, med sågtandad kant..."

*I laborationen använder ni Pythons egna listor för att direkt representera AST:et, vilket är som att använda färdiga byggklossar istället för att såga träbitar för hand.*

### 🏗️ Anekdot 3: Byggarbetsplatsen

**"På en byggarbetsplats..."**

- **Lexikalisk analys** är som byggarbetaren som sorterar material: "det här är en tegelsten, det här är en bräda, det här är en spik..." Han skapar meningsfulla enheter från råmaterial.

- **Syntaktisk analys** är som byggledaren som kontrollerar att alla delar passar ihop: "En dörr måste ha en karm - du kan inte sätta en dörr direkt i tomma luften!"

- **Semantisk analys** är som arkitekten som kollar att byggnaden blir stabil: "Den här bärande väggen måste vara av större dimensioner!"

### 🎒 Anekdot 4: Reseledaren och Kartan

**"Tänk dig en reseledare..."**

- **Variabeltabellen** är som reseledarens karta där han markerar var alla gruppmedlemmar befinner sig. När någon rör sig, uppdaterar han kartan. Men istället för att skriva på originalet, ritar han en ny kopia och ändrar på den - **funktionell programmering** i praktiken!