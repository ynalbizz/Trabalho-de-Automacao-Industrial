import AuxiliarLib as aux



def OneHandcontroller(mao,dedos,dist_entreIeP,maoPos,area):

    #Delimita a detecção dos gestos referente a mão direita
    if(mao == "Right"):
        # Adiciona lógica para ligar o LED quando o gesto for detectado
        if(dedos == [0, 1, 0, 0, 0]):            
            print("Rg1")
            return

        if(dedos == [0, 1, 1, 0, 0]):
            #c.write(b'A')
            print("Rg2")
            return
        
        return
       
   
    # if aux.HandLocationVerifiying(maoPos,area[1].Infos()):
    #     print("chegou")
          
      

    #Delimita a detecção dos gestos referente a mão esquerda
    if(mao == "Left"):
        # Adiciona lógica para desligar o LED quando o gesto for detectado
        if (dedos == [0, 1, 0, 0, 0]):
            #c.write(b'K')
            print("Lg1")
            return

        if (dedos == [0, 1, 1, 0, 0]):
            #c.write(b'B')
            print("Lg2")
            return
        
        return

def TwoHandcontroller(mao,dedos,dist_entreIeP,dist_entreMaos,maoPos,area):
    #Lê os Gestos da Nova mão
    OneHandcontroller(mao,dedos,dist_entreIeP,maoPos,area)

    #Adiciona novos gestos Exclusivos para Duas 
    if(dist_entreMaos >= 100):
      True

#pega esaa