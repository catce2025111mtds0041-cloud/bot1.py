#criando o cofre eletronico 
class Cofre_Eletronico:
    #função para definir a senha, estado e tentativas 
    def __init__(self, senha):
        self.senha = senha
        self.estado = "Fechado"
        self.tentativas_restantes = 3

    #função para abrir o cofre
    def abrir_cofre(self, senha):
        #se o numero de tentativas for ecedido 
        if self.tentativas_restantes == 0:
            print("❌ Cofre bloqueado! Sem tentativas restantes.")
            return False
        
        #se a senha for a correta 
        if senha == self.senha:
            #chamando  o estado com (self.estado)
            self.estado = "aberto"
            print("✅ Cofre aberto com sucesso!")
            # e mostrando o restante de tentativas restantes 
            self.tentativas_restantes = 3
            return True
        #em caso de multiplos erros 
        else:
            #exibir o tentativas_restantes
            self.tentativas_restantes -= 1
            print(f"⚠️ Senha incorreta! Tentativas restantes: {self.tentativas_restantes}")

            # se as tentativas chega a 0
            if self.tentativas_restantes == 0:
                print("🚫 Cofre bloqueado por excesso de tentativas.")
                return False
            

        #fechando o cofre
        def fechar_cofre(self):
            # se o cofre estiver aberto
            if self.estado == "aberto":
                #feche com "self.estado"
                self.estado = "fechado"
                print("🔒 Cofre fechado.")

            # se já estiver fechado 
            else:
                print("⚠️ O cofre já está fechado.")

        #Função para reserta as tentativas
        def reserta_tentativas(self):
            if self.estado == "Aberto":
                print("🔄 Tentativas resetadas para 3.")

            #se não
            else:
                print("❌ Não é possível resetar. O cofre está fechado.")

        #função para troca a senha
        def trocar_senha(self, senha_antiga, nova_senha):
            # se o cofer não estiver aberto 
            if self.estado != "Aberto":
                print("❌ O cofre precisa estar aberto para trocar a senha.")
                return False
            
            #criando nova senha
            if senha_antiga == self.senha:
                #criando uma nova senha
                self.senha = nova_senha
                print("🔑 Senha trocada com sucesso!")
                return True
            #caso a senha antiga for colocada errada
            else:
                print("⚠️ Senha antiga incorreta. Não foi possível trocar.")
                return False
            
            def __str__(self):
                return f"Cofre(estado='{self.estado}', tentativas_restantes={self.tentativas_restantes})"