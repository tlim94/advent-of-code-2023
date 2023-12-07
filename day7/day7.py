from collections import Counter


class CamelCard:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)

    def __str__(self):
        return f"Hand: {self.hand} Bid: {self.bid}"

    def __eq__(self, other):
        return self.hand == other.hand

    def __lt__(self, other):
        for i in range(len(self.hand)):
            s = self.hand[i]
            o = other.hand[i]

            if s == o:
                continue
            else:
                return getCardValue(s) < getCardValue(o)

        return self.hand < other.hand


def getCardValue(card):
    value_mapping = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 1,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    return value_mapping.get(card, None)


def readFile():
    all_hands = []
    file_path = 'C:\day7_input.txt'

    try:
        with open(file_path, 'r') as file:
            for line in file:
                elements = line.strip().split()
                hand, bid = elements
                card = CamelCard(hand, bid)
                all_hands.append(card)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return all_hands


# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
def evaluateHand(card):
    counts = Counter(card.hand)
    numUnique = len(set(card.hand))
    values = sorted(counts.values(), reverse=True)

    mostCommonCount = values[0]
    secondCommonCount = values[1] if len(values) > 1 else 0

    if mostCommonCount == 4:
        return 6  # Five of a kind
    elif mostCommonCount == 4:
        return 5  # Four of a kind
    elif mostCommonCount == 3 and secondCommonCount == 2:
        return 4  # Full house
    elif mostCommonCount == 3:
        return 3  # Three of a kind
    elif mostCommonCount == 2 and secondCommonCount == 2:
        return 2  # Two pair
    elif mostCommonCount == 2:
        return 1  # One pair
    elif numUnique == 5:
        return 0  # High card
    else:
        return -1  # Invalid hand


def getMaxRank(card):
    maxRank = -1
    if 'J' in card.hand:

        for char in card.hand:
            if char == 'J':
                continue

            newHand = card.hand.replace('J', char)
            print(newHand)
            newCard = CamelCard(newHand, 0)
            maxRank = max(maxRank, evaluateHand(newCard))
    else:
        return evaluateHand(card)

    return maxRank


def main():
    all_hands = readFile()

    totalCards = [[] for _ in range(7)]
    orderedCards = []

    for card in all_hands:
        rank = getMaxRank(card)
        totalCards[rank].append(card)

    for i in range(len(totalCards)):
        print(i)
        for card in sorted(totalCards[i]):
            print(card)
        orderedCards += sorted(totalCards[i])

    i = 1
    sum = 0
    for card in orderedCards:
        sum += card.bid * i
        i += 1
        print(card)

    print(sum)


if __name__ == "__main__":
    main()
