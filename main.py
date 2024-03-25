# los diferentes "niveles" de nodos se representan con una lista 2d
# donde los items de la lista 0 no tienen dependencias los de la lista
# 1 tienen como dependencia a alguno de la 0
# aquellos nodos que no tengan dependientes se conectan al final




# se crea el nodo inicio en (0, 0)
# le sumo (3 * radio) a x
# la distancia vertical entre los nodos es de (2 * radio), desde el centro (4 * radio)

# recorro la linsta de tareas
# se acumunlan en una lista y se hacen pop
# todas las que no tengan dedepndientes
# al llegar al fin de la lista se se calcula y:
#                                               siendo n el numero de nodos en la lista
#                                               el primero va en y + ( (n - 1) * 2 * r ) y cada centro va en ( y + (4 * radio) )
# al dibujar un nodo se busca su dependencia y se conecta a él
# si no tiene, se conecta al nodo inicio
# aquellos nodos que no tengan dependientes son conectados al final
