

class Nodo:
    def __init__(self,valor):
        self.izquierda = None
        self.derecha = None
        self.valor = valor

    def Insertar(self,dato):
        if self.valor == dato:
            return False
        
        elif self.valor > dato:
            if self.izquierda:
                return self.izquierda.Insertar(dato)
            else:
                self.izquierda = Nodo(dato)
        else:
            if self.derecha:
                return self.derecha.Insertar(dato)
            else:
                self.derecha = Nodo(dato)

    def ImprimirInOrden(self):
        if self:
            if self.izquierda:
                self.izquierda.ImprimirInOrden()
            print(str(self.valor))
            if self.derecha:
                self.derecha.ImprimirInOrden()

    def ImprimirPreOrden(self):
        if self:
            print(str(self.valor))
            if self.izquierda:
                self.izquierda.ImprimirPreOrden()
            if self.derecha:
                self.derecha.ImprimirPreOrden()

    def ImprimirPostOrden(self):
        if self:
            if self.izquierda:
                self.izquierda.ImprimirPostOrden()
            if self.derecha:
                self.derecha.ImprimirPostOrden()
            print(str(self.valor))


class Tree:
    
    def __init__(self):
        self.raiz = None

    
    def Insertar(self,dato):
        if self.raiz:
            return self.raiz.Insertar(dato)
        else:
            self.raiz = Nodo(dato)
        
    def Eliminar(self,dato):
        #arbol vacio
        if self.raiz is None:
            return False

        #el dato a borrar esta en la raiz
        elif self.raiz.valor == dato:
            
            if self.raiz.izquierda is None and self.raiz.derecha is None:
                self.raiz = None
                
            elif self.raiz.izquierda and self.raiz.derecha is None:
                self.raiz = self.raiz.izquierda
                
            elif self.raiz.izquierda is None and self.raiz.derecha:
                self.raiz = self.raiz.derecha
                
            elif self.raiz.izquierda and self.raiz.derecha:
                delNodoPadre = self.raiz
                delNodo = self.raiz.derecha
                while delNodo.izquierda:
                    delNodoPadre = delNodo
                    delNodo = delNodo.izquierda
                    
                self.raiz.valor = delNodo.valor
                if delNodo.derecha:
                    if self.raiz.valor > delNodo.valor:
                        delNodoPadre.izquierda = delNodo.derecha
                    elif self.raiz.valor < delNodo.valor:
                        delNodoPadre.derecha = delNodo.derecha
                else:
                    if delNodo.valor < delNodoPadre.valor:
                        delNodoPadre.izquierda = None
                    else:
                        delNodoPadre.derecha = None
        
        padre = None
        nodo = self.raiz

        #Encontrar el nodo a eliminar
        while nodo and nodo.valor != dato:
            padre = nodo
            if dato < nodo.valor:
                nodo = nodo.izquierda
                
            elif dato > nodo.valor:
                nodo = nodo.derecha

        #caso 1: el dato no esta en el arbol
        if nodo is None or nodo.valor != dato:
            print ("El valor no se encuentra en el arbol")

        #caso 2: el nodo a remover no tiene hijos
        elif nodo.izquierda is None and nodo.derecha is None:
            if dato < padre.valor:
                padre.izquierda = None
            else:
                padre.derecha = None

        #caso 3: el nodo a remover solo tiene  un hijo a la izquierda
        elif nodo.izquierda and nodo.derecha is None:
            if dato < padre.valor:
                padre.izquierda = nodo.izquierda
            else:
                padre.derecha = nodo.izquierda
                
        #caso 4: el nodo a remover solo tiene un hijo a la derecha
        elif nodo.izquierda is None and nodo.derecha:
            if dato < padre.valor:
                padre.izquierda = nodo.derecha
            else:
                padre.derecha = nodo.derecha

        #caso 5: el nodo a remover tiene hijos a ambos lados
        else:
            delNodoPadre = nodo
            delNodo = nodo.derecha
            while delNodo.izquierda:
                delNodoPadre = delNodo
                delNodo = delNodo.izquierda

            nodo.valor = delNodo.valor
            if delNodo.derecha:
                if delNodoPadre.valor > delNodo.valor:
                    delNodoPadre.izquierda = delNodo.derecha
                elif delNodoPadre.valor < delNodo.valor:
                    delNodoPadre.derecha = delNodo.derecha
            else:
                if delNodo.valor < delNodoPadre.valor:
                    delNodoPadre.izquierda = None
                else:
                    delNodoPadre.derecha = None
                    
    def BuscarMax(self,temp):
        if self.raiz == None:
            print ("El arbol esta  vacio")
        else:
            maximo = temp.valor
            if temp.izquierda != None:
                MaxIzquierda = self.BuscarMax(temp.izquierda)
                maximo = max(maximo,MaxIzquierda)

            if temp.derecha != None:
                MaxDerecha = self.BuscarMax(temp.derecha)
                maximo = max(maximo,MaxDerecha)
            return maximo

    def BuscarMin(self,temp):
        if self.raiz == None:
            print ("El arbol esta  vacio")
        else:
            minimo = temp.valor
            if temp.izquierda != None:
                MinIzquierda = self.BuscarMin(temp.izquierda)
                minimo = min(minimo,MinIzquierda)

            if temp.derecha != None:
                MinDerecha = self.BuscarMin(temp.derecha)
                minimo = min(minimo,MinDerecha)
            return minimo
               
                    
    def ImprimirInOrden(self):
        if self.raiz is not None:
            print ("InOrden")
            self.raiz.ImprimirInOrden()
   
    def ImprimirPreOrden(self):
        if self.raiz is not None:
            print ("PreOrden")
            self.raiz.ImprimirPreOrden()

    def ImprimirPostOrden(self):
        if self.raiz is not None:
            print ("PostOrden")
            self.raiz.ImprimirPostOrden()








