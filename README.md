# network-delay
Skrypt do sprawdzania opóznienia internetowego.

Cel: Automatyczne sprawdzenie opóźnienia pomiędzy serwerami.

Opis: Skrypt ma robić coś podobnego co polecenie ping, jednak ma się to dziać automatycznie w określonych godzinach i raportoawć do pliku. Na podstawie tego można stwierdzić kiedy (o ile) występuje wąskie gardło (bottleneck) oraz czy łącze jest stabilne. W ten sposób można sprawdzić czy potencjalny problem jest regularny.

Informacje dodatkowe: Należy go dodać do crontaba w Linuxie lub w Harmonogramie Zadań, aby wykonywał się samoistnie
W cel.txt można wpisać sobie adres który ma sie przeskanować i zapisuje się do logów
