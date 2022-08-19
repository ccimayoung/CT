
choose_data = [0 for _ in range(len(clients))]

choose_ser = [0 for _ in range(len(clients))]


for i in range(len(clients)) :
    for j in range(len(plans ) -1) :
        if (clients[i][0] <= plans[0][0]) : choose_data[i ] =1
        elif (clients[i][0] >= plans[j][0]) and (clients[i][0] < plans[ j +1][0]):
            choose_data[i] = j +2
        else : choose_data[i]=0