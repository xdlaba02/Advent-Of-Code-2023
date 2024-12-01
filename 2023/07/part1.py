import sys

def encode_hand(hand_str):
	return sorted([hand_str.count(card) for card in set(hand_str)], reverse = True)

def encode_cards(hand_str):
	return ["23456789TJQKA".index(card) for card in hand_str]

def main():
	hands = []

	for line in sys.stdin:
		hand_str, bid = line.split()
		hands.append((hand_str, int(bid)))

	hands.sort(key = lambda hand: (encode_hand(hand[0]), encode_cards(hand[0])))

	print(sum(rank * hand[1] for rank, hand in enumerate(hands, start = 1)))

if __name__ == "__main__":
	main()