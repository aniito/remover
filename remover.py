import os
import time
import asyncio
# import script_kiddage
# from skid_universal import 2qi


async def main():
    print(""" 
             :     :
        __    |     |    _,_
       (  ~~^-l_____],.-~  /
        \\    ")\ "^k. (_,-"
         `>._  ' _ `\\  \\
      _.-~/'^k. (0)  ` (0
   .-~   {    ~` ~    ..T
  /   .   "-..       _.-'
 /    Y        .   "T
Y     l         ~-./l_
|      \\          . .<'
|       `-.._  __,/"r'
l   .-~~"-.    /    I
 Y         Y "~[    |
  \\         \_.^--, [
   \\            _~> |
    \\      ___)--~  |
     ^.       :     l
       ^.   _.j     |
         Y    I     |
         l    l     I
          Y    \\    |    #43G remover [discord.gg/FyY9Hvm8T8]
           \\    ^.  |
            \\     ~-^.
             ^.       ~"--.,_
              |~-._          ~-.
              |    ~Y--.,_      ^.
              :     :     "x      \\
                            \\      \\.
                             \\      ]
                              ^._  .^
                                 ~~
""")
    await asyncio.sleep(1)
    print(">>------> Skiddage en cours ", end="")
    for x in range(4):
        time.sleep(0.4)
        print(".", end="", flush=True)


def mrRboto_discord():
    print("mon serveur : https://discord.gg/FyY9Hvm8T8")
    print("tu auras compris que ce def sert à rien et donc est juste pour les personnes qui lisent le script vous êtes des bons !")




def prout():
    time.sleep(0.5)
    fid = input("\n\n>>------> mettez le fichier dans lequel vous indiquez les fichiers à enlever ! : ")
    os.system("clear")
    
    print("""                                        
                         ____________________
                        /                    \\
                        !  Attention  à      !
                        !     la  casse !    !
                        \\____________________/
                                 !  !
                                 !  !
                                 L_ !
                                / _)!
                               / /__L
                         _____/ (____)
                                (____)
                         _____  (____)
                              \_(____)
                                 !  !
                                 !  !
                                 \__/   
                                                                                                                                                                                                                                                                                               
           Attention Le script est à faire tourner en Super Utilisateur (Root)
           \\
            \\______ Si vous voulez supprimer des fichiers avec des permissions root -- faites un sudo su avant de lancer le script                                         

    """)
    print("pour arrêter faites CTRL + C ")
    attention = input("\n\nvoulez vous vraiment continuer ? : ")
    try:   
            print("je vais essayer avec le fichier que tu m'a envoyé sinon je fais avec remv.txt !")
            with open(fid, "r") as f:
                for line in f.readlines():
                        ski = line.strip()
                        os.system(f"sudo rm -rf {ski}")
                        print(f"{ski} à été supprimé ! \n")
                        
                
    except: 
        print(" \n\n |-- Erreur ! Le fichier que vous avez indiqué n'es pas trouvable ! --|")
        print("je fais donc avec le remv.txt")
        rvm = input("faites CTRL + C si vous ne voulez pas avec remv.txt ! continuer ? :")
        with open("remv.txt", "r") as f:
             for line in f.readlines():
                ski = line.strip()
                os.system(f"sudo rm -rf {ski}")
                print(f"{ski} à été supprimé ! \n")
    
    print("\n\n[+] FINIS retrouve moi sur discord https://discord.gg/FyY9Hvm8T8 !")       

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    prout()
