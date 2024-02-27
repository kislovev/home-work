from deck_total import Card, Deck

"""
Cоздадим имитацию ходов в “Дурака без козырей”:

1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 10 карт
3. Второй игрок берет сверху 10 карт.
4. Игрок-1 ходит:
    4.1. игрок-1 выкладывает самую маленькую карту по "старшенству"
    4.2. игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
    4.3. Если игрок-2 не может побить карту, то он проигрывает/забирает себе(см. пункт 7)
    4.4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Если Игрок-2 отбился, то Игрок-1 и Игрок-2 меняются местами. Игрок-2 ходит, Игрок-1 отбивается.
6. Выведите в консоль максимально наглядную визуализацию данных ходов (библиотека rich)
7* Реализовать возможность добрать карты из колоды после того, как один из игроков отбился/взял в руку
"""
import random


VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
    'Spades': '♠',
    'Clubs': '♣',
    'Diamonds': '♦',
    'Hearts': '♥'
}


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __repr__(self) -> str:
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def equal_value(self, other_card):
        return self.value == other_card.value

    def __gr__(self, other_card):
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __lt__(self, other_card):
        if self.value == other_card.value:
            return SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return VALUES.index(self.value) < VALUES.index(other_card.value)


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def __str__(self) -> str:
        return (f'deck:{len(self.cards)}, Карты: {", ".join([str(i) for i in self.cards])}')

    def __repr__(self) -> str:
        return f'Deck {self}'

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        print(self)
        # print(f'deck:[{len(self.cards)}]: {
        #    ", ".join([str(i) for i in self.cards])}')

    def draw(self, x) -> list[Card]:
        # Принцип работы данного метода прописан в 00_task_deck.md
        cars_in_hand = self.cards[:x]
        self.cards = self.cards[x:]
        return cars_in_hand

    # получение значения по индексу
    def __getitem__(self, item):
        return self.cards.__getitem__(item)

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, cards, card_player=None) -> list[Card]:
        # Список карт в руке
        self.cards = cards
        self.card_player = card_player

    def __str__(self) -> str:
        return f'В руке карт осталось: {len(self.cards)}, карты: {self.cards}'

    def __repr__(self) -> str:
        return self.cards

    # получение значения по индексу
    def __getitem__(self, item):
        return self.cards.__getitem__(item)

    def get_unbreakable_card(self, card):
        self.cards.append(card)

    def rem_unbreakable_card(self, card):
        self.cards.remove(card)

    def move2(self, player, card):
        table = []
        bito = []
        print(f'Игрок 1 пошел_ картой {card[0]}')
        table.append(card[0])
        cards_same_suit = sorted([
            i for i in player if i.equal_suit(card[0])])
        if cards_same_suit != []:
            self.rem_unbreakable_card(card[0])
            max_card = None
            for i in cards_same_suit:
                if i > card[0]:
                    max_card = i
                    table.append(max_card)
                    player.rem_unbreakable_card(max_card)
                    bito.append(max_card)
                    print(f'Игрок 2 отбил картой {max_card}')
                    break
            if bito != []:
                print(f'карты на столе2 {table}')
                cart_in_pl1_val = [
                    i.value for i in table for j in self.cards if i.equal_value(j)]
                cart_in_pl1 = [
                    i for i in self.cards for j in set(cart_in_pl1_val) if i.value in j]
                if cart_in_pl1 != []:
                    print(f'карта(ы) у первого игрока, которыми можно еще раз ходить {
                        cart_in_pl1}')
                    self.move2(player, cart_in_pl1)
                else:
                    print('Игрок 2 отбился')
            else:
                print(f'Игрок 2 не смог отбиться')
                player.get_unbreakable_card(self.cards[0])
                self.rem_unbreakable_card(self.cards[0])
        else:
            print(f'Игрок 2 не смог отбиться')
            player.get_unbreakable_card(card[0])
            self.rem_unbreakable_card(card[0])

    def move(self, player):
        table = []
        bito = []
        print(f'Игрок 1 пошел картой {self.cards[0]}')
        table.append(self.cards[0])
        cards_same_suit = sorted([
            i for i in player if i.equal_suit(self.cards[0])])
        # если карты такой масти у игрока2 нет
        if cards_same_suit != []:
            self.rem_unbreakable_card(self.cards[0])
            max_card = None
            for i in cards_same_suit:
                if i > self.cards[0]:
                    max_card = i
                    table.append(max_card)
                    player.rem_unbreakable_card(max_card)
                    print(f'Игрок 2 отбил картой {max_card}')
                    bito.append(max_card)
                    break
            if max_card != []:
                print(f'карты на столе {table}')
                cart_in_pl1_val = [
                    i.value for i in table for j in self.cards if i.equal_value(j)]
                cart_in_pl1 = [
                    i for i in self.cards for j in set(cart_in_pl1_val) if i.value in j]

                if cart_in_pl1 != []:
                    print(f'карта(ы) у первого игрока, которыми можно еще раз ходить {
                        cart_in_pl1}')
                    self.move2(player, cart_in_pl1)
                else:
                    print('Игрок 2 отбился')
            else:
                print(f'Игрок 2 не смог отбиться')
                player.get_unbreakable_card(self.cards[0])
                self.rem_unbreakable_card(self.cards[0])
        else:
            print(f'Игрок 2 не смог отбиться')
            player.get_unbreakable_card(self.cards[0])
            self.rem_unbreakable_card(self.cards[0])


class Game:
    def __init__(self, player1, player2, table=[]):
        self.player1 = player1
        self.player2 = player2
        self.table = table

    def move(self):
        pass


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании

# Тусуем колоду
deck.shuffle()
deck.show()
print("="*30)

# Возьмем 5 карт "в руку"
pl1 = Player(sorted(deck.draw(10)))
print(pl1)
pl2 = Player(sorted(deck.draw(10)))
print(pl2)

pl1.move(pl2)

print(pl1)
print(pl2)
print('='*30)
pl2.move(pl1)
print(pl1)
print(pl2)