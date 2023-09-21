class Bank() :
    clients = []
    name = "  Welcome In The International Bank Of Egypt.  "

    def update_db(self,client) :
        self.clients.append(client)
    def authentication(self,name,account_num) :
        for i in range(len(self.clients))    :
            if name in self.clients[i].accounts.values() and account_num in self.clients[i].accounts.values() :
                print()
                print("Authenticated Successfully!.")
                return self.clients[i]

