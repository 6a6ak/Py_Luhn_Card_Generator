import random
import csv

def luhn_generate(prefix, length):
    """
    Generate a valid card number using the Luhn algorithm.
    """
    card_number = [int(d) for d in str(prefix)]
    while len(card_number) < (length - 1):
        card_number.append(random.randint(0, 9))
    checksum = calculate_luhn_checksum(card_number)
    card_number.append(checksum)
    return ''.join(map(str, card_number))

def calculate_luhn_checksum(digits):
    """
    Calculate the Luhn checksum.
    """
    checksum = 0
    reverse_digits = digits[::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return (10 - (checksum % 10)) % 10

def format_card_number(card_number):
    """
    Format the card number to include dashes every 4 digits.
    Example: 1234567812345678 -> 1234-5678-1234-5678
    """
    return '-'.join([card_number[i:i+4] for i in range(0, len(card_number), 4)])

def generate_cards_to_csv(prefix, length, count, file_name):
    """
    Generate and write formatted card numbers to a CSV file.
    """
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Card Number'])
        for _ in range(count):
            card_number = luhn_generate(prefix, length)
            formatted_card = format_card_number(card_number)
            writer.writerow([formatted_card])

# Configuration
card_prefix = 9  # Card prefix (e.g., 4 for Visa)
card_length = 16  # Card length (usually 16 digits)
card_count = 10000  # Number of cards to generate
output_file = f"valid_cards_{card_prefix}.csv"  # Output file name

# Generate the cards
generate_cards_to_csv(card_prefix, card_length, card_count, output_file)
print(f"{card_count} valid card numbers have been saved to {output_file}.")
