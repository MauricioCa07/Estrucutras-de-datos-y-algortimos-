class adicional:
    
    def bienvenida():
        print("********************************************************\n\n Bienvenid@ a nuestro programa \n\n ********************************************************")
      
        
    def crear_Grafo(df,i):
        grafo={}
        df_Filtrado = df.fillna({"harassmentRisk":df['harassmentRisk'].mean()})
        
        for linea in df_Filtrado.index:
            temp=(((df_Filtrado["harassmentRisk"][linea]*100)+df_Filtrado["length"][linea])/2,df_Filtrado["length"][linea],df_Filtrado["harassmentRisk"][linea])
            if df_Filtrado["origin"][linea] not in grafo:
                grafo[df_Filtrado["origin"][linea]]={df_Filtrado["destination"][linea]:temp[i]}
            else:
                grafo[df_Filtrado["origin"][linea]][df_Filtrado["destination"][linea]]=temp[i]
            if  df_Filtrado["oneway"][linea] == True: 
                if df_Filtrado["destination"][linea] not in grafo:
                    grafo[df_Filtrado["destination"][linea]]={df_Filtrado["origin"][linea]:temp[i]}
                else:
                    grafo[df_Filtrado["destination"][linea]][df_Filtrado["origin"][linea]]=temp[i]    
        return  grafo
    
    
    def dijkstra(grafo,inicial,final):
        camino_mas_Corto={}
        camino_Recorrido={}
        nodos_Nousados=grafo
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
                elif camino_mas_Corto[node] < camino_mas_Corto[distancia_Minima]:
                    distancia_Minima=node
            opciones_Caminos=grafo[distancia_Minima].items()
        
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
                print("La ruta no es valida")
                break   
        ruta.insert(0,inicial)
        if camino_mas_Corto[final] != infinito:
            print(camino_mas_Corto[final]," metros")
            return  ruta
      
