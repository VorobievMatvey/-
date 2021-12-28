class Wallet:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'Клиент "{self.name}". Баланс: {self.balance} руб.'

client_1 = Wallet("Иван Петров", "50")
client_2 = Wallet("Петр Иванов", "150")
client_3 = Wallet("Глеб Тахов", "300")

clients = [client_1, client_2, client_3]

for client in clients:
    print(client.__str__())
