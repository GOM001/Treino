dia, mes, ano=input('qual a sua data de nacimento? (dd/mm/aaaa) ').split('/')
meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio","Junho","Julho","Agosto","Sentembro","Outubro","Novembro","Dezembro"]
print("Sua data de Nascimento em extenso é ",dia," de ",meses[(int(mes))-1]," de ",ano)
