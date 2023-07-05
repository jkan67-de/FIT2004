from Task2_jkan67 import *

if __name__=='__main__':
    inital=input('Enter source vertex: ')
    final=input('Enter target vertex: ')

    print_task1(dijsktra(Graph, initial, final))

    initial_span, init_vert_par = dijsktra2(Graph, initial)
    final_span, final_vert_par = dijsktra2(Graph, final)
    print_task2(lin_search(initial, initial_span, init_vert_par, final, final_span, final_vert_par, Customers))