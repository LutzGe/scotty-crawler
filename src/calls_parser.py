from bs4 import BeautifulSoup

from time import time

class CallsParser:

    def __init__(self, html, save=True):
        self.soup = BeautifulSoup(html, 'html.parser')

        if save:
            self.save_html()
    
    
    def get_total_calls(self) -> str: 
        """'[1..30] de 508' => 508"""
        upper = self.soup.select("div.mGridNavigation")
        total = upper[0].select("div.mGridNavigatorRange")
        # apenas o texto
        total = total[0].string

        slicer = '] de '
        total = total[total.index(slicer) + len(slicer):]

        return int(total)

    def get_list_range(self) -> list:
        """'[1..30] de 508' => ['1', '30']"""
        upper = self.soup.select("div.mGridNavigation")
        total = upper[0].select("div.mGridNavigatorRange")
        # apenas o texto
        total = total[0].string
        total = total[ total.index('[') + 1 : total.index(']') ].split('..')

        return total
    
    def get_columns(self) -> list:
        parent = self.soup.select("a.order")
        columns = [column.string for column in parent]


        return columns

    def get_calls(self) -> list:
        pass


    def save_html(self, filename='parsed') -> bool:
        with open('dist/' + filename + str(int(time())) + '.html', 'w') as out:
            out.write(self.soup.prettify())

        return True

