import sys

cards = "J23456789TQKA"

def substitute_jokers(hand_str):
	substituted_hands = []

	joker_indices = [index for index, card in enumerate(hand_str) if card == "J"]

	for subst_card in cards:

		hand_list = list(hand_str)

		for i in joker_indices:
			hand_list[i] = subst_card

		substituted_hands.append("".join(hand_list))

	return substituted_hands

def best_substitution(hand_str):
	return max(substitute_jokers(hand_str), key = encode_hand)

def encode_hand(hand_str):
	return sorted([hand_str.count(card) for card in set(hand_str)], reverse = True)

def encode_cards(hand_str):
	return [cards.index(card) for card in hand_str]

def main():
	hands = []

	for line in sys.stdin:
		hand_str, bid = line.split()
		hands.append((encode_hand(best_substitution(hand_str)), encode_cards(hand_str), int(bid)))

	hands.sort()

	print(sum(rank * hand[-1] for rank, hand in enumerate(hands, start = 1)))

if __name__ == "__main__":
	main()