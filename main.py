from datas_br import DatasBr
from TelefonesBr import TelefonesBr
from cpf import Cpf

#telefone
telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

#cpf validado
cpf_um = Cpf("15316264754")
print(cpf_um)

#datas/horarios
hoje = DatasBr()
print(hoje.tempo_cadastro())