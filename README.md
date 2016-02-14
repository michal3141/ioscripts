# ioscripts
Scripts for IO 

Jak stworzyć jara ?

Z poziomu katalogu scala-mas:
$ sbt assembly

Wynikiem powinien być m.in. jar examples-assembly-1.0.jar, którego później odpalam

Krótki opis skryptów:

* run_emas.py -
  Skrypt używany przeze mnie do generowania wyników (w przypadku EMASa).
  
  Uruchomienie:

  $ python run_emas.py
  
  Wymagania:

  examples-assembly-1.0.jar w katalogu skryptu run_emas.py

  Podstawowe parametry skryptu:

  * JAVA_HOME - tutaj trzeba ustawić odpowiedni katalog z Java
  * DIVS_COUNT, alphas, deltas - tutaj definiujemy dla jakich alpha oraz delta ma być odpalany program
  * ITERS_COUNT - liczba iteracji
  * RUNS_COUNT- liczba uruchomień (ile razy program bedzie odpalalany z tymi samymi alpha i delta)
  * NUM_OF_PROCESSES - maksymalna liczba procesów, które w danym momencie moga byc odpalone (na 24 core'owej maszynie ok. 8 bylo ok)

* run.py - 
  Skrypt używany przeze mnie do generowania wynikow w przypadku tej pierwszej appki Java'ovej

  Dziala podobnie jak run_emas.py
  
* graph.py -
  Skrypt używany do rysowania tych wykresów dwu-wymiarowych z procentem kooperacji

  Uruchomienie:
  
  $ python graph.py
  
  Wymagania:
  
  Katalog out z plikami tekstowymi zawierajacymi wyniki odnosnie liczby stanów kooperacji dla poszczególnych uruchomień programu
  
  Zależnosci:
  
  Wymaga numpy, scipy, matplotlib
