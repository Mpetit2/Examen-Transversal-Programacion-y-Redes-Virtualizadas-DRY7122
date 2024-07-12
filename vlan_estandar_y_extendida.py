num_vlan_estandar=range(1,1005)
num_vlan_extendida=range(1006,4095)

num_vlan=int(input("Ingrese numero de vlan: "))
if num_vlan in num_vlan_estandar:
    print("el numero de vlan",num_vlan,"es una vlan estandar")
elif num_vlan in num_vlan_extendida:
    print("el numero de vlan",num_vlan,"es una vlan extendida")
else :
    print("el numero ",num_vlan,"no corresponde a una vlan")