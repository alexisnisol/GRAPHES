import requetes as req
import networkx as nx

def jeu_donnees():
    G = req.json_vers_nx("data_100.txt")
    return G

def test_collab_communs():
    G = jeu_donnees()
    assert req.collaborateurs_communs(G, "", "") is None
    assert req.collaborateurs_communs(G, "Marisa Berenson", "Mel Gibson") == {'Bud Cort', 'Rosanna Arquette'}

def test_collab_proches():
    G = jeu_donnees()
    assert req.collaborateurs_proches(G, "", 50) is None
    assert req.collaborateurs_proches(G, "James Woods", 1) == {'Randi Brooks', 'Barry Switzer', 'Warren Moon', 'Charlton Heston', 'Clifton Davis', 'Lela Rochon', 'Lauren Holly', 'Ann-Margret|Ann-Margret Olsson', 'Jan McGill', 'Oliver Stone', 'Vicki Wauchope', 'John C. McGinley', 'Dennis Quaid', 'Charles Durning', 'Steven Lambert', 'Lawrence Taylor', 'Jim Brown', 'Dick Butkus', 'Wilt Chamberlain', 'Raymond J. Barry', 'Annie McEnroe', 'James Woods', 'Aaron Eckhart', 'Christopher Wynne', 'Bill Bellamy', 'Jamie Foxx', 'Y. A. Tittle', 'Johnny Unitas', 'Lesley Ann Warren', 'Dennis Cleveland Stewart|Dennis Stewart', 'Ann-Margret', 'Charles Haid', 'Terrell Owens', 'John Petievich', 'LL Cool J', 'Elizabeth Berkley', 'Melinda Lynch', 'Cameron Diaz', 'Matthew Modine', 'Ricky Watters', 'Al Pacino', 'Irving Fryar'}
    assert req.collaborateurs_proches(G, "James Woods", 0) is None

def test_est_proche():
    G = jeu_donnees()
    assert req.est_proche(G, "James Woods", "Bruno Kirby", 4)
    assert req.est_proche(G, "", "", 1) is None
    assert req.est_proche(G, "James Woods", "Bruno Kirby", 0) is None

def test_dist_naive():
    G = jeu_donnees()
    assert req.distance_naive(G, "", "") is None
    assert req.distance_naive(G, "James Woods", "Roy Jones Jr") == 2
    # pour si les acteurs ne sont pas accessibles
    G.add_node("inaccessible")
    assert req.distance_naive(G, "inaccessible", "James Woods") == -1

def test_distance():
    G = jeu_donnees()
    assert req.distance(G, "", "") is None
    assert req.distance(G, "James Woods", "Roy Jones Jr") == 2
    # pour si les acteurs ne sont pas accessibles
    G.add_node("inaccessible")
    assert req.distance(G, "inaccessible", "James Woods") == -1

def test_centralite():
    G9 = nx.Graph()
    G9.add_edges_from([(1,4),(4,2),(4,3),(4,5),(5,6),(2,7),(6,8),(8,9),(7,10),(9,4)])
    assert req.centralite(G9, 4) == 3
    assert req.centralite(G9, 10) == 5
    assert req.centralite(G9, 564) is None

def test_centre_hollywood():
    G9 = nx.Graph()
    G9.add_edges_from([(1,4),(4,2),(4,3),(4,5),(5,6),(2,7),(6,8),(8,9),(7,10),(9,4)])
    assert req.centre_hollywood(G9) is None

def test_eloignement():
    G9 = nx.Graph()
    G9.add_edges_from([(1,4),(4,2),(4,3),(4,5),(5,6),(2,7),(6,8),(8,9),(7,10),(9,4)])
    assert req.eloignement_max(G9) == 6 or req.eloignement_max(G9) == 10 or req.eloignement_max(G9) == 8
