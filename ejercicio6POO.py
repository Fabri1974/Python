class Cuenta(object):
    def __init__(self,titular, saldo):
        self.titular=titular
        self.saldo=saldo
    def saldo(self):
        return self.saldo
    def setSaldo(self,nuevoSaldo):
        self.saldo=nuevoSaldo    
    def MostrarDatos(self):
        print (self.titular)
        print (self.saldo)
    def Depositar(self,deposito):
        nuevoSaldo=self.saldo+deposito
        Cuenta.setSaldo(self,nuevoSaldo)
        return  print(nuevoSaldo)
    def Retiro(self,retiro):
        saldo_actual=self.saldo+retiro
        Cuenta.setSaldo(self,saldo_actual)
        return print("Tu Saldo actual es ahora de:",saldo_actual)
op=6
cuenta1=Cuenta("Fabricio",10000)
while op==6:

       
       cuenta1.MostrarDatos()
       dep=int(input("Ingrese el monto a depositar"))
       if dep> 0:
             cuenta1.Depositar(dep)
       else:
             cuenta1.Retiro(dep)
       cuenta1.MostrarDatos()
       op=input("Desea realizar otra operacion Si/No")
       if op=="Si":
            op=6
       else:
            op=5  

