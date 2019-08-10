import pygame
a=int(input("Selecione 1 para Maneva ou 2 para full Figthers:  "))
lista=("1 - Maneva Cabelo Pixaim\n2 - Maneva Daquele Jeito \n3 - Maneva Lembranças \n4 - Maneva Luz que me traz paz \n5 - Maneva Meu Pai é Rastafari \n6 - Maneva Pisando Descalço \n7 - Maneva Saudades do Tempo")
rlista=["Maneva Cabelo Pixaim.mp3","Maneva Daquele Jeito.mp3","Maneva Lembranças.mp3","Maneva Luz que me traz paz.mp3","Maneva Meu Pai é Rastafari.mp3","Maneva Pisando Descalço.mp3","Maneva Saudades do Tempo.mp3"]
if a==1:
    print(lista)
    b=int(input("Digite o número da música que você quer tocar: "))
    c=rlista[(b-1)]
    pygame.mixer.init()
    pygame.mixer.music.load(c)
    pygame.mixer.music.play()
    pygame.event.wait()
    print('Acabou')