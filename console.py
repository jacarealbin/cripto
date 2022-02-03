
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"



def menu():
    

     print(RED + '''
                                          
                       )      
     (   (          ( /(      
  (  )(  )\  `  )   )\()) (   
  )\(()\((_) /(/(  (_))/  )\  
 ((_)((_)(_)((_)_\ | |_  ((_) 
/ _|| '_|| || '_ \)|  _|/ _ \ 
\__||_|  |_|| .__/  \__|\___/ 
            |_|               

---------------Jk--------------- 
        

[1] - Criptografar foto
[2] - descriptografar foto
[S] - Sair
    ''')
     return str(input('Escolha uma opção: '))
 
opcao_escolhida = menu()
if opcao_escolhida == '1':
    import miain
if opcao_escolhida == '2':
    import main
    
    
 