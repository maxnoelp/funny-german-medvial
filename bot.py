import random

part2 = [
    "hat keinen einzigen Drachen besiegt,",
    "riecht wie ein verfaulter Käse,",
    "hat das Turnier verloren,",
    "zittert vor Angst,",
    "schläft ständig ein,",
    "verliert ständig sein Schwert,",
    "redet ohne Unterlass,",
    "reitet auf einem klapprigen Gaul,",
    "hat keine Kondition,",
    "kommt immer zu spät,",
]
part3 = [
    "wurde sogar von einem Schaf vertrieben.",
    "konnte nicht einmal eine Maus fangen.",
    "weil sie über ihren eigenen Rock gestolpert ist.",
    "wenn er nur ein Eichhörnchen sieht.",
    "selbst während der königlichen Audienz.",
    "weil es ihm immer aus den Händen rutscht.",
    "aber niemand hört ihr zu.",
    "der beim ersten Windstoß umfällt.",
    "und wird immer zuletzt gewählt.",
    "selbst zur eigenen Rettung.",
]
part4 = [
    "So peinlich.",
    "Einfach erbärmlich.",
    "Zum Lachen!",
    "Arme Seele.",
    "Was für eine Schande.",
    "So kläglich.",
    "So wahr.",
    "So traurig.",
    "Ein Trauerspiel.",
    "Einfach unbegreiflich.",
]

best_words = [part2, part3, part4]
# print(best_words)

sentence = []
print("Schreib einen Namen:")
name = input()

if name != "":
    for part in best_words:
        x = random.randint(0, len(part) - 1)
        sentence.append(part[x])
elif name == "":
    print("Bitte Name eintragen!!")

print(name + ", " + " ".join(sentence))
