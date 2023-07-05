from Task1_jkan67 import *

def dijsktra2(graph,initial):
    Discovered=MinHeap(6105)
    Finalised=[0]*6105
    Vert_parent=[-1]*6105
    Discovered.insert((initial,0))

    while Discovered.currentSize>0:
        current=Discovered.delMin()
        for i in range(len(graph[current[0]])):
            connected_node=graph[current[0]][i]
            if Discovered.vertices[connected_node[0]]==-2:
                Discovered.insert((connected_node[0],connected_node[1]+current[1]))
                Vert_parent[connected_node[0]]= current[0]

            elif Discovered.vertices[connected_node[0]]!=-1 and Discovered.heapList[Discovered.vertices[connected_node[0]]][1]>connected_node[1]+current[1]:
                Discovered.replace(Discovered.vertices[connected_node[0]],(connected_node[0], connected_node[1] + current[1]))
                Vert_parent[connected_node[1]] = current[0]

        Finalised[current[0]]=current
        Discovered.vertices[current[0]] = -1

    return Finalised,Vert_parent

def create_customer(Cust_doc):
    Customer_list= []
    for customer in Cust_doc:
        a = customer.split(' ')
        Customer_list.append(int(a[0]))
    return Customer_list

def lin_search(initial,initial_span,init_vert_par,final,final_span,final_vert_par,Customers):
    min_dist=float('inf')
    lucky_customer=0

    for c in Customers:
        if min_dist>initial_span[c][1]+final_span[c][1]:
            min_dist=initial_span[c][1]+final_span[c][1]
            lucky_customer=c

    if min_dist==0:
        path1=''
        path2=str(initial)+' (C)'

    else:
        path1=dijsktra(Graph,initial,lucky_customer)[0]
        path2=' (C) --> '+dijsktra(Graph,lucky_customer,final)[0]

    return path1+path2,min_dist

def print_task2(info):
    print('Minimum Detour Path and Distance: ')
    print(info[0])
    print('Total route distance: ' + str(info[1]) + '\n')

C= open('customers.txt')
Customers=create_customer(C)
