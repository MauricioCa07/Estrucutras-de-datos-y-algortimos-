import pandas as pd
import gmplot 

df=pd.read_csv('C:\Programacion_Visual\Datos.py\calles_de_medellin_con_acoso.csv',sep=';')
df_Filtrado = df.fillna({"harassmentRisk":df['harassmentRisk'].mean()})

grafo={}

#con esto creo el grafo, es un una tupla dentro de un diccionario anidado
for linea in df_Filtrado.index:
    #Esta es una tupla que contiene el promedio de riego y longitd, así como sus valores por aparte será util pa calcular 3 rutas
    temp=((df_Filtrado["harassmentRisk"][linea]+df_Filtrado["length"][linea])/2,df_Filtrado["length"][linea],df_Filtrado["harassmentRisk"])
    if df_Filtrado["origin"][linea] not in grafo:
        grafo[df_Filtrado["origin"][linea]]={df_Filtrado["destination"][linea]:temp}
    else:
        grafo[df_Filtrado["origin"][linea]][df_Filtrado["destination"][linea]]=temp
        
    if  df_Filtrado["oneway"][linea] == True: 
      if df_Filtrado["destination"][linea] not in grafo:
        grafo[df_Filtrado["destination"][linea]]={df_Filtrado["origin"][linea]:temp}
      else:
        grafo[df_Filtrado["destination"][linea]][df_Filtrado["origin"][linea]]=temp
        
        
grafo_Temp={}

#creo un grafo aparte del cuya en la que la tupla se cambia por el promedio de riesgo y longitud
#lo hize así pa cuando toque calcular los 3 caminos distintos 
for clave in grafo:
    grafo_Temp[clave]=grafo[clave]
    for valor in grafo[clave]:
            grafo_Temp[clave][valor]=grafo[clave][valor][0]
 
def dijkstra(inicial,final):
    camino_mas_Corto={}
    camino_Recorrido={}
    nodos_Nousados=grafo_Temp
    infinito=9999999
    ruta=[] 
    
    for node in nodos_Nousados:
        camino_mas_Corto[node]=infinito
    camino_mas_Corto[inicial]=0

    while nodos_Nousados:
        distancia_Minima=None
        for node in nodos_Nousados:
            if distancia_Minima is None:
                distancia_Minima=node
            if camino_mas_Corto[node] < camino_mas_Corto[distancia_Minima]:
                distancia_Minima=node
        opciones_Caminos=grafo_Temp[distancia_Minima].items()
    
        for tempNodo, indice in opciones_Caminos:
            if indice + camino_mas_Corto[distancia_Minima] < camino_mas_Corto[tempNodo]:
                camino_mas_Corto[tempNodo]=indice+camino_mas_Corto[distancia_Minima]
                camino_Recorrido[tempNodo]=distancia_Minima
        nodos_Nousados.pop(distancia_Minima)   
                  
    nodo_actual=final
    while nodo_actual != inicial:
        try:
            ruta.insert(0,nodo_actual)
            nodo_actual=camino_Recorrido[nodo_actual]
        except KeyError:
            print("La ruta no no es valida")
            break   
    ruta.insert(0,inicial)
    if camino_mas_Corto[final] != infinito:
        return  ruta
 


temp=dijkstra('(-75.5641291, 6.2265514)','(-75.7161351, 6.3424055)')

latitude_list = []
longitude_list = [] 
    
for i in range (0,len(temp)):
    valores=str(temp[i])
    longitude_list.append(float(valores[1:valores.find(",")]))
    latitude_list.append(float(valores[valores.find(",")+2:len(valores)-1]))
 
#esto genera un mapa una pagina en google maps con los puntos   
gmap3 = gmplot.GoogleMapPlotter(latitude_list[0],longitude_list[0], 13) 
gmap3.scatter( latitude_list, longitude_list, '# FF0000', size = 40, marker = False ) 
gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width = 2.5) 
gmap3.draw( "C:\Programacion_Visual\Datos.py\map13.html" )
