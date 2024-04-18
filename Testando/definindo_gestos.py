def controller(mao,dedos):
    #Delimita a detecção dos gestos referente a mão direita
    if(mao == "Right"):

        # Adiciona lógica para ligar o LED quando o gesto for detectado
        if(dedos == [0, 1, 0, 0, 0]):
            c.write(b'L')
        if(dedos == [0, 1, 1, 0, 0]):
            c.write(b'A')
        

    #Delimita a detecção dos gestos referente a mão esquerda
    if(mao == "Left"):
        # Adiciona lógica para desligar o LED quando o gesto for detectado
        if (dedos == [0, 1, 0, 0, 0]):
            c.write(b'K')
        if (dedos == [0, 1, 1, 0, 0]):
            c.write(b'B')
  