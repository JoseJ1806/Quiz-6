from unittest import TestCase

from Arbol_Binario import Tree

class TestArbol(TestCase):
    
    def test_Insertar(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        
    def test_Insertar_Repetido(self):
        bst = Tree()
        bst.Insertar(60)
        bst.Insertar(60)
        
    def test_Eliminar(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.Eliminar(21)
        
    def test_Eliminar_Raiz(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Eliminar(21)

    def test_Eliminar_Izq(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(19)
        bst.Eliminar(21)

    def test_Eliminar_Der(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(53)
        bst.Eliminar(21)

    def test_Eliminar_2Hijos(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.Eliminar(21)

    def test_Eliminar_Nulo(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Eliminar(45)

    #def test_Eliminar_RaizMasNodos(self):
        #bst = Tree()
        #bst.Insertar(21)

    def test_Eliminar_Vacio(self):
        bst = Tree()
        bst.Eliminar(21)

    def test_Eliminar_SinHijo(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.Eliminar(40)

    def test_Eliminar_HijoIzq(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.Eliminar(13)

    def test_Eliminar_HijoDer(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(45)
        bst.Insertar(32)
        bst.Insertar(91)
        bst.Eliminar(45)

    def test_Max(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.BuscarMax(bst.raiz)

    def test_Max_Vacio(self):
        bst = Tree()
        bst.BuscarMax(bst.raiz)

    def test_Min(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.BuscarMin(bst.raiz)

    def test_Min_Vacio(self):
        bst = Tree( )
        bst.BuscarMin(bst.raiz)

    def test_InOrden(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.ImprimirInOrden()

    def test_InOrden_Vacio(self):
        bst = Tree()
        bst.ImprimirInOrden()

    def test_PreOrden(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.ImprimirPreOrden()

    def test_PreOrden_Vacio(self):
        bst = Tree()
        bst.ImprimirPreOrden()

    def test_PostOrden(self):
        bst = Tree()
        bst.Insertar(21)
        bst.Insertar(13)
        bst.Insertar(10)
        bst.Insertar(33)
        bst.Insertar(18)
        bst.Insertar(25)
        bst.Insertar(40)
        bst.ImprimirPostOrden()

    def test_PostOrden_Vacio(self):
        bst = Tree( )
        bst.ImprimirPostOrden()



        

    

    
 
        

