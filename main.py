#### Fonctions secondaires
"""Fonctions pour calculer différentes suites de syracuse en utilisant des listes"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """ Illustre les résultats des fonctions avec un graphe """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n

    syracuse_l(15)
    >>> [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    l = [n]
    while n != 1 :
        if n % 2 == 0 :
            n //=  2
        else :
            n = n * 3 + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    
    temps_de_vol(15)
    >>> 17
    temps_de_vol(127)
    >>> 46
    """
    return len(l)-1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    temps_de_vol_en_altitude(15)
    >>> 10
    temps_de_vol_en_altitude(127)
    >>> 23
    """
    first = l[0]
    for i in range(1, len(l)):
        if l[i]<first:
            return i-1
    return -1

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    altitude_maximale(15)
    >>> 160
    altitude_maximale(127)
    >>> 4372
    """
    return max(l)

#### Fonction principale

def main():
    """Affiche la suite de Syracuse et les différentes fonctions associés"""
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(syracuse_l(15))
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
