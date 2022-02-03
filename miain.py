try: 
    
    path = input(r'Digite o caminho da imagem: ') 
      
    
    key = int(input('Digite a chave para criptografar a imagem : ')) 
      
    
    
    print('O caminho do arquivo: ', path) 
    print('Chave para criptografia : ', key) 
      
    
    fin = open(path, 'rb') 
      
    
    image = fin.read() 
    fin.close() 
      
    
    
    image = bytearray(image) 
  
    
    for index, values in enumerate(image): 
        image[index] = values ^ key 
  
    
    fin = open(path, 'wb') 
      
    
    fin.write(image) 
    fin.close() 
    print('Criptografia concluída ...') 
  
      
except Exception: 
    print('Error caught : ', Exception.__name__) 