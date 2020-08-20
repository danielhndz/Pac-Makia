def list_ad(tablero_juego):
    listAd = {}
    for i in range (len(tablero_juego)):
        for j in range (len(tablero_juego[i])):
            temp = []
            if i-1 >= 0:
                temp.append((i-1,j))
            if j-1 >= 0:
                temp.append((i,j-1))
            if i+1 < len(tablero_juego):
                temp.append((i+1,j))
            if j+1 < len(tablero_juego[i]):
                temp.append((i,j+1))
            listAd [(i,j)] = temp
    return listAd
