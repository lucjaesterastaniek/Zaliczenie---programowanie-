#2. Korzystając ze słownika, utwórz funkcję, która będzie zwracać tłumaczenia nazw miesięcy z języka polskiego na angielski.
def miesiace_angielski(miesiac):
    polski_na_angielski = {"styczen":"january","luty":"february","marzec":"march","kwiecien":"april","maj":"may","czerwiec":"june","lipiec":"july","sierpien":"august","wrzesien":"september","pazdziernik":"october","listopad":"november","grudzien":"december"}
    return polski_na_angielski[miesiac]