def tokenize_test(ls):
    """Tokeniza uma lista de sentenças e printa a primeira palavra dessa sentença 
    tokenizada
    
    :param ls: lista de sentenças
    :type ls: list    
    
    """
    for sentence in ls:
        temp_text = sentence.split()
        print(temp_text[0])

DEBUG = True
if __name__ == "__main__":
    if DEBUG:
        ls_text = ["FEA.Dev é uma entidade estudantil que tem por objetivo unir o mundo dos negócios ...",
                   "Exemplo1: Teste",
                   "Exemplo 2: FEA Dev"]
        tokenize_test(ls = ls_text)
    