import pandas as pd
import gmplot 
from Adicional import adicional

df=pd.read_csv('C:\Programacion_Visual\Datos.py\calles_de_medellin_con_acoso.csv',sep=';')
df_Filtrado = df.fillna({"harassmentRisk":df['harassmentRisk'].mean()})


adicional.bienvenida()
grafo={}
grafo=adicional.crear_Grafo(df_Filtrado,grafo)

print("Digite la coordinada inicial, sin los parentesis:")
nodo_Inicial="("+str(input())+")"
print("Digite la coordinada final, sin los parentesis:")
nodo_FInal="("+str(input())+")"
temp=""
continuar="si"

while continuar=="si":    
    adicional.información()
    n=int(input())
    if n==1:
        grafo_Temp={}
        #creo un grafo aparte del cuya en la que la tupla se cambia por el promedio de riesgo y longitud
        #lo hize así pa cuando toque calcular los 3 caminos distintos 
        for clave in grafo:
            grafo_Temp[clave]=grafo[clave]
            for valor in grafo[clave]:
                grafo_Temp[clave][valor]=grafo[clave][valor][0]
        temp=adicional.dijkstra(grafo_Temp,nodo_Inicial,nodo_FInal)
    elif n==2:
        grafo_Temp={}
        #creo un grafo aparte del cuya en la que la tupla se cambia por el promedio de riesgo y longitud
        #lo hize así pa cuando toque calcular los 3 caminos distintos 
        for clave in grafo:
            grafo_Temp[clave]=grafo[clave]
            for valor in grafo[clave]:
                grafo_Temp[clave][valor]=grafo[clave][valor][1]
        temp=adicional.dijkstra(grafo_Temp,nodo_Inicial,nodo_FInal)
    elif n==3:
        grafo_Temp={}
        #creo un grafo aparte del cuya en la que la tupla se cambia por el promedio de riesgo y longitud
        #lo hize así pa cuando toque calcular los 3 caminos distintos 
        for clave in grafo:
            grafo_Temp[clave]=grafo[clave]
            for valor in grafo[clave]:
                grafo_Temp[clave][valor]=grafo[clave][valor][2]
        temp=adicional.dijkstra(grafo_Temp,nodo_Inicial,nodo_FInal)
    else:
        print("Por favor digite una opción valida")
    
    latitude_list = []
    longitude_list = [] 
    

    for i in range (0,len(temp)):
        valores=str(temp[i])
        longitude_list.append(float(valores[1:valores.find(",")]))
        latitude_list.append(float(valores[valores.find(",")+2:len(valores)-1]))
 
    #esto genera un mapa una pagina en google maps con los puntos   
    gmap3 = gmplot.GoogleMapPlotter(latitude_list[0],longitude_list[0], 40) 
    gmap3.scatter( latitude_list, longitude_list, '# FF0000', size = 40, marker = False )   
    gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width = 2.5) 
    gmap3.draw("C:\Programacion_Visual\Datos.py\mapaConPuntos.html")#en este punto se genera el html en la posición que se indique
    
    print("Si desea graficar otra ruta escriba si a continuación: ")
    continuar=str(input())
